# Nexo — site institucional com Django

Site demonstrativo de uma empresa fictícia, com apresentação de serviços, equipe e formulário de contato.

## Recursos
- Serviços, cargos e funcionários gerenciados no Django Admin.
- Upload de fotos com miniaturas; banco SQLite local ou PostgreSQL via DATABASE_URL.
- Formulário validado pelo Django e envio por e-mail; backend de console por padrão.
- Interface responsiva, com personalização visual do template Fusion.
- Listagens ordenadas, exibindo apenas registros ativos.

## Executar (Python 3.10 ou superior)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Abra http://127.0.0.1:8000 e cadastre serviços e equipe em /admin/.
As variáveis são lidas do ambiente: o arquivo .env.example é apenas uma referência, não é carregado automaticamente.

## Verificar
```bash
python manage.py check
python manage.py test
```

## Publicação
Configure DEBUG=False, SECRET_KEY, ALLOWED_HOSTS e CSRF_TRUSTED_ORIGINS (URLs HTTPS), DATABASE_URL e SMTP. Execute migrate e collectstatic. O Procfile usa Gunicorn; arquivos estáticos são atendidos pelo WhiteNoise. Fotos enviadas precisam de armazenamento persistente e serviço próprio para mídia em produção; o Django serve mídia apenas no desenvolvimento. HTTPS é configurado no provedor de hospedagem. Não publique senhas, banco local ou uploads pessoais.

## Origem e escopo
Projeto adaptado de uma base didática fornecida, com template Fusion da UIdeck. As alterações incluem marca fictícia Nexo, paleta verde-petróleo, tipografia, cartões, textos em português e ajustes de configuração. Mantenha a atribuição do template e verifique a licença original antes de redistribuir seus assets. Nenhuma licença dos assets foi inferida nesta adaptação.

Os planos e depoimentos fictícios da base foram substituídos por processo de trabalho e descrição do projeto. Não há checkout, assinaturas, dashboard de métricas ou cadastro público. As mensagens de contato são enviadas por e-mail, não armazenadas no banco.
