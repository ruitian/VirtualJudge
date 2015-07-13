import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    SECRET_KEY = 'you-will-never-guess'
    CSRF_ENABLED = True
    PROBLEM_PER_PAGE = 20
    CONTEST_PER_PAGE = 20
    STATUS_PER_PAGE = 50
    UPLOAD_FOLDER = BASE_DIR + '/app/uploads'
    GRAVATAR_BASE_URL = 'http://gravatar.duoshuo.com/avatar/'
    MONGODB_SETTINGS = {
        'db': 'OJCC',
        'username': '',
        'password': '',
        'host': '127.0.0.1',
        'port': 27017
    }

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
