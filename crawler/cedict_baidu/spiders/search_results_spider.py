import json
from collections import defaultdict
from urllib.parse import parse_qs, urlencode, urlparse

import scrapy
from redis import Redis
from scrapy.http.request import Request

query_file = '/Users/nathanglenn/workspaces/python_workspace/cedict.txt'
baidu_url = "http://www.baidu.com/s?ie=utf-8&"

# handles retries as outlined here: https://stackoverflow.com/questions/22795416/how-to-handle-302-redirect-in-scrapy

def _get_cedict_queries():
    with open(query_file) as f:
        return f.read().splitlines()

def _get_finished_queries():
    r = Redis()
    all_raw_entries = r.lrange('cedict_baidu', 0 ,-1)
    queries = set()
    for re in all_raw_entries:
        e = json.loads(re.decode('utf-8').replace("'",'"'))
        queries.add(e["query"])
    return queries

def _get_start_urls():
    all_queries = _get_cedict_queries()
    finished_queries = _get_finished_queries()
    queries = filter(lambda q: q not in finished_queries, all_queries)
    # print(len(list(queries)))
    # exit()

    start_urls = [baidu_url + urlencode({'wd': word}) for word in queries]
    print(f"Created {len(start_urls)} URLs from {query_file}; example formatted URL: {start_urls[0]}")
    return start_urls

class SearchResultsSpider(scrapy.Spider):
    name = 'cedict_counts'
    allowed_domains = ['baidu']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.retries = defaultdict(int)
        self.max_retries = 2

    def start_requests(self):
        counter = 0
        for url in _get_start_urls():
            # try resetting cookies every 20 requests to shake the captcha
            counter += 1
            if counter % 20 == 0:
                yield Request(url, callback=self.parse, meta={'dont_merge_cookies': True})
            else:
                yield Request(
                url,
                callback=self.parse,
                # meta={
                #     'handle_httpstatus_list': [302],
                # },
                # meta={'dont_redirect': True}
            )

    def parse(self, response):
        if response.status == 302:
            response.request.url
            print(f"Sent to captcha for '{response.request.url}' :(((")
            # retries = self.retries[response.url]
            # if retries < self.max_retries:
            #     self.retries[response.url] += 1
            #     yield response.request.replace(dont_filter=True)
            # else:
            #     self.logger.error('%s still returns 302 responses after %s retries',
            #                       response.url, retries)
            return
        try:
            count = response.css(".nums_text::text").get()
            if '个' not in count:
                count = 'failed!'
            else:
                count = count.removeprefix('百度为您找到相关结果约')
                count = count.removesuffix('个')
                count = count.replace(',', '')
                print(f'Count!!!: {count}')
        except:
            count = 'failed!'

        yield {
            'query': parse_qs(urlparse(response.url).query)['wd'][0],
            'result_count': count
        }
