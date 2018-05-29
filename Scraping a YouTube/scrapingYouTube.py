# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       scrapingYouTube.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       28 de Mayo 2018
# Modificado:   28 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *scrapingYouTube* permite extraer datos de YouTube como son el nombre del canal y la
cantidad de suscriptores, y también de los primeros 30 vídeos (Más populares - más antiguos -
más recientes) el link o url, título, duración, vistas y hace cuanto se publicó el vídeo y
por último guardar todos esos datos en un archivo de texto(txt).
"""

from scrapy import Item, Field, Spider
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess


# ===================== CLASE YoutubeVideo =========================

class YoutubeVideo(Item):
    nombre_canal = Field()
    suscriptores = Field()
    
    link = Field()
    titulo = Field()
    duracion_video = Field()
    vistas = Field()
    tiempo_publicacion = Field()


# ===================== CLASE scrapyYoutube ========================

class scrapyYoutube(Spider):
    name = "scrapy-youtube"
    
    urls = {1: "https://www.youtube.com/c/AndresNi%C3%B1oPython/videos?sort=p&view=0&flow=grid",
            2: "https://www.youtube.com/c/AndresNi%C3%B1oPython/videos?flow=grid&view=0&sort=da",
            3: "https://www.youtube.com/c/AndresNi%C3%B1oPython/videos?flow=grid&view=0&sort=dd"}
    
    print("================ Scraping a YouTube ================\n\n"
          "1: Scraping a los primeros 30 videos más populares\n"
          "2: Scraping a los primeros 30 videos más antiguos\n"
          "3: Scraping a los primeros 30 videos más recientes\n")
    opcion = int(input("Ingrese una opción: "))

    start_urls = [urls[opcion]]
    
    def parse(self, response):
        # Obtener el nombre del canal y la cantidad de suscriptores
        selector = response.css("div#c4-primary-header-contents > div")
        datosCanal = ItemLoader(YoutubeVideo(), selector=selector)
        datosCanal.add_xpath("nombre_canal", "//*[@id='c4-primary-header-contents']/div[1"
                           "]/div/div[1]/h1/span/span/span/a/text()")
        datosCanal.add_xpath("suscriptores", "//*[@id='c4-primary-header-contents']/div[1"
                           "]/div/div[2]/div/span/span[1]/text()")

        datosCanal = datosCanal.load_item()

        # Obtener los datos de los videos       
        def datosVideos():
            indice = 1
            for sel in response.css("ul#channels-browse-content-grid > li"):
                loader = ItemLoader(YoutubeVideo(), selector=sel)
                loader.add_xpath("link", ".//h3/a/@href")
                loader.add_xpath("titulo", ".//h3/a/text()")
                loader.add_xpath("duracion_video", "//*[@id='channels-browse-content-grid']"
                                 "/li[{}]/div/div[1]/div[1]/span/span[1]/span/text()"
                                 .format(indice))
                loader.add_xpath("vistas", ".//ul/li[1]/text()")
                loader.add_xpath("tiempo_publicacion", ".//ul/li[2]/text()")
                indice += 1
                
                yield loader.load_item()

        # Escribir los datos obtenidos en un archivo de texto(txt)               
        with open("youtube_informe.txt", "w") as archivo:
            tituloDescripcion = {1: "PRIMEROS 30 VIDEOS MÁS POPULARES",
                                 2: "PRIMEROS 30 VIDEOS MÁS ANTIGUOS",
                                 3: "PRIMEROS 30 VIDEOS MÁS RECIENTES"}
            
            archivo.write("DATOS GENERALES DEL CANAL\n\n{}\n\n\nDESCRIPCIÓN DE LOS "
                          "{}\n\n".format(datosCanal, tituloDescripcion[self.opcion]))

            datosVideos = datosVideos()
            for datos in datosVideos:
                archivo.write("{}\n\n".format(datos))


proceso = CrawlerProcess()

proceso.crawl(scrapyYoutube)
proceso.start() # El script se bloqueará aquí hasta que se complete el rastreo
