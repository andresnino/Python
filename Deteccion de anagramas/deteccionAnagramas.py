# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       deteccionAnagramas.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       21 de Julio 2018
# Modificado:   21 de Julio 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__version__ = "1.0"

"""
El módulo *deteccionAnagramas* permite encontrar los anagramas de una palabra o frase.
"""

# Versión Python: 3.5.2


# ================== FUNCIÓN deteccionAnagramas ====================

def deteccionAnagramas(palabra, listaPalabras):
    palabra = sorted(palabra)
    anagramas = [cadena for cadena in listaPalabras if sorted(cadena) == palabra]

    return anagramas
    

# ======================== LLAMAR FUNCIÓN ==========================

palabra = "amor"
listaPalabras = ["roma", "mario", "mora", "andres", "ramo",
                 "nino", "omar", "youtube", "arom", "suscribete"]

anagramas = deteccionAnagramas(palabra, listaPalabras)
print("Anagramas de la palabra {}:".format(palabra), anagramas)
