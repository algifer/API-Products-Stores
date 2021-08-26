"""
@file config.py
@ingroup CARGAMOS
@project Test
@brief
        This software is copyright protected and proprietary to CARGAMOS.
                All other rights remain with CARGAMOS.
@author Algemiro J. Gil Fernandez
@version Module: 1.0.0.0
@delivery 202108
@date 2021-08-25
@company CARGAMOS
@description:	This document follows the standards defined in
                https://devguide.python.org/documenting/
@known issues:  None

"""
__author__ = "Algemiro J. Gil Fernandez"
__copyright__ = "Copyright 2010, CARGAMOS"
__licence__ = "GPL"
__version__ = "1.0.0.0"
__maintainer__ = "Algemiro Jose Gil Fernandez"
__email__ = "algifer53@gmail.com"
__status__ = "Production"

# Get absolut path
import os
dir = os.path.abspath("./")


class Config:
    """
    @class Config
    @brief This class defines parameters to be used in the server.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'Set_a_very_dificult_key')
    DEBUG = False
    BUNDLE_ERRORS = True
    HOST = "localhost"
    PORT = 5000
    SERVER_NAME = HOST+":"+str(PORT)
    DATABASE_URI = 'postgresql://postgres:#12345@localhost/Shop_products'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class DevConfig(Config):
    """
    @class DevConfig
    @brief This class configure the parameters to be used in the 
            development environment.
    """
    ENV = 'development'
    DEBUG = True
    HOST = "localhost.localhost"
    PORT = 5000
    SERVER_NAME = HOST+":"+str(PORT)
    DATABASE_URI = 'postgresql://postgres:#12345@localhost/Shop_products'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI


class TestConfig(Config):
    """
    @class TestConfig
    @brief This class configure the parameters to be used in the testing 
            environment.
    """
    ENV = 'testing'
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    HOST = "127.0.0.1"
    PORT = 5000
    SERVER_NAME = HOST+":"+str(PORT)
    DATABASE_URI = 'postgresql://postgres:#12345@localhost/Shop_products'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI


class ProdConfig(Config):
    """
    @class Service
    @brief This class configure the parameters to be used in the 
            production environment."""
    DEBUG = False
    ENV = 'production'

# Environment selection parameter.
config_by_name = dict(
    dev=DevConfig,
    test=TestConfig,
    prod=ProdConfig
)

# Application secret key configuration parameter
key = Config.SECRET_KEY

# Configuration parameter of logs in console.
logging_config = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in '+
                    '%(module)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'custom_handler': {
            'class' : 'logging.FileHandler',
            'formatter': 'default',
            'filename': '{}/logs/app.log'.format(dir)
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'custom_handler']
    }
}

# Configuration parameter of the waiting time in coroutines.
DELAY_TIME = 4 

