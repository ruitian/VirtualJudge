import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')

    SECRET_KEY = 'you-will-never-guess'
    CSRF_ENABLED = True
    FLASK_POSTS_PER_PAGE = 10
    UPLOAD_FOLDER = BASE_DIR + '/app/uploads'
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    DEFAULT_PASSWORD = '123'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/dev_db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/comdb'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/comdb'

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
