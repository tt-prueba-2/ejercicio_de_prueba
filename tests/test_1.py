import pytest
import re

def test_horario_clases(capsys):
    # Simulamos el programa del horario de clases
    print("Horario de clases:")
    print("Lunes:\t Matemáticas, Lengua")
    print("Martes:\t Historia, Ciencias")
    print("Miércoles:\t Geografía, Arte")
    print("Jueves:\t Educación Física, Inglés")
    print("Viernes:\t Computación, Música")

    # Capturamos la salida del programa
    captured = capsys.readouterr()

    # Verificamos que los días de la semana estén presentes y el formato sea correcto
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    
    # Patrón flexible para validar formato "Día: Materia1, Materia2"
    for dia in dias_semana:
        assert re.search(fr"{dia}:\s+\w+(,\s+\w+)*", captured.out), f"Falta el día {dia} o formato incorrecto."

def test_calculadora_ahorros(capsys):
    # Simulamos el programa de ahorros
    ahorro_julio = 500
    ahorro_agosto = 600
    ahorro_septiembre = 700
    total_ahorros = ahorro_julio + ahorro_agosto + ahorro_septiembre
    print(f"El total de ahorros en los últimos tres meses es de {total_ahorros}")
    
    # Capturamos la salida del programa
    captured = capsys.readouterr()

    # Usamos regex para capturar el total de ahorros
    match = re.search(r"El total de ahorros en los últimos tres meses es de (\d+)", captured.out)
    assert match is not None, "No se encontró la salida correcta."

    # Comparamos el valor calculado con el esperado
    total_calculado = int(match.group(1))
    assert total_calculado == total_ahorros

def test_promedio_edad(capsys):
    # Simulamos el programa del promedio de edad
    edad1 = 25
    edad2 = 30
    edad3 = 22
    edad4 = 28
    edad5 = 35
    promedio_edad = (edad1 + edad2 + edad3 + edad4 + edad5) / 5
    print(f"El promedio de edad es de {promedio_edad}")

    # Capturamos la salida del programa
    captured = capsys.readouterr()

    # Usamos regex para capturar el promedio
    match = re.search(r"El promedio de edad es de ([\d\.]+)", captured.out)
    assert match is not None, "No se encontró la salida correcta."

    # Comparamos el promedio calculado con el esperado
    promedio_calculado = float(match.group(1))
    assert promedio_calculado == promedio_edad
