from mis_funciones import agregar
from mis_funciones import comparar
from mis_funciones import prestar_o_reporte
from mis_funciones import pedir_datos
from mis_funciones import reporte

while True:
    resultado = prestar_o_reporte()
    if resultado is not None and resultado:
        autor, titulo, dia, fecha= pedir_datos()
        resultado_comparar = comparar('autores.csv', 'libros.csv', autor, titulo)
        if not resultado_comparar or resultado_comparar is None:
            print('Problema al comparar')
            continue
        agregar('prestamos.csv', [[autor, titulo, dia, fecha]])
    elif resultado is not None and not resultado:
        reporte()
    else:
        break
