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