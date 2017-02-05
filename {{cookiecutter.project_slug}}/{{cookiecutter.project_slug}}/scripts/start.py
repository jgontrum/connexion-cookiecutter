import logging

import logstash

from {{cookiecutter.project_slug}}.app import app
from {{cookiecutter.project_slug}} import options


def run(debug=False):
    # Logging configuration
    logger = logging.getLogger('main')
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logstash_options = options()['logstash']
    ls = logstash.TCPLogstashHandler(
        host=logstash_options['host'],
        port=logstash_options['port'])
    ls.setLevel(logging.INFO)
    logger.addHandler(ls)

    app.run(port=8080, debug=debug, server='flask')


def run_debug():
    run(debug=True)
