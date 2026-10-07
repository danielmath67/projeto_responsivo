from django.test import TestCase, override_settings
from django.core import mail
from .models import Servico


class InstitutionalSiteTests(TestCase):
    def test_home_only_shows_active_services(self):
        Servico.objects.create(servico='Desenvolvimento web', descricao='Sites sob medida', icone='lni-cog')
        Servico.objects.create(servico='Serviço oculto', descricao='Não publicado', icone='lni-cog', ativo=False)
        response = self.client.get('/')
        self.assertContains(response, 'Desenvolvimento web')
        self.assertNotContains(response, 'Serviço oculto')
        self.assertContains(response, 'Nexo')
        self.assertNotContains(response, 'Geek University')

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_contact_sends_validated_message(self):
        response = self.client.post('/', {'nome': 'Visitante', 'email': 'visitante@example.com', 'assunto': 'Projeto', 'mensagem': 'Gostaria de um site.'})
        self.assertRedirects(response, '/')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].extra_headers['Reply-To'], 'visitante@example.com')

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_invalid_contact_keeps_form_and_does_not_send(self):
        response = self.client.post('/', {'nome': 'Visitante', 'email': 'invalido', 'assunto': 'Projeto', 'mensagem': 'Olá'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Revise os campos')
        self.assertEqual(len(mail.outbox), 0)
