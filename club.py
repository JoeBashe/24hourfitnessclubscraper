# -*- coding: utf-8 -*-
import re
import scrapy
from twentyfourhourfitnessclub.twentyfourhourfitnessclub.items import TwentyfourhourfitnessclubItem


class ClubSpider(scrapy.Spider):
    name = 'club'
    base_url = 'https://www.24hourfitness.com'
    # allowed_domains = ['www.24hourfitness.com/Website/clubList']
    start_urls = ['https://www.24hourfitness.com/Website/clubList/']

    def parse(self, response):
        for state in response.css('.card-content.state-card > a'):
            url = '{}{}'.format(self.base_url, state.attrib['href'])
            yield scrapy.Request(url, self.parse_state)

    def parse_city(self, response):
        for gym in response.css('.club-card .link-button-24 > a'):
            url = '{}{}'.format(self.base_url, gym.attrib['href'])
            yield scrapy.Request(url, self.parse_gym)

    def parse_gym(self, response):
        store_name = response.css('#overview_amenities::text').get()
        address1 = response.css('.address-container .club-info > a > span:first-child::text').get()
        address2 = response.css('.address-container .club-info > a > span:nth-child(2)::text').get()
        address3 = response.css('.address-container .club-info > a > span:nth-child(3)::text').get()
        phone_number = response.css('.phone-container-label .club-info > span::text').get()
        # store_hours = response.css('#club-hours-details')
        item = TwentyfourhourfitnessclubItem(
            store_name=store_name,
            address1=address1,
            address2=address2,
            address3=address3,
            phone_number=phone_number
        )
        yield item

    def parse_state(self, response):
        for city in response.css('.card-city > a'):
            url = '{}{}'.format(self.base_url, city.attrib['href'])
            yield scrapy.Request(url, self.parse_city)
