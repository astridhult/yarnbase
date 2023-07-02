# Yarn database

Astrid's awesome yarn database is here!

## Basic setup

After downloading this repository you first need to configure Django's environment variables. Copy the file `.env.example` and rename it to `.env` like so:

```bash
cp .env.example .env
```

Now you should be able to run django and get an error that there is no database:

```bash
poetry shell
./manage.py runserver
# or
poetry run python manage.py runserver
```

You can run the database in a docker container like so:

```bash
docker compose up -d
```

After this runserver should work.

## General tips

When starting with a fresh database you always need to run the migrations:

```bash
docker compose down -v  # Stop the database _AND_ remove all the data!!
docker compose up -d  # Start a fresh database
./manage.py migrate  # Apply Django's migrations
```

You can also get an actual sql prompt in the database like so:

```bash
docker exec -it garn-postgres-1 bash  # if the name does not exist use docker ps to list containers
psql -U yarn
```

After making changes to models in Django you need to make new migration to integrate the new stuff into the database schema like so:

```bash
./manage.py makemigrations
```
