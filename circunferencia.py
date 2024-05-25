import math

print("---------------------------------------------------------------------------")
print("Programa para calcular la ecuación de una circunferencia")
print("Pull request 1")
print("---------------------------------------------------------------------------")
print("Implementacion de suma de las coordenadas del centro de la circunferencia")
print("---------------------------------------------------------------------------")

print("Primer commit")
print("Bienvenidos al programa")
print("---------------------------------------------------------------------------")
# Coordenadas del centro de la circunferencia (h, k)
h = float(input("Ingrese la coordenada x del centro (h): "))
k = float(input("Ingrese la coordenada y del centro (k): "))
print("---------------------------------------------------------------------------")

# Coordenadas de un punto en la circunferencia (x, y)
x = float(input("Ingrese la coordenada x de un punto en la circunferencia (x): "))
y = float(input("Ingrese la coordenada y de un punto en la circunferencia (y): "))
print("---------------------------------------------------------------------------")

# Calcula el radio
radio = math.sqrt((x - h)**2 + (y - k)**2)

# Escribe la ecuación de la circunferencia
ecuacion = f"(x - {h})^2 + (y - {k})^2 = {radio**2}"

# Punto medio
punto_medio = (h, k)

suma =  h + k

# Imprime los resultados
print("---------------------------------------------------------------------------")
print(f"Ecuación de la circunferencia: {ecuacion}")
print(f"Radio de la circunferencia: {radio}")
print(f"Punto medio de la circunferencia: ({punto_medio[0]}, {punto_medio[1]})")
print(f'Suma de las coordenadas del centro de la circunferencia: {suma}')
print("---------------------------------------------------------------------------")

print("Gracias por usar el programa")