# Cinema

## About

The project was developed as part of term paper on subject "Databases".

## Quick install for development

Create Python virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Update pip and install project requirements:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Also you need some Postgres server. If you have Postgres installed natively, just make sure it works correctly. Otherwise You can run Postgres in Docker container using Docker compose. Just run:

```bash
docker compose -f postgres/docker-compose.yml up -d
```

After that You can migrate DB structure and run Django development server:

```bash
src/manage.py migrate
src/manage.py runserver
```
