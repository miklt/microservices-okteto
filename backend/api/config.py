import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ENV = 'productione'
    TESTING = False            
    DEBUG = False
    DEVELOPMENT = False
    CSRF_ENABLED = True
    SECRET_KEY = "secret_for_test_environment"    
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")    
    
class ProductionConfig(Config):
    ENV = 'productiona'
    TESTING = False            
    DEBUG = False
    DEVELOPMENT = False
    CSRF_ENABLED = True
    SECRET_KEY = "secret_for_production_environment"    
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")    

class DevelopmentConfig(Config):
    ENV = 'developmento'
    TESTING = True 
    DEBUG= True,    
    DEVELOPMENT = True
    CSRF_ENABLED = True
    SECRET_KEY = "secret_for_test_environment"    
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_DEV")