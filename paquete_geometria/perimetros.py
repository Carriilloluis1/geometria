#2.

import math

def calcular_perimetro_circulo(radio: float = 3) -> float:
    
    '''Calcula el perímetro del circulo dado su radio'''
    
    perimetro = 2 * math.pi * radio
    
    return perimetro

def calcular_perimetro_cuadrado(lado: float) -> float:
    
    '''Calcula el perímetro del cuadrado dado su lado'''
    
    perimetro = lado * 4
    
    return perimetro

def calcular_perimetro_triangulo(lado_uno: float, lado_dos:float, lado_tres: float) -> float:
    
    '''Calcula el perímetro del triangulo dado el valor de sus 3 lados'''
    
    perimetro = lado_uno + lado_dos + lado_tres
    
    return perimetro
