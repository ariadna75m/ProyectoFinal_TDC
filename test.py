from mis_funciones import sobreescribir
from mis_funciones import leer
from mis_funciones import seleccionar_columna
from mis_funciones import filtrar
from mis_funciones import contar
from mis_funciones import posicion
from mis_funciones import comparar
from mis_funciones import generar_prestamos_auto

def test_crear_archivo():
    mis_lineas = [
        ['autor1'],
        ['autor2'],
        ['autor3']
    ]
    archivo_nombre = 'csv_test.csv'
    sobreescribir(archivo_nombre, mis_lineas)
    lectura = leer(archivo_nombre)
    assert mis_lineas == lectura

def test_seleccionar_columna():
    mis_lineas = [
        ['autorx', 'librox'],
        ['autory', 'libroy'],
        ['autorz', 'libroz'],
    ]
    resultado = seleccionar_columna(mis_lineas, 0)
    assert resultado == ['autorx', 'autory', 'autorz']

def test_filtrar():
    mis_lineas = [
        ['autorx', 'librox', 'lunes', '2020-10-10'],
        ['autorx', 'librox', 'martes', '2020-09-10'],
        ['autory', 'libroy', 'domingo', '2020-10-10'],
        ['autorz', 'libroz', 'jueves', '2020-01-11'],
    ]
    resultado = filtrar(mis_lineas, 'autorx', 0)
    assert resultado == [['autorx', 'librox', 'lunes', '2020-10-10'],
                         ['autorx', 'librox', 'martes', '2020-09-10']]

def  test_posicion():
    mis_lineas = [
        ['autorx'],
        ['autory'],
        ['autorz'],
        ['autorw'],
    ]
    resultado = posicion(mis_lineas, 'autory', 0)
    assert resultado == 1


def test_contar():
    mis_lineas = [
        ['autorx', 'librox', 'lunes', '2020-10-10'],
        ['autorx', 'librox', 'martes', '2020-09-10'],
        ['autory', 'libroy', 'miercoles', '2020-10-10'],
        ['autory', 'libroy', 'domingo', '2020-10-10'],
        ['autory', 'libroy', 'domingo', '2020-10-10'],
        ['autory', 'libroy', 'domingo', '2020-10-10'],
        ['autorz', 'libroz', 'jueves', '2020-01-11'],
        ['autory', 'libroy', 'domingo', '2020-10-10'],
    ]
    resultado = contar(mis_lineas, 2)
    assert resultado == {'domingo': 4, 'jueves': 1, 'lunes': 1, 'martes': 1, 'miercoles': 1}

def test_generar_prestamos_auto():
    generar_prestamos_auto()
