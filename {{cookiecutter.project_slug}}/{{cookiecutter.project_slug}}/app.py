import logging

{% if cookiecutter.use_logstash.startswith('y') -%}
import logstash
{%- endif %}
import connexion

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

{%- if cookiecutter.use_logstash.startswith('y') -%}
logstash_options = options()['logstash']
ls = logstash.TCPLogstashHandler(
    host=logstash_options['host'],
    port=logstash_options['port'])
ls.setLevel(logging.INFO)
logger.addHandler(ls)
{%- endif %}

app = connexion.App("{{cookiecutter.project_name}}")
application = app.app
app.add_api("config/api.yml",
            strict_validation=True,
            validate_responses=True)

if __name__ == '__main__':
    app.run(port=8080, server='flask')
