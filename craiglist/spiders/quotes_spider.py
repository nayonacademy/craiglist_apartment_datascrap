import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://bangladesh.craigslist.org/search/apa',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]

        for row in response.css('ul.rows li'):
            title = row.css('p.result-info a::text').extract_first()
            time = row.css('p.result-info time::text').extract_first()
            price = row.css('p.result-info span.result-price::text').extract_first()
            address = row.css('p.result-info span.result-hood::text').extract_first()
            print dict(title=title, time=time, price=price, address=address)

            #alternative way
            # yield {
            #     'title': row.css('p.result-info a::text').extract_first(),
            #     'time': row.css('p.result-info time::text').extract_first(),
            #     'price': row.css('p.result-info span.result-price::text').extract_first(),
            #     'address': row.css('p.result-info span.result-hood::text').extract_first(),
            # }


        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(datastore)
        # self.log('Saved file %s' % filename)
