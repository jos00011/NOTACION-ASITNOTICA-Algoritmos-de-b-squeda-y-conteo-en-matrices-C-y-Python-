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