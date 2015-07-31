from VJ import app, mail
from flask.ext.mail import Message
from flask import render_template
from celery import Celery

from crawl import (
    OriginOJCrawler,
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
def send_email(to, subject, template, **kwargs):
    msg = Message(
        app.config['VJ_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
        sender=app.config['VJ_MAIL_SENDER'],
        recipients=[to]
    )
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


@celery.task()
def origin_oj_crawler(origin_oj):
    crawler = OriginOJCrawler()
    crawler.crawl(origin_oj)


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
        nickname,
        password):
    crawler = CodeSubmitCrawler()
    crawler.crawl(
        origin_oj,
        solution_id,
        problem_id,
        language,
        code,
        username,
        nickname,
        password
    )


@celery.task()
def test(a, b):
    return a + b
