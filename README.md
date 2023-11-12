# Backend for "Shoot Children's scares" game

Backend in Django that provides data to the front end via an API

> [!NOTE]
> It is currently not used because our MVP is not connected to any external data source.

## Installing and running locally

1. Install the project
```bash
poetry install
```
2. Copy `settings_sample.py` to `settings.py`, make necessary changes before deploying to production (see Django manual).

3. Apply migrations
```bash
poetry run python manage.py makemigrations api
poetry run python manage.py migrate
```

4. If you want to run the server locally:

```bash
poetry run python manage.py runserver
```
