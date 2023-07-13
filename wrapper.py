# # scrapy runspider app.py
# import os
# import json
import scrapy
# from flask import Flask, jsonify
# from scrapy.crawler import CrawlerRunner
# from twisted.internet import reactor, defer

# app = Flask(__name__)

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://haveibeenpwned.com/']

    def parse(self, response):
        for item in response.xpath('/html/body/div[6]/div[1]'):
            count = {
                'pwned_websites': item.xpath('./div[1]/span/text()').get(),
                'pwned_accounts': item.xpath('./div[2]/span/text()').get(),
            }
            yield count


# @app.route('/hibp', methods=['GET'])
# def scrape():
#     @defer.inlineCallbacks
#     def crawl():
#         process = CrawlerRunner(settings={
#             'USER_AGENT': 'Mozilla/5.0',
#             'FEED_FORMAT': 'jsonlines',
#             'FEED_URI': 'output.json'
#         })
#         yield process.crawl(MySpider)
#         reactor.stop()

#     crawl()
    
#     with open('output.json', 'r') as f:
#         data = json.load(f)

#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)

