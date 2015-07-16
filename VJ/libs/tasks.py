from VJ import app
from celery import Celery
from base64 import b64encode

from crawl import (
    AccountCrawler,
    CodeSubmitCrawler
)

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
    crawler = AccountCrawler()
    crawler.crawl(
        origin_oj,
        username,
        password
    )

@celery.task()
def code_submit(
        origin_oj,
        solution_id,
        problem_id,
        language,
        code,
        username,
        password):
    crawler = CodeSubmitCrawler()
    crawler.crawl(
        origin_oj,
        solution_id,
        problem_id,
        language,
        b64encode(code),
        username,
        password
    )
