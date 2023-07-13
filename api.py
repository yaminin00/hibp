from flask import Flask, jsonify
import logging
import scrapydo
import scrapy

app = Flask(__name__)

scrapydo.setup()

logging.basicConfig(filename='app.log', level=logging.DEBUG)

class PwnedSpider(scrapy.Spider):
    name = 'pwnedspider'
    start_urls = ['https://haveibeenpwned.com/']

    def parse(self, response):
        try:
            for item in response.xpath('/html/body/div[6]/div[1]'):
                count = {
                    'pwned_websites': item.xpath('./div[1]/span/text()').get(),
                    'pwned_accounts': item.xpath('./div[2]/span/text()').get(),
                }
                yield count
        except Exception as e:
            logging.error(str(e))
            yield {'error': 'An error occurred while parsing the response.'}

@app.route('/hibp', methods=['GET'])
def crawl():
    try:
        results = scrapydo.run_spider(PwnedSpider)
        return jsonify(results[0])
    except Exception as e:
        logging.error(str(e))
        return jsonify({'error': 'An error occurred while crawling the website.'})


if __name__ == '__main__':
    app.run(debug=True)