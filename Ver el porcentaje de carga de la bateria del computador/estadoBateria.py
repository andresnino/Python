# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       estadoBateria.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       18 de Mayo 2018
# Modificado:   18 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *estadoBateria* permite ver el porcentaje de carga de la batería y si
está recibiendo carga.
"""

from ctypes import Structure, wintypes, POINTER, windll, pointer, WinError


# ===================== FUNCIÓN cargaBateria =======================

def cargaBateria():
   class ESTADO_ENERGIA_SISTEMA(Structure):
       _fields_ = [
           ("ACLineStatus", wintypes.BYTE),
           ("BatteryFlag", wintypes.BYTE),
           ("BatteryLifePercent", wintypes.BYTE),
           ]

   ESTADO_ENERGIA_SISTEMA_P = POINTER(ESTADO_ENERGIA_SISTEMA)

   GetSystemPowerStatus = windll.kernel32.GetSystemPowerStatus
   GetSystemPowerStatus.argtypes = [ESTADO_ENERGIA_SISTEMA_P]
   GetSystemPowerStatus.restype = wintypes.BOOL

   estado = ESTADO_ENERGIA_SISTEMA()
   if not GetSystemPowerStatus(pointer(estado)):
      raise WinError()

   cargador, carga = estado.ACLineStatus, estado.BatteryLifePercent
   return (cargador, carga)

        
# ==================== FUNCIÓN estadoBateria =======================

def estadoBateria():
   cargadorCarga = cargaBateria()
   cargador = cargadorCarga[0]
   carga = cargadorCarga[1]
   
   if cargador == 0:
      print("La batería no esta recibiendo carga.")
      if carga <= 15:
         print("La carga de la batería está por debajo o igual al 15%.")
      else:
         print("Carga de la batería: {}%.".format(carga))
   elif cargador == 1:
      print("La batería esta recibiendo carga.")
      if carga >= 95:
         print("La carga de la batería está por encima o igual al 95%.")
      else:
         print("Carga de la batería: {}%.".format(carga))
   else:
      print("Este sistema solo funciona en ordenadores portatiles.")


# ======================== LLAMAR FUNCIÓN ==========================

estadoBateria()
