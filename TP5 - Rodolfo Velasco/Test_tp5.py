#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

import pytest
from tp5_funciones import *

#Prueba 1

@pytest.mark.parametrize("a, res", [
    (5, False),
    (7, True),
    (-7, False),
])
def test_id_checker(a, res):
    assert id_checker(a) == res

#Prueba 2

@pytest.mark.parametrize("a, res", [
    ("Hola a todos", "5"),
    ("Soy alto", "4"),
    ("Me despido", "7"),

])
def test_last_word(a, res):
    assert last_word(a) == res

#Prueba 3

@pytest.mark.parametrize("a, b, res", [
    (["Juan", "Lopez"], "40628371", "Juan5406"),
    (["Maria", "Ines", "Rosales"], "25469648", "Maria7254"),
    (["Roberto", "Sanchez"], "35371654", "Roberto7353"),
])
def test_name_id(a, b, res):
    assert name_id(a, b) == res

#Prueba 4

@pytest.mark.parametrize("a, b, res", [
    (40, 20, True),
    (21, 3, True),
    (15, 2, False),
])
def test_multiple(a, b, res):
    assert multiple(a, b) == res

#Prueba 5

@pytest.mark.parametrize("a, b, res", [
    (20, 10, 15),
    (50, 30, 40),
    (25, 15, 20),
])
def test_temperatura_media(a, b, res):
    assert temperatura_media(a, b) == res

#Prueba 6

@pytest.mark.parametrize("a, res", [
    ("Hola, tú", "H o l a , t ú"),
    ("Soy alto", "S o y a l t o"),
    ("Me despido", "M e d e s p i d o"),
])
def test_add_space(a, res):
    assert add_space(a) == res

#Prueba 7

@pytest.mark.parametrize("a, b, res", [
    ([1, 5, 2, 8], 4,  [8, 1]),
    ([-5, 3, 50], 3, [50, -5]),
    ([0, 3, 5, 7, 8, 10], 6, [10, 0]),
])
def test_max_min(a, b, res):
    assert max_min(a, b) == res

#Prueba 8

@pytest.mark.parametrize("a, res", [
    ([1, 5, 2, 8],  [2, 10, 4, 16]),
    ([1, 2, 3, 4], [2, 4, 6, 8]),
    ([0, -4, 20, 1], [0, -8, 40, 2]),
])
def test_double(a, res):
    assert double (a) == res

#Prueba 9

@pytest.mark.parametrize("a, res", [
    (3, True),
    (8, False),
    (7, True),
])
def test_prime_number(a, res):
    assert prime_number(a) == res

#Prueba 10

@pytest.mark.parametrize("a, res", [
    (3, 6),
    (4, 24),
    (5, 120),
])
def test_check_factorial(a, res):
    assert check_factorial(a) == res

#Pruebe este pytest con el comando: pytest "Test_tp5.py"