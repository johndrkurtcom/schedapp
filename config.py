import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass
        
class DeployConfig(Config):
    DEBUG=False
    

config={'default': DeployConfig}
