from {{cookiecutter.project_slug}}.app import app


def run(debug=False):
    app.run(port=8080, debug=debug, server='flask')


def run_debug():
    run(debug=True)
