# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as link
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from OJCC.items import ProblemItem, SolutionItem, AccountItem
from base64 import b64decode
from datetime import datetime
import time
import re

LANGUAGE = {
    'g++': '0',
    'gcc': '1',
    'pascal': '2',
    'java': '3',
    'c++': '4',
    'c': '5'
}


class FzuInitSpider(CrawlSpider):
    name = 'fzu_init'
    allowed_domains = ['acm.fzu.edu.cn']

    start_urls = [
        'http://acm.fzu.edu.cn/list.php'
    ]

    rules = [
        Rule(
            link(
                allow=('list.php\?vol=[0-9]+'),
                unique=True
            )),
        Rule(
            link(
                allow=('problem.php\?pid=[0-9]+')
            ), callback='problem_item')
    ]

    def problem_item(self, response):
        html = response.body.\
            replace(' <= ', ' &le; ').\
            replace(' < ', ' &lt; ').\
            replace(' > ', ' &gt; ').\
            replace(' >= ', ' &ge; ').\
            replace(' << ', ' &lt;&lt; ').\
            replace(' >> ', ' &gt;&gt; ')

        sel = Selector(text=html)

        item = ProblemItem()
        item['origin_oj'] = 'fzu'
        item['problem_id'] = response.url[-4:]
        item['problem_url'] = response.url
        item['title'] = sel.xpath(
            '//div[contains(@class,\
            "problem_title")]/b/text()').extract()[0][14:].rstrip()
        item['description'] = \
            sel.css('.pro_desc').extract()[0][22:-6].\
            replace('<div class="data">', '<pre>').\
            replace('</div>', '</pre>')

        try:
            item['input'] = sel.css('.pro_desc').extract()[1]
        except:
            item['input'] = []
        try:
            item['output'] = sel.css('.pro_desc').extract()[2]
        except:
            item['output'] = []
        item['time_limit'] = sel.css('.problem_desc').re('T[\S*\s]*c')[0][12:]
        item['memory_limit'] = sel.css('.problem_desc').\
            re('M[\S*\s]*B')[0][15:]
        item['accept'] = sel.css('.problem_desc').re('Accept:*\s[0-9]+')[0][8:]
        item['submit'] = sel.css('.problem_desc').re('Submit:*\s[0-9]+')[0][8:]
        item['sample_input'] = \
            sel.css('.data').extract()[-2].\
            replace('<div class="data">', '<pre>').\
            replace('</div>', '</pre>')
        item['sample_output'] = \
            sel.css('.data').extract()[-1].\
            replace('<div class="data">', '<pre>').\
            replace('</div>', '</pre>')
        item['update_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return item


class FzuProblemSpider(Spider):
    name = 'fzu_problem'
    allowed_domains = ['acm.fzu.edu.cn']

    def __init__(self, problem_id='1000', *args, **kwargs):
        self.problem_id = problem_id
        super(FzuProblemSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://acm.fzu.edu.cn/problem.php?pid=%s' % problem_id
        ]

    def parse(self, response):
        html = response.body.\
            replace(' <= ', ' &le; ').\
            replace(' < ', ' &lt; ').\
            replace(' > ', ' &gt; ').\
            replace(' >= ', ' &ge; ').\
            replace(' << ', ' &lt;&lt; ').\
            replace(' >> ', ' &gt;&gt; ')

        sel = Selector(text=html)

        item = ProblemItem()
        item['origin_oj'] = 'fzu'
        item['problem_id'] = self.problem_id
        item['problem_url'] = response.url
        item['title'] = sel.xpath(
            '//div[contains(@class,\
            "problem_title")]/b/text()').extract()[0][14:].rstrip()
        item['description'] = \
            sel.css('.pro_desc').extract()[0][22:-6].\
            replace('<div class="data">', '<pre>').\
            replace('</div>', '</pre>')

        try:
            item['input'] = sel.css('.pro_desc').extract()[1]
        except:
            item['input'] = []
        try:
            item['output'] = sel.css('.pro_desc').extract()[2]
        except:
            item['output'] = []
        item['time_limit'] = sel.css('.problem_desc').re('T[\S*\s]*c')[0][12:]
        item['memory_limit'] = sel.css('.problem_desc').\
            re('M[\S*\s]*B')[0][15:]
        item['accept'] = sel.css('.problem_desc').re('Accept:*\s[0-9]+')[0][8:]
        item['submit'] = sel.css('.problem_desc').re('Submit:*\s[0-9]+')[0][8:]
        item['sample_input'] = \
            sel.css('.data').extract()[-2].\
            replace('<div class="data">', '<pre>').\
            replace('</div>', '</pre>')
        item['sample_output'] = \
            sel.css('.data').extract()[-1].\
            replace('<div class="data">', '<pre>').\
            replace('</div>', '</pre>')
        item['update_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return item


class FzuSubmitSpider(CrawlSpider):
    name = 'fzu_submit'
    allowed_domains = ['acm.fzu.edu.cn']
    login_url = 'http://acm.fzu.edu.cn/login.php?act=1&dir='
    submit_url = 'http://acm.fzu.edu.cn/submit.php?act=5'
    login_verify_url = 'http://acm.fzu.edu.cn/mail.php'
    source = \
        'I2luY2x1ZGUgPHN0ZGlvLmg+CgppbnQgbWFpbigpCnsKICAg\
        IGludCBhLGI7CiAgICBzY2FuZigiJWQgJWQiLCZhLCAmYik7C\
        iAgICBwcmludGYoIiVkXG4iLGErYik7CiAgICByZXR1cm4gMDsKfQ=='

    start_urls = [
            "http://acm.fzu.edu.cn/log.php"
    ]

    download_delay = 0.5
    is_login = False

    rules = [
        Rule(
            link(
                allow=('log.php\?&page=[0-9]+'),
                deny=('log.php\?&page=1$')
            ), follow=True, callback='parse_start_url')
    ]

    def __init__(
            self,
            solution_id=1,
            problem_id='1000',
            language='g++',
            source=None,
            username='sdutacm1',
            password='sdutacm', *args, **kwargs):
        super(FzuSubmitSpider, self).__init__(*args, **kwargs)

        self.solution_id = solution_id
        self.problem_id = problem_id
        self.language = language
        self.username = username
        self.password = password
        if source is not None:
            self.source = source

    def start_requests(self):
        return [FormRequest(self.login_url,
                formdata={
                        'uname': self.username,
                        'upassword': self.password,
                        'submit': 'Submit',
                },
                callback=self.after_login,
                dont_filter=True
        )]

    def after_login(self, response):
        return [Request(
            self.login_verify_url,
            callback=self.login_verify
        )]

    def login_verify(self, response):
        if re.search('Write New Mail', response.body):
            self.is_login = True

            self.login_time = time.mktime(
                time.strptime(
                    response.headers['Date'],
                    '%a, %d %b %Y %H:%M:%S %Z')
            ) + (8 * 60 * 60)
            time.sleep(1)
            return [FormRequest(self.submit_url,
                    formdata={
                            'pid': self.problem_id,
                            'lang': LANGUAGE.get(self.language, '0'),
                            'code': b64decode(self.source),
                            'submit': 'Submit',
                    },
                    callback=self.after_submit,
                    dont_filter=True
            )]
        else:
            return Request(self.start_urls[0], callback=self.parse_start_url)

    def after_submit(self, response):
        time.sleep(10)
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse_start_url(self, response):

        sel = Selector(response)

        item = SolutionItem()
        item['solution_id'] = self.solution_id
        item['origin_oj'] = 'fzu'
        item['problem_id'] = self.problem_id
        item['language'] = self.language

        if self.is_login:
            for tr in sel.xpath('//table/tr')[1:]:
                user = tr.xpath('.//td/a/text()').extract()[-1]
                _submit_time = tr.xpath('.//td/text()').extract()[1]
                submit_time = time.mktime(
                        time.strptime(_submit_time, '%Y-%m-%d %H:%M:%S'))
                if submit_time > self.login_time and \
                        user == self.username:
                    item['submit_time'] = _submit_time
                    item['run_id'] = tr.xpath('.//td/text()').extract()[0]

                    try:
                        item['memory'] = \
                            tr.xpath('.//td')[5].xpath('./text()').extract()[0]
                        item['time'] = \
                            tr.xpath('.//td')[6].xpath('./text()').extract()[0]
                    except:
                        pass

                    item['code_length'] = tr.xpath('.//td/text()').\
                        extract()[-1]
                    try:
                        item['result'] = tr.xpath('.//td/font/text()').\
                            extract()[0]
                    except:
                        item['result'] = tr.xpath('.//td/font/a/text()').\
                            extract()[0]
                    self._rules = []
                    return item
        else:
            item['result'] = 'Submit Error'
            self._rules = []
            return item


class FzuAccountSpider(CrawlSpider):
    name = 'fzu_user'
    allowed_domains = ['acm.fzu.edu.cn']
    login_url = 'http://acm.fzu.edu.cn/login.php?act=1&dir='
    login_verify_url = 'http://acm.fzu.edu.cn/mail.php'
    accepted_url = \
        'http://acm.fzu.edu.cn/log.php?pid=&user=%s\
        &language=99&state=1&submit=Go'

    is_login = False
    solved = {}

    def __init__(
            self,
            username='sdutacm1',
            password='sdutacm', *args, **kwargs):
        super(FzuAccountSpider, self).__init__(*args, **kwargs)

        self.username = username
        self.password = password

        self.start_urls = [
                "http://acm.fzu.edu.cn/user.php?uname=%s" % username
        ]

    def start_requests(self):
        return [FormRequest(self.login_url,
                formdata={
                        'uname': self.username,
                        'upassword': self.password,
                        'submit': 'Submit',
                },
                callback=self.after_login,
                dont_filter=True
        )]

    def after_login(self, response):
        return [Request(
            self.login_verify_url,
            callback=self.login_verify
        )]

    def login_verify(self, response):
        if re.search('Write New Mail', response.body):
            self.is_login = True
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        sel = Selector(response)

        self.item = AccountItem()
        self.item['origin_oj'] = 'fzu'
        self.item['username'] = self.username
        if self.is_login:
            try:
                self.item['rank'] = sel.xpath('//table')[2].\
                    xpath('./tr')[0].xpath('./td/text()')[1].extract()
                self.item['accept'] = sel.xpath('//table')[2].\
                    xpath('./tr')[2].xpath('./td/text()')[1].extract()
                self.item['submit'] = sel.xpath('//table')[2].\
                    xpath('./tr')[1].xpath('./td/text()')[1].extract()
                yield Request(
                    self.accepted_url % self.username,
                    callback=self.accepted
                )
                self.item['status'] = 'Authentication Success'
            except:
                self.item['status'] = 'Unknown Error'
        else:
            self.item['status'] = 'Authentication Failed'

        yield self.item

    def accepted(self, response):

        sel = Selector(response)

        next_url = sel.xpath('//b/a/@href')[-2].extract()
        table_tr = sel.xpath('//table/tr')[1:]
        for tr in table_tr:
            name = tr.xpath('.//td/a/text()').extract()[-1]  # noqa
            problem_id = tr.xpath('.//td[4]/a/text()').extract()[0]
            submit_time = tr.xpath('.//td/text()').extract()[1]

            self.solved[problem_id] = submit_time
            self.item['solved'] = self.solved

        if sel.xpath('//b/a/text()')[-2].extract() == 'Next':
            yield Request(
                'http://' + self.allowed_domains[0] + '/' + next_url,
                callback=self.accepted
            )

        yield self.item
