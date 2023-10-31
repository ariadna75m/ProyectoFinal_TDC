import csv
import random
import pandas as pd

# Constantes
ARCHIVO_AUTORES = 'autores.csv'
ARCHIVO_TITULOS = 'libros.csv'
ARCHIVO_PRESTAMOS = 'prestamos.csv'
DIAS = ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']

def leer(nombre):
    with open(nombre, mode='r') as File:
        lector = csv.reader(File)
        return list(lector)

def sobreescribir(nombre, mis_lineas):
    with open(nombre, mode='w', newline='') as File:
        escritor = csv.writer(File)
        escritor.writerows(mis_lineas)

def sobreescribir_linea_a_linea(nombre, mis_lineas):
    with open(nombre, mode='w', newline='') as File:
        escritor = csv.writer(File)
        for line in mis_lineas:
            escritor.writerow(line)

def agregar(nombre, mis_lineas):
    with open(nombre, mode='a', newline='') as File:
        escritor = csv.writer(File)
        escritor.writerows(mis_lineas)

def seleccionar_columna(lista, indice):
    return [i[indice] for i in lista]

def posicion(lista, valor, posicion):
    return seleccionar_columna(lista, posicion).index(valor)

def filtrar(lista, valor, indice):
    return [i for i in lista if i[indice] == valor]

def contar(lista, indice):
    columna = seleccionar_columna(lista, indice)
    unicos = set(columna)
    return {i : columna.count(i) for i in sorted(unicos)}

def pedir_datos():
    autor = input('Favor ingresar autor:')
    titulo = input('Favor ingresar titulo:')
    dia = input('Favor ingresar dia:')
    fecha = input('Favor ingresar fecha:')
    return autor, titulo, dia, fecha

def comparar(archivo_autores, archivo_titulos, autor, titulo):
    autores = leer(archivo_autores)
    autores = seleccionar_columna(autores,0)
    if not autor in autores:
        return
    titulos = leer(archivo_titulos)
    titulos = seleccionar_columna(titulos, 0)
    if not titulo in titulos:
        return
    index_autor = {k for k, v in enumerate(autores) if v == autor}
    index_titulo = {k for k, v in enumerate(titulos) if v == titulo}
    return len(index_titulo & index_autor) > 0

def prestar_o_reporte():
    dato = input('Bienvenido. Escriba Prestar o Reporte o cualquier cosa para salir:')
    if dato.lower().startswith('p'):
        return True
    elif dato.lower().startswith('r'):
        return False
    else:
        return
