import os
import jinja2

DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')

PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])
