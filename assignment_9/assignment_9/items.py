import scrapy

class CourseItem(scrapy.Item):
    emnekode = scrapy.Field()
    tittel = scrapy.Field()
    overskrifter = scrapy.Field()
    innhold = scrapy.Field()
    url = scrapy.Field()