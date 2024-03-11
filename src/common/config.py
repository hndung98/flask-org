import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

# basedir = os.path.abspath(os.path.dirname(__file__))

# class Config:
#     SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
#     DEBUG = False


# class DevelopmentConfig(Config):
#     # uncomment the line below to use postgres
#     # SQLALCHEMY_DATABASE_URI = postgres_local_base
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# class TestingConfig(Config):
#     DEBUG = True
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
#     PRESERVE_CONTEXT_ON_EXCEPTION = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# class ProductionConfig(Config):
#     DEBUG = False
#     # uncomment the line below to use postgres
#     # SQLALCHEMY_DATABASE_URI = postgres_local_base


# config_by_name = dict(
#     dev=DevelopmentConfig,
#     test=TestingConfig,
#     prod=ProductionConfig
# )

# key = Config.SECRET_KEY

from dotenv import load_dotenv
load_dotenv()

FLASK_HOST = os.environ.get("FLASK_HOST")
FLASK_PORT = os.environ.get("FLASK_PORT")
ADMIN_USER = os.environ.get("ADMIN_USER")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
SECRET_KEY = os.environ.get("SECRET_KEY")

DBS_HOSTNAME = os.environ.get("DBS_HOSTNAME")
DBS_DATABASE_NAME = os.environ.get("DBS_DATABASE_NAME")
DBS_PORT = os.environ.get("DBS_PORT")
DBS_USERNAME = os.environ.get("DBS_USERNAME")
DBS_PASSWORD = os.environ.get("DBS_PASSWORD")
