import scrapy


# Subclass of scrapy.Spider
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_number = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page_number
        with open(filename, 'wb') as file:
            file.write(response.body)
        self.log('Saved file %s' % filename)
