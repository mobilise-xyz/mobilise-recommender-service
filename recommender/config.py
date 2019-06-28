import os


def get_env_variable(name, default=None):
    try:
        return os.environ[name]
    except KeyError:
        if (default == None):
            message = "Expected environment variable '{}' not set.".format(name)
            raise Exception(message)
        else:
            return default

# Some global constants
API_URL = get_env_variable("API_URL", default="https://api.mobilise.xyz")
API_KEY = get_env_variable("API_KEY", default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjRhNDYxNTJiLTUyY2MtNGI1Yy05ZjY3LTAzOWE3NmYwNTRkNCIsImlhdCI6MTU2MTcyMTY4MywiZXhwIjoxNTYyMzIxNjIzfQ.VSx63pK4cw1iCad_4Y_TRZfwYGUBuKuSiu12ZMGhgrE")

# Flask app configuration
class Config:
    pass


class DevelopmentConfig(Config):
    ENV = "DEVELOPMENT"


class ProductionConfig(Config):
    ENV = "PRODUCTION"
