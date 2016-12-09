from setuptools import setup

setup(
    name='{{cookiecutter.project_slug}}',
    version='0.1',
    description='{{cookiecutter.project_description}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    include_package_data=True,
    license='{{cookiecutter.license}}',
    entry_points={
          'console_scripts': [
              'start = {{cookiecutter.project_slug}}.scripts.start:run',
              'start_debug = {{cookiecutter.project_slug}}.scripts.start:run_debug'
          ]
      }
)
