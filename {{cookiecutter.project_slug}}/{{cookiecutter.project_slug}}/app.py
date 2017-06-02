import logging

{% if cookiecutter.use_logstash.startswith('y') -%}
import logstash
{%- endif %}
import connexion
import yaml
import json
from prance import ResolvingParser

from {{cookiecutter.project_slug}} import options

logging.basicConfig(level=logging.INFO)

# Logging configuration
logger = logging.getLogger('main')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

{% if cookiecutter.use_logstash.startswith('y') -%}
logstash_options = options()['logstash']
ls = logstash.TCPLogstashHandler(
    host=logstash_options['host'],
    port=logstash_options['port'])
ls.setLevel(logging.INFO)
logger.addHandler(ls)
{%- endif %}

app = connexion.App("{{cookiecutter.project_name}}")
parsed_definition = yaml.load(open("config/api.yml"))
swagger_definiton = ResolvingParser(
    spec_string=json.dumps(parsed_definition)).specification
app.add_api(swagger_definiton,
            strict_validation=True,
            validate_responses=True)

application = app.app

if __name__ == '__main__':
    app.run(port=8080, server='flask')
