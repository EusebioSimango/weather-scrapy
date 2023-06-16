from scrapy import Spider

class AccuWeatherSpider(Spider):
    name = 'accuWeather'
    allowed_domains = ['https://www.accuweather.com/']
    start_urls = [
        'https://www.accuweather.com/en/mz/matola/244230/weather-forecast/244230'
    ]

    def parse(self, response):
      weather = response.xpath('//div[@class="page-content content-module"]/a//div[@class="temp"]/text()').get()
      self.logger.info('Scraped value: %s', weather)
      print('Scraped value: ', weather)
        