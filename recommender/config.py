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


# Flask app configuration
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_NAME = get_env_variable("DB_NAME")
    DB_HOST = get_env_variable("DB_HOST")
    DB_PORT = get_env_variable("DB_PORT")
    DB_USERNAME = get_env_variable("DB_USERNAME")
    DB_PASSWORD = get_env_variable("DB_PASSWORD")
    SQLALCHEMY_DATABASE_URI = f"postgres://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    COMPUTATION_KEY = get_env_variable("COMPUTATION_KEY")


class DevelopmentConfig(Config):
    ENV = "DEVELOPMENT"


class ProductionConfig(Config):
    ENV = "PRODUCTION"
