import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_links = response.css(
            'a.pep.reference.internal::attr(href)'
        ).getall()
        for pep_link in all_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        text = response.css('h1.page-title::text').get()
        number, name = map(
            lambda x: x.encode('latin1').decode('unicode_escape'),
            text.split(' – ', 1)
        )
        data = {
            'number': number.split(' ')[1],
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
