# 📘 Análisis de Algoritmos y Complejidad Computacional

Repositorio con implementaciones en **C++** y **Python** enfocadas en el análisis de algoritmos, conteo de números pares y primos en matrices, además de una comparación gráfica de complejidad temporal utilizando notación Big-O.

---

# 📂 Contenido del Repositorio

## 1️⃣ Generación y análisis de matrices
Implementación de programas que:
- Generan matrices aleatorias.
- Cuentan números pares.
- Detectan números primos.
- Calculan tiempo de ejecución.

Lenguajes utilizados:
- C++
- Python

---

## 2️⃣ Comparación de complejidad temporal
Script en Python que genera una gráfica comparando:
- Complejidad lineal \(O(n)\)
- Complejidad constante \(O(1)\)

Usando la librería:
- Matplotlib

---

# 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|---|---|
| C++ | Implementación eficiente de algoritmos |
| Python | Simulación y análisis |
| Matplotlib | Visualización gráfica |
| Git & GitHub | Control de versiones |

---

# 📌 Código 1 — Análisis de Matriz en C++

## 🔹 Descripción
El programa:
1. Genera una matriz de tamaño 200x200.
2. Llena la matriz con números aleatorios entre 0 y 100.
3. Cuenta números pares.
4. Cuenta números primos.
5. Mide el tiempo de ejecución.

## ▶️ Compilación y ejecución

```bash
#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <cmath>
using namespace std;

vector<vector<int>> generarMatriz(int filas, int columnas) {
    vector<vector<int>> matriz(filas, vector<int>(columnas));
    for (int i = 0; i < filas; ++i)
        for (int j = 0; j < columnas; ++j)
            matriz[i][j] = rand() % 101;
    return matriz;
}

int contarPares(const vector<vector<int>>& matriz) {
    int conteo = 0;
    for (const auto& fila : matriz)
        for (int val : fila)
            if (val % 2 == 0) ++conteo;
    return conteo;
}

bool esPrimo(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

int contarPrimos(const vector<vector<int>>& matriz) {
    int conteo = 0;
    for (const auto& fila : matriz)
        for (int val : fila)
            if (esPrimo(val)) ++conteo;
    return conteo;
}

int main() {
    srand(time(0));
    int filas = 200, columnas = 200;
    vector<vector<int>> matriz = generarMatriz(filas, columnas);

    clock_t inicio = clock();

    int pares = contarPares(matriz);
    int primos = contarPrimos(matriz);

    clock_t fin = clock();

    cout << "Números pares: " << pares << endl;
    cout << "Números primos: " << primos << endl;
    cout << "Tiempo de ejecución: "
         << double(fin - inicio) / CLOCKS_PER_SEC << " segundos\n";

    return 0;
}
```

## 📸 Ejemplo de salida

<img width="369" height="81" alt="Screenshot 2026-05-06 111848" src="https://github.com/user-attachments/assets/1f064cbd-a838-41ec-83fc-d10e8d7998ca" />

---

# 📌 Código 2 — Análisis de Matriz en Python

## 🔹 Descripción
Este programa realiza exactamente el mismo procedimiento que la versión en C++, permitiendo comparar:
- Legibilidad
- Rendimiento
- Tiempo de ejecución

## ▶️ Ejecución

```bash
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
```

## 📸 Ejemplo de salida

<img width="304" height="69" alt="Screenshot 2026-05-06 111700" src="https://github.com/user-attachments/assets/b2cb190e-15f5-4cae-993b-85a384f6a862" />


---

# 📌 Código 3 — Gráfica de Complejidad Temporal

## 🔹 Descripción
Este script genera una gráfica comparativa entre:
- Un algoritmo de complejidad lineal \(O(n)\)
- Un algoritmo de complejidad constante \(O(1)\)

## ▶️ Ejecución

```bash
import matplotlib.pyplot as plt

n_vals = [1000, 10000, 50000, 100000, 200000, 500000, 1000000]
tiempos_linear = [0.000050, 0.000480, 0.002400, 0.004800, 0.009600, 0.024000, 0.048000]
tiempos_const = [0.000001] * len(n_vals)

plt.figure(figsize=(8,5))
plt.plot(n_vals, tiempos_linear, 'o-', label='O(n) - Bucle')
plt.plot(n_vals, tiempos_const, 's-', label='O(1) - Fórmula')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de tiempos: suma de 1..n')
plt.legend()
plt.grid(True)
plt.show()
```

## 📈 Resultado esperado

<img width="803" height="573" alt="Screenshot 2026-05-06 113011" src="https://github.com/user-attachments/assets/04cb88ce-fcbc-45ac-86af-0eb457cedb7a" />

---

# 📊 Explicación de Complejidad

| Algoritmo | Complejidad |
|---|---|
| Conteo de pares | \(O(n \times m)\) |
| Conteo de primos | \(O(n \times m \times \sqrt{k})\) |
| Fórmula matemática | \(O(1)\) |
| Bucle acumulativo | \(O(n)\) |

Donde:
- \(n\) = filas
- \(m\) = columnas
- \(k\) = valor máximo analizado

---

# 📖 Objetivo Académico

Este proyecto fue desarrollado con fines educativos para:
- Analizar algoritmos.
- Comprender la complejidad temporal.
- Comparar rendimiento entre lenguajes.
- Visualizar comportamiento computacional.

---

# 👨‍💻 Autor

**Jose Enrique Coaguila Alave**  
Ingeniería de Sistemas

---
