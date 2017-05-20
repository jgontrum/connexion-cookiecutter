from {{cookiecutter.project_slug}}.app import app


# Get Flask app
flask_app = app.app
flask_app.testing = True
client = flask_app.test_client()
