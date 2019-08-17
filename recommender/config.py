import os


def get_env_variable(name, default=None):
    try:
        return os.environ[name]
    except KeyError:
        if (default == None):
            message = f"Expected environment variable '{name}' not set."
            raise Exception(message)
        else:
            return default

# Some global constants
API_URL = get_env_variable("API_URL", default="https://api.mobilise.xyz")
API_KEY = get_env_variable("API_KEY", default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjRhNDYxNTJiLTUyY2MtNGI1Yy05ZjY3LTAzOWE3NmYwNTRkNCIsImlhdCI6MTU2MTcyMTY4MywiZXhwIjoxNTYyMzIxNjIzfQ.VSx63pK4cw1iCad_4Y_TRZfwYGUBuKuSiu12ZMGhgrE")


# Flask app configuration
class Config:
    DB_NAME = get_env_variable("DB_NAME")
    DB_PORT = get_env_variable("DB_PORT")
    SQLALCHEMY_DATABASE_URI = f"postgres://{DB_NAME}:{DB_PORT}"


class DevelopmentConfig(Config):
    ENV = "DEVELOPMENT"


class ProductionConfig(Config):
    ENV = "PRODUCTION"
