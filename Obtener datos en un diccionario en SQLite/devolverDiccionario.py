# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       devolverDiccionario.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       07 de Julio 2018
# Modificado:   07 de Julio 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__version__ = "1.0"

"""
El módulo *devolverDiccionario* permite realizar una consulta a una base de datos (SQLite)
y obtener los resultados en un diccionario.
"""

# Versión Python: 3.5.2

import sqlite3


# ===================== FUNCIÓN dict_factory =======================

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# ================= FUNCIÓN devolverDiccionario ====================

def devolverDiccionario():
    conexionMemoria = sqlite3.connect(":memory:") # Crear objeto de conexión
    conexionMemoria.row_factory = dict_factory # Forma avanzada de obtener resultados
    cursorMemoria = conexionMemoria.cursor() # Crear cursor

    # Crear tabla
    cursorMemoria.execute("CREATE TABLE PRUEBA (NOMBRE TEXT, APELLIDO TEXT)")

    datos_insertar = [("Andres", "Niño"),
                      ("Elon", "Musk"),
                      ("Donald", "Trum")]

    # Insertar multiples filas o datos
    cursorMemoria.executemany("INSERT INTO PRUEBA(NOMBRE, APELLIDO) VALUES (?, ?)",
                              datos_insertar)

    # Ejecutar una consulta
    cursorMemoria.execute("SELECT * FROM PRUEBA")

    # Obtener los resultados de la consulta en una lista
    resultadoConsulta = cursorMemoria.fetchall()

    # Cerrar base de datos
    conexionMemoria.close()

    return resultadoConsulta


# ======================== LLAMAR FUNCIÓN ==========================

funcion = devolverDiccionario()
print(funcion)
