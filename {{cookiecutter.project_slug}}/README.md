# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

The API can be reached under ```http://localhost:{{cookiecutter.api_port}}/api/```.

## Requirements

- Python 3.5: [Instructions](https://www.python.org/downloads/)

- virtualenv: [Instructions](https://virtualenv.pypa.io/en/stable/installation/)

## Installation

Run ```make``` for a local setup and then ```env/bin/start_debug``` to start the API in debug mode.

To start the uWSGI, run ```make start```

## Procedure

First, define your REST API in the configuration under ```/config/api.yml```, 
then add the Python logic for the *operationId* under /{{cookiecutter.project_slug}}/api

## SwaggerUI

Go to [here](http://localhost:{{cookiecutter.api_port}}/api/ui) to view the brilliant SwaggerUI documentation of your API.

## Logstash

By default, this project sends request logs and other (e.g. error logs) to different logstash UDP ports.

Configure the logstash input like this:

```
input {
    udp {
        codec => json {}
        type => "{{cookiecutter.project_slug}}"
        port => {{cookiecutter.logstash_request_port}}   
    }
    udp {
        codec => json {}
        type => "{{cookiecutter.project_slug}}_uwsgi"
        port => {{cookiecutter.logstash_uwsgi_port}}   
    }
}

filter {
    if [type] == "{{cookiecutter.project_slug}}" {
        json {
            source => "message"
        }
        mutate {
            remove_field => [ 'message' ]
        }
    }
}
```

## Resources
### Connexion
[Documentation](https://connexion.readthedocs.io/en/latest/)
[Github](https://github.com/zalando/connexion)
