import webapp.config.Database as db

class Config(object):
  #SECRET_KEY = 'oswscript-clave-secreta'
  SERVER_NAME = "oswflask.com"
 
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/pruebaflask'

  SQLALCHEMY_TRACK_MODIFICATIONS = False

class Dev(Config):
  DEBUG = True
  
class Prod(Config):
  DEBUG = False
