# Leer la cantidad de litros
litros = float(input("Ingrese la cantidad de litros: "))

# Calcular la cantidad de galones
galones = litros / 3.785

# Leer el precio por galón
precio_por_galon = float(input("Ingrese el precio por galón: "))

# Calcular el pago total
pago_total = galones * precio_por_galon

# Imprimir los resultados
print("La cantidad de galones es:", galones)
print("El pago total es:", pago_total)