# -*- coding: utf-8 -*-
from celery.schedules import crontab

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    import sys
    reload(sys)  # noqa
    sys.setdefaultencoding('utf-8')

    SECRET_KEY = (
        os.environ.get('SECRET_KEY') or
        u'\x97\xfa%\xab\xd2\xc2\xf8\xfc\xef\xaeTKDk\xc0\xe1//($\xc7\xc0'
    )

    CSRF_ENABLED = True

    SERVER_NAME = os.getenv('VJ_SERVER_NAME') or 'vj.sdutacm.org'

    # pagination
    PROBLEM_PER_PAGE = 20
    CONTEST_PER_PAGE = 20
    STATUS_PER_PAGE = 50
    FOLLOWERS_PER_PAGE = 20
    FOLLOWING_PER_PAGE = 20
    UPLOAD_FOLDER = BASE_DIR + '/app/uploads'
    GRAVATAR_BASE_URL = 'http://gravatar.duoshuo.com/avatar/'

    # mongodb
    MONGODB_SETTINGS = {
        'db': 'OJCC',
        'username': '',
        'password': '',
        'host': '127.0.0.1',
        'port': 27017
    }

    # email
    MAIL_SERVER = 'smtp.sina.cn'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    VJ_MAIL_SUBJECT_PREFIX = '[Virtual Judge]'
    VJ_MAIL_SENDER = os.environ.get('MAIL_USERNAME')
    VJ_ADMIN = os.environ.get('VJ_ADMIN')

    # redis
    REDIS_URL = 'redis://%s:%s/%s' % (
        os.environ.get('REDIS_HOST', 'localhost'),
        os.environ.get('REDIS_PORT', '6379'),
        os.environ.get('REDIS_DATABASE', '1'),
    )

    # celery
    CELERY_BROKER_URL = 'redis://%s:%s' % (
        os.environ.get('REDIS_HOST', 'localhost'),
        os.environ.get('REDIS_PORT', '6379')
    )
    CELERY_BROKER_BACKEND = 'redis://%s:%s' % (
        os.environ.get('REDIS_HOST', 'localhost'),
        os.environ.get('REDIS_PORT', '6379')
    )
    CELERYBEAT_SCHEDULE = {
        'test': {
            'task': 'VJ.libs.tasks.test',
            'schedule': crontab(minute='*/1'),
            'args': (1, 2)
        },
        'hdu': {
            'task': 'VJ.libs.tasks.origin_oj_crawler',
            'schedule': crontab(minute=0, hour=3),
            'args': ['hdu']
        },
        'sdut': {
            'task': 'VJ.libs.tasks.origin_oj_crawler',
            'schedule': crontab(minute=0, hour=3),
            'args': ['sdut']
        },
        'fzu': {
            'task': 'VJ.libs.tasks.origin_oj_crawler',
            'schedule': crontab(minute=0, hour=3),
            'args': ['fzu']
        },
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
