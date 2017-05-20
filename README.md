# Connexion Cookiecutter Template

This Cookiecutter template helps you setting up a RESTful API in minutes. Just answer some questions about you and your projects and a ready-to-go python project will be created.

## Requirements

- Python
- Cookiecutter. Just run ```pip install cookiecutter``` :)

## Usage

```bash
cookiecutter https://github.com/jgontrum/connexion-cookiecutter.git

cd <PROJECTNAME>/
make
env/bin/start_debug
```

## Features

- Ready-to-go **Python 3.6** project
- Routing defined in **Swagger** definition
- Strict **model validation** by default
- **Dockerfile**
- Deployed as a uwsgi app behind nginx
- Direct support for static files (-> nginx)
- **Logstash** configuration (optional)
- Examples for **unit and integration tests**
- **Coverage reports** for tests
- Configuration for SonarQube


## Scripts
```make``` Build project

```make clean``` Clean folder

```make test``` Run tests

```make build-and-push``` Build Docker image and push to repository
