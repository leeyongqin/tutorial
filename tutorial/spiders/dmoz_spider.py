import scrapy


class DmozSpider(scrapy.spiders.Spider):
    name = 'dmoz'
    allowed_domain = ["dmoz.org"]
    start_url = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)