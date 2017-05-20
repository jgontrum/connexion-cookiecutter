.PHONY: clean start {% if cookiecutter.use_docker.startswith('y') %}build-docker build-and-push start-docker attach-to-docker{% endif %}

all: env/bin/python

env/bin/python:
	python3.6 -m venv env
	env/bin/pip install --upgrade pip
	env/bin/pip install wheel
	env/bin/pip install -r requirements.txt
	env/bin/python setup.py develop

clean:
	rm -rfv bin develop-eggs dist downloads eggs env parts
	rm -fv .DS_Store .coverage .installed.cfg bootstrap.py
	rm -fv logs/*.txt
	find . -name '*.pyc' -exec rm -fv {} \;
	find . -name '*.pyo' -exec rm -fv {} \;
	find . -depth -name '*.egg-info' -exec rm -rfv {} \;
	find . -depth -name '__pycache__' -exec rm -rfv {} \;

start: env/bin/python
	env/bin/uwsgi --yaml=config/uwsgi.yml

{% if cookiecutter.use_docker.startswith('y') -%}
build-docker:
	docker build -t {{cookiecutter.docker_repository}}{{'/' if cookiecutter.docker_repository else ''}}{{cookiecutter.docker_project_name}}:{{cookiecutter.docker_default_tag}} .

build-and-push: build-docker
	docker push {{cookiecutter.docker_repository}}{{'/' if cookiecutter.docker_repository else ''}}{{cookiecutter.docker_project_name}}:{{cookiecutter.docker_default_tag}}

start-docker:
	docker rm {{cookiecutter.project_slug}} || true
	docker run --name "{{cookiecutter.project_slug}}" -p "127.0.0.1:{{cookiecutter.api_port}}:{{cookiecutter.api_port}}" {{cookiecutter.docker_repository}}{{'/' if cookiecutter.docker_repository else ''}}{{cookiecutter.docker_project_name}}:{{cookiecutter.docker_default_tag}}

attach-to-docker:
	 docker exec -i -t {{cookiecutter.project_slug}} /bin/bash 
{%- endif -%}

update-all-packages: env/bin/python
	 env/bin/pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 env/bin/pip install -U

test: env/bin/python
	env/bin/py.test --cov={{cookiecutter.project_slug}} {{cookiecutter.project_slug}}_test -vv
