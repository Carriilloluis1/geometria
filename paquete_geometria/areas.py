#1.
import math

def calcular_area_circulo(radio: float = 3) -> float:
    
    '''Calcula el area del circulo dado su radio'''
    
    area = math.pi * (radio ** 2)
    
    return area

def calcular_area_cuadrado(lado: float) -> float:
    
    '''Calcula el area del cuadrado dado su lado'''
    
    area = lado * lado
    
    return area

def calcular_area_triangulo(base: float, altura: float) -> float:
    
    '''Calcula el area del triangulo dado su base y altura'''
    
    area = (base * altura) / 2
    
    return area


