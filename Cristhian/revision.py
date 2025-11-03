notas = [3.5, 4.2, 3.8, 3.6, 4.1, 4.3, 3.9, 3.7, 4.0, 4.4,
        3.5, 4.2, 3.6, 4.0, 3.9, 4.1, 3.8, 4.2, 3.5, 4.3,
        3.7, 4.0, 3.6, 4.5, 3.9, 4.1, 3.5, 4.2, 3.8, 3.7,
        4.0, 4.2, 3.6, 3.9, 4.4, 3.5, 4.1, 3.8, 4.0, 3.6]

# Calcular estadísticas
maximo = max(notas)
minimo = min(notas)
promedio = sum(notas) / len(notas)

# Calcular mediana
notas_ordenadas = sorted(notas)
n = len(notas_ordenadas)
if n % 2 == 0:
    # Si hay un número par de elementos, tomar el promedio de los dos del medio
    mediana = (notas_ordenadas[n//2 - 1] + notas_ordenadas[n//2]) / 2
else:
    # Si hay un número impar de elementos, tomar el del medio
    mediana = notas_ordenadas[n//2]

# Imprimir resultados
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Promedio: {promedio:.2f}")
print(f"Mediana: {mediana:.2f}")

numero1 = 20
numero2 = 10

suma = numero1+numero2
print(f"suma={suma}")