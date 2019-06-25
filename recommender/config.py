import os


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# Some global constants
API_URL = get_env_variable("API_URL")
API_KEY = get_env_variable("API_KEY")

# Flask app configuration
class Config:
    pass


class DevelopmentConfig(Config):
    ENV = "DEVELOPMENT"


class ProductionConfig(Config):
    ENV = "PRODUCTION"
