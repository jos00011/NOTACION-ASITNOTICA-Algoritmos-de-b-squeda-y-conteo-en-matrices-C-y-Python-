import random
import time

def generar_matriz(filas, columnas):
    return [[random.randint(0, 100) for _ in range(columnas)] for _ in range(filas)]

def contar_pares(matriz):
    conteo = 0
    for fila in matriz:
        for valor in fila:
            if valor % 2 == 0:
                conteo += 1
    return conteo

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(matriz):
    conteo = 0
    for fila in matriz:
        for valor in fila:
            if es_primo(valor):
                conteo += 1
    return conteo

filas, columnas = 200, 200
matriz = generar_matriz(filas, columnas)

inicio = time.time()
pares = contar_pares(matriz)
primos = contar_primos(matriz)
fin = time.time()

print(f"Números pares: {pares}")
print(f"Números primos: {primos}")
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")