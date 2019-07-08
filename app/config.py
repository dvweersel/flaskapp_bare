import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get('SECREY_KEY')

class TestConfig(BaseConfig):
    DEBUG = False
    TESTING = True


class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = False


class ProdConfig(DevConfig):
    DEBUG = False
    TESTING = False
