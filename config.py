import os 
basedir = os.path.abspath(os.path.dirname(__name__)) # (gets you base directory for config.py)
class Config():
    FLASK_APP = os.environ.get('FLASK_APP') # what is the entrypoint to the application
    FLASK_ENV = os.environ.get('FLASK_ENV') # could hardcode this in as 'development'