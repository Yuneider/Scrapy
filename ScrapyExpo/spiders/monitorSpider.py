import scrapy

class MonitorSpider(scrapy.Spider):
    name = "Monitor"
    start_urls = ['https://www.amazon.com/s?k=monitor+1440p+144hz&sprefix=monitor+1440p%2Caps%2C157&ref=nb_sb_ss_ts-doa-p_2_13']


    def parse(self, response):
        for products in response.css('div.sg-col.sg-col-4-of-12.sg-col-8-of-16.sg-col-12-of-20.s-list-col-right'):
            yield {
                'name': products.css('span.a-size-medium.a-color-base.a-text-normal::text').get(),
                'price': products.css('span.a-price-whole::text').get()
            }
        next_page = response.css('span.s-pagination-strip>a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)