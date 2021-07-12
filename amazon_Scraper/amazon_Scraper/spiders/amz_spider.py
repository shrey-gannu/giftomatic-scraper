import scrapy
import pandas as pd
from ..items import AmazonScraperItem

newlist = []
data = pd.read_csv("C:/Users/shrey/Desktop/giftshop/giftdatabase.csv")



class AmzSpiderSpider(scrapy.Spider):
    name = 'amz_spider'
    start_urls = data['address'].tolist()

    def parse(self, response):
        
        items = AmazonScraperItem()
        product_url = response.request.url
        product_name = response.css("#productTitle::text")[0].extract()
        product_image = response.css("div.imgTagWrapper img::attr(src)").extract()
        product_rating = response.css("span.a-icon-alt::text").get()

        newlist ="".join([x.strip("'\n'") for x in product_name]) 
        items['product_url'] = product_url
        items['product_name'] = newlist
        items['product_image'] = product_image
        items['product_rating'] = product_rating
        print(response.headers)

        return items
