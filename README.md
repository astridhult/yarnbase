Something something run things

Ater running the docker container with the database like so:
```
docker compose up -d
```

You can get an sql prompt like so:
```
docker exec -it garn-postgres-1 bash  # if the name does not exist use docker ps to list containers
psql -U yarn
```
