# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Modelo = scrapy.Field()    
    Marca = scrapy.Field()
    Precio = scrapy.Field()
    TamañoPantalla = scrapy.Field()
    Resolucion = scrapy.Field()
    TipoDisplay = scrapy.Field()
    Calificacion = scrapy.Field()
    url = scrapy.Field()  
    activo = scrapy.Field()
    pass
