from VJ import app
from celery import Celery

from crawl import AccountInitCrawler

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)

@celery.task()
def account_init(origin_oj, username, password):
    crawler = AccountInitCrawler()
    crawler.crawl(
        origin_oj,
        username,
        password
    )
