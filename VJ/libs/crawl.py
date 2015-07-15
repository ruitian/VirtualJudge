from billiard import Process

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy.utils.log import configure_logging

settings = get_project_settings()

class AccountInitCrawler():

    def __init__(self):
        self.crawler = CrawlerProcess(settings)

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
