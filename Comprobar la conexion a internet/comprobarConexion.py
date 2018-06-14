# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       comprobarConexion.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       13 de Junio 2018
# Modificado:   13 de Junio 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__version__ = "1.0"

"""
El módulo *comprobarConexion* permite comprobar la conexión a internet.
"""

# Versión Python: 3.5.2

from ctypes import windll, byref
from ctypes.wintypes import DWORD
from socket import gethostbyname, create_connection, error


# =================== FUNCIÓN comprobarConexion ====================

def comprobarConexion():
    flags = DWORD()
    conexion = windll.wininet.InternetGetConnectedState(byref(flags), None)

    if conexion:
        return "Hay conexión a internet..."
    else:
        return "No hay conexión a internet..."


# ================= FUNCIÓN comprobarConexionUno ===================

def comprobarConexionUno():
    try:
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()
        return "Hay conexión a internet..."
    except error:
        return "No hay conexión a internet..."


# ======================= LLAMAR FUNCIONES =========================

conexion = comprobarConexion()
conexionUno = comprobarConexionUno()

print(conexion)
print(conexionUno)
