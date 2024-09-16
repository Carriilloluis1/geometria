import paquete_geometria.areas as paqarea
import paquete_geometria.perimetros as paqper

# Calculo de Areas

area_circulo = paqarea.calcular_area_circulo()
print(area_circulo)

area_cuadrado = paqarea.calcular_area_cuadrado(25)
print(area_cuadrado)

area_triangulo = paqarea.calcular_area_triangulo(20,10.2)
print(area_triangulo)


#Calculo Perímetros

perimetro_circulo = paqper.calcular_perimetro_circulo(8)
print(perimetro_circulo)

perimetro_cuadrado = paqper.calcular_perimetro_cuadrado(20)
print(perimetro_cuadrado)

perimetro_triangulo = paqper.calcular_perimetro_triangulo(15,50,10)
print(perimetro_triangulo)


