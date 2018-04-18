import os

basedir = os.path.abspath(os.path.dirname(__file__))

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PW = os.environ['POSTGRES_PW']
POSTGRES_URL = os.environ['POSTGRES_URL']
POSTGRES_DB = os.environ['POSTGRES_DB']

DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL,
                                                      db=POSTGRES_DB)

# base config
class BaseConfig:
    SECRET_KEY = 'CAN_YOU_KEEP_MY_SECRET'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DB_URL

# dev config
class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

# prod config
class ProductionConfig(BaseConfig):
    SECRET_KEY = 'NO_I_CANT'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_map = dict(dev=DevConfig, prod=ProductionConfig)