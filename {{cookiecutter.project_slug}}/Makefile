.PHONY: clean start build-docker start-docker

all: env/bin/python

env/bin/python:
	virtualenv env -p python3.5 --no-site-packages
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

build-docker: clean
	docker build -t {{cookiecutter.username_slug}}/{{cookiecutter.project_slug}} .

start-docker:
	mkdir -p /tmp/{{cookiecutter.project_slug}}-logs
	docker run --name "{{cookiecutter.project_slug}}" -p "127.0.0.1:{{cookiecutter.api_port}}:{{cookiecutter.api_port}}" -v "/tmp/{{cookiecutter.project_slug}}-logs:/app/logs" {{cookiecutter.username_slug}}/{{cookiecutter.project_slug}}

start: env/bin/python
	env/bin/uwsgi --yaml=config/uwsgi.yml
