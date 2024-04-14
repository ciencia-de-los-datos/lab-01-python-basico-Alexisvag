
"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv

def lectura_de_documento(archivo_csv="data.csv"):
    """
    Lee un archivo CSV y devuelve una lista de listas con sus contenidos.
    """
    with open(archivo_csv, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        return [row for row in reader]

def pregunta_01():
    """
    Retorna la suma de la segunda columna.
    """
    datos = lectura_de_documento()
    return sum(int(row[1]) for row in datos)

def pregunta_02():
    """
    Retorna la cantidad de registros por cada letra de la primera columna.
    """
    datos = lectura_de_documento()
    counts = {}
    for row in datos:
        letter = row[0]
        counts[letter] = counts.get(letter, 0) + 1
    return sorted(counts.items())

def pregunta_03():
    """
    Retorna la suma de la columna 2 por cada letra de la primera columna.
    """
    datos = lectura_de_documento()
    sums = {}
    for row in datos:
        letter = row[0]
        value = int(row[1])
        sums[letter] = sums.get(letter, 0) + value
    return sorted(sums.items())

def pregunta_04():
    """
    Retorna la cantidad de registros por cada mes en la columna 3.
    """
    datos = lectura_de_documento()
    counts = {}
    for row in datos:
        month = row[2].split("-")[1]
        counts[month] = counts.get(month, 0) + 1
    return sorted(counts.items())

def pregunta_05():
    """
    Retorna el valor máximo y mínimo de la columna 2 por cada letra de la columna 1.
    """
    datos = lectura_de_documento()
    values = {}
    for row in datos:
        letter = row[0]
        number = int(row[1])
        if letter not in values:
            values[letter] = [number, number]
        else:
            values[letter][0] = max(values[letter][0], number)
            values[letter][1] = min(values[letter][1], number)
    return sorted([(key, *value) for key, value in values.items()])

def pregunta_06():
    """
    Retorna el valor mínimo y máximo de las claves en la columna 5.
    """
    datos = lectura_de_documento()
    min_max = {}
    for row in datos:
        items = row[4].split(",")
        for item in items:
            key, value = item.split(":")
            value = int(value)
            if key not in min_max:
                min_max[key] = [value, value]
            else:
                min_max[key][0] = min(min_max[key][0], value)
                min_max[key][1] = max(min_max[key][1], value)
    return sorted([(key, *value) for key, value in min_max.items()])

def pregunta_07():
    """
    Retorna una lista de tuplas asociando la columna 2 con la columna 1.
    """
    datos = lectura_de_documento()
    associations = {}
    for row in datos:
        key = int(row[1])
        value = row[0]
        if key not in associations:
            associations[key] = []
        associations[key].append(value)
    return sorted([(key, sorted(value)) for key, value in associations.items()])

def pregunta_08():
    """
    Retorna una lista de tuplas asociando la columna 2 con las letras de la columna 1.
    """
    datos = lectura_de_documento()
    associations = {}
    for row in datos:
        key = int(row[1])
        value = row[0]
        if key not in associations:
            associations[key] = set()
        associations[key].add(value)
    return sorted([(key, sorted(list(value))) for key, value in associations.items()])

def pregunta_09():
    """
    Retorna un diccionario con la cantidad de registros por cada clave en la columna 5.
    """
    datos = lectura_de_documento()
    counts = {}
    for row in datos:
        items = row[4].split(",")
        for item in items:
            key = item.split(":")[0]
            counts[key] = counts.get(key, 0) + 1
    return counts

def pregunta_10():
    """
    Retorna una lista de tuplas con la letra de la columna 1 y la cantidad de elementos de las columnas 4 y 5.
    """
    datos = lectura_de_documento()
    result = []
    for row in datos:
        letter = row[0]
        col4_count = len(row[3].split(","))
        col5_count = len(row[4].split(","))
        result.append((letter, col4_count, col5_count))
    return result

def pregunta_11():
    """
    Retorna un diccionario con la suma de la columna 2 por cada letra de la columna 4.
    """
    datos = lectura_de_documento()
    sums = {}
    for row in datos:
        letters = row[3].split(",")
        value = int(row[1])
        for letter in letters:
            sums[letter] = sums.get(letter, 0) + value
    return sums

def pregunta_12():
    """
    Retorna un diccionario con la suma de los valores de la columna 5 por cada letra de la columna 1.
    """
    datos = lectura_de_documento()
    sums = {}
    for row in datos:
        letter = row[0]
        items = row[4].split(",")
        for item in items:
            value = int(item.split(":")[1])
            sums[letter] = sums.get(letter, 0) + value
    return sums
