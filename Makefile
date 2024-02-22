#Local DB
DB_URL="postgresql://postgres:mysecretpassword@localhost:5435/ocel2db"

#Local Backend Config
VERSION=1.0.0
IMAGE_NAME = ppmt-backend
SECRET_KEY = $(shell openssl rand -hex 32)
BACKEND_VERSION  = $(shell git describe --tags)

prepare: 
	docker run --name postgres_ocel2 -p 5435:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres:14

createdb:
	docker exec -it postgres_ocel2 createdb --username=postgres --owner=postgres ocel2db

startdb:
	docker start postgres_ocel2

stopdb:
	docker stop postgres_ocel2

run:
	poetry shell
	DB_URL=$(DB_URL) SECRET_KEY=$(SECRET_KEY) uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

ker push ${AWS_REPO_KEY}/${IMAGE_NAME}:v$$(echo $${VERSION})

.PHONY: prepare createdb startdb stopdb run 
