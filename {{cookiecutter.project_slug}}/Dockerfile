FROM python:3.5
MAINTAINER {{cookiecutter.full_name}} <{{cookiecutter.email}}>

RUN mkdir /app
RUN pip install virtualenv

COPY . /app
RUN cd /app && make

WORKDIR /app
EXPOSE {{cookiecutter.api_port}}
CMD make start
