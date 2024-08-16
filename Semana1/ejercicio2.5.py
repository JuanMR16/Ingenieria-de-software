# Solicitar los valores al usuario
valorA = float(input("Ingresa el valor de A: "))
valorB = float(input("Ingresa el valor de B: "))
valorC = float(input("Ingresa el valor de C: "))
12
# Calcular el área del triángulo
AreaTriangulo = valorB * (valorA - valorC) / 2

# Calcular el área del rectángulo
AreaRectangulo = valorB * valorC

# Calcular el área total (asumiendo que AreaTotal se refiere a la suma de las dos áreas)
AreaTotal = AreaTriangulo + AreaRectangulo

# Imprimir los resultados
print(f"Área del Triángulo: {AreaTriangulo}")
print(f"Área del Rectángulo: {AreaRectangulo}")
print(f"Área Total: {AreaTotal}")