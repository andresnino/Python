# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       operacionesFechas.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       08 de Agosto 2018
# Modificado:   08 de Agosto 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

# Versión Python: 3.5.2

"""
El módulo *operacionesFechas* permite realizar operaciones con fechas.
"""

from arrow import utcnow, get
         

# =================== FUNCIÓN operacionesFechas ====================

def operacionesFechas():
    """
       Tokens
       
       Use los siguientes tokens en el análisis y el formateo. Tenga en cuenta
       que no son lo mismo que los tokens para strptime (3):

                         Token   Salida
       Año               YYYY    2000, 2001, 2002 ... 2018, 2019
                         YY      00, 01, 02 ... 18, 19

       Mes               MMMM    Enero, Febrero, Marzo ... Noviembre, Diciembre
                         MMM     Ene, Feb, Mar ... Nov, Dic
                         MM      01, 02, 03 ... 11, 12
                         M       1, 2, 3 ... 11, 12

       Día del año       DDDD    001, 002, 003 ... 364, 365
                         DDD     1, 2, 3 ... 4, 5

       Dia del mes       DD      01, 02, 03 ... 30, 31
                         D       1, 2, 3 ... 30, 31

       Día de la semana  dddd   Lunes, Martes, Miércoles ... Sábado, Domingo
                         ddd    Lun, Mar, Mie ... Sab, Dom
                         d      1, 2, 3 ... 6, 7

       Idiomas

       Ingles:  'en', 'en_us', 'en_gb', 'en_au', 'en_be', 'en_jp', 'en_za', 'en_ca'
       Español: 'es', 'es_es'

       """

    # Obtener fecha del Sistema Operativo
    utc = utcnow().to("local")
    
    anio = utc.format("YYYY, YY")
    mes = utc.format("MMMM, MMM, MM, M", locale="es")
    diaAnio = utc.format("DDDD, DDD")
    diaMes = utc.format("DD, D")
    diaSemana = utc.format("dddd, ddd, d", locale="es")

    diaMesAnio = utc.format("DD/MM/YYYY")
    anioMesDia = utc.format("YYYY-MM-DD")
    
    print("Año token(YYYY, YY):", anio)
    print("Mes token(MMMM, MMM, MM, M):", mes)
    print("Día del año token(DDDD, DDD):", diaAnio)
    print("Dia del mes token(DD, D):", diaMes)
    print("Día de la semana token(dddd, ddd, d):", diaSemana)

    print()

    print("Formato Día/Mes/Año:", diaMesAnio)
    print("Formato Año-Mes-Día:", anioMesDia)

    print()

  # ================================================================

    cadenaAnalizar = "2018-08-08"

    analizar = get(cadenaAnalizar, ["DD/MM/YYYY", "YYYY-MM-DD", "DD-MMMM-YYYY"])
    print("Analizar cadena:", analizar.format("DD/MM/YYYY"))
    print("Fecha tipo datetime.date:", type(analizar.date()), analizar.date())
    print()

  # ================================================================

    fechaUno = "2018-06-06"
    fechaDos = "2019-06-06"

    print("Fecha de referencia Uno:", fechaUno)
    print("Fecha de referencia Dos:", fechaDos)
    print()

    restarFechas = get(fechaDos, "YYYY-MM-DD") - get(fechaUno, "YYYY-MM-DD")
    print("Restar fechas:", restarFechas.days)
    print()

  # ================================================================

    # shift
    modificarDias = get(fechaUno, "YYYY-MM-DD").shift(days=2)
    modificarSemanas = get(fechaUno, "YYYY-MM-DD").shift(weeks=1)
    modificarMeses = get(fechaUno, "YYYY-MM-DD").shift(months=2)
    modificarAnios = get(fechaUno, "YYYY-MM-DD").shift(years=1)
    
    print("Modificar días:", modificarDias.format("YYYY-MM-DD"),
          modificarDias.format("YYYY-MMMM-dddd", locale="es"))
    print("Modificar semanas:", modificarSemanas.format("YYYY-MM-DD"))
    print("Modificar meses:", modificarMeses.format("YYYY-MM-DD"))
    print("Modificar años:", modificarAnios.format("YYYY-MM-DD"))
    print()

  # ================================================================

    # replace
    reemplazarDia = get(fechaUno, "YYYY-MM-DD").replace(day=7)
    reemplazarMes = get(fechaUno, "YYYY-MM-DD").replace(month=7)
    reemplazarAnio = get(fechaUno, "YYYY-MM-DD").replace(year=2019)
    
    print("Reemplazar día:", reemplazarDia.format("YYYY-MM-DD"))
    print("Reemplazar mes:", reemplazarMes.format("YYYY-MM-DD"))
    print("Reemplazar año:", reemplazarAnio.format("YYYY-MM-DD"))
    print()


# ===================== FUNCIÓN ejemploFechas ======================

def ejemploFechas():
    """Iterar sobre un conjunto de datos (Usuario, fecha de nacimiento) y guadar en
       dos listas los usuarios que nacieron antes y después de 1990-06-07."""

    datos = [("Andres Niño", "06/06/1990"),
             ("Donald Trump", "1991-06-05"),
             ("Elon Musk", "05/06/1990"),
             ("Alberto Canosa", "1992-06-05"),
             ("Richard Branson", "1993/02/10"),
             ("Guido van Rossum", "1990 04 20"),
             ]

    fechaComparar = "1990-06-07"

    antes, despues = [], []
    for dato in datos:
        fechaNacimiento = get(dato[1], ["YYYY-MM-DD", "DD/MM/YYYY", "YYYY/MM/DD", "YYYY MM DD"])
        fecha = get(fechaComparar, "YYYY-MM-DD")

        fechaNacimientoFormato = fechaNacimiento.format("YYYY-MM-DD")
        
        if fechaNacimiento < fecha:
            antes.append((dato[0], fechaNacimientoFormato))
        else:
            despues.append((dato[0], fechaNacimientoFormato))

    print("Usuarios que nacieron antes de 1990-06-07:", antes)
    print()
    print("Usuarios que nacieron después de 1990-06-07:", despues)


# ======================= LLAMAR FUNCIONES =========================

operacionesFechas()
ejemploFechas()
