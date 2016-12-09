import logging
import logging.handlers

import connexion
logging.basicConfig(level=logging.INFO)

app = connexion.App("{{cookiecutter.project_name}}")
application = app.app
app.add_api("config/api.yml",
            strict_validation=True)

if __name__ == '__main__':
    app.run(port=8080, server='flask')
