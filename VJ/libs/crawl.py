from billiard import Process

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging  # noqa

from base64 import b64encode

settings = get_project_settings()


class Crawler():

    def __init__(self):
        self.crawler = CrawlerProcess(settings)


class OriginOJCrawler(Crawler):

    def _crawl(self, origin_oj):
        self.crawler.crawl(
            origin_oj + '_init',
        )
        self.crawler.start()
        self.crawler.stop()

    def crawl(self, origin_oj):
        p = Process(
            target=self._crawl,
            args=[origin_oj]
        )
        p.start()
        p.join()


class CodeSubmitCrawler(Crawler):

    def _crawl(
            self,
            origin_oj,
            solution_id,
            problem_id,
            language,
            code,
            username,
            password):
        self.crawler.crawl(
            origin_oj + '_submit',
            solution_id=solution_id,
            problem_id=problem_id,
            language=language,
            source=b64encode(code),
            username=username,
            password=password
        )
        self.crawler.start()
        self.crawler.stop()

    def crawl(
            self,
            origin_oj,
            solution_id,
            problem_id,
            language,
            code,
            username,
            password):
        p = Process(
            target=self._crawl,
            args=[
                origin_oj,
                solution_id,
                problem_id,
                language,
                code,
                username,
                password
            ]
        )
        p.start()
        p.join()


class AccountCrawler(Crawler):

    def _crawl(self, origin_oj, username, password):
        self.crawler.crawl(
            origin_oj + '_user',
            username=username,
            password=password
        )
        self.crawler.start()
        self.crawler.stop()

    def crawl(self, origin_oj, username, password):
        p = Process(
            target=self._crawl,
            args=[
                origin_oj,
                username,
                password
            ]
        )
        p.start()
        p.join()
