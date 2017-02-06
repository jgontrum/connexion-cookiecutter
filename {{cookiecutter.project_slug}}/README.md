# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

The API can be reached under ```http://localhost:{{cookiecutter.api_port}}/api/v1```.

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

Go to [here](http://localhost:{{cookiecutter.api_port}}/api/v1/ui) to view the brilliant SwaggerUI documentation of your API.

## Healthcheck

Configure a health check under /api/v1/health (GET).

The check should return 200 if everything is fine, 424 if a depending service is not working or 503 if the API does not work correctly.
Additionally, a JSON is returned containing the fields 'health', 'dependencies' and 'message'. The first one defines the color ('green', 'yellow', 'red') that
correspond to the status codes. The second one is the name of the depending services that cannot be reached and 'message'
can hold a string defining the cause of a problem.

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
    tcp {
        codec => json {}
        type => "{{cookiecutter.project_slug}}_logs"
        port => {{cookiecutter.logstash_log_port}}
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

### Swagger
[API.yml Editor](http://editor.swagger.io/#/)
