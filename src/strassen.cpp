#include "strassen.h"
#include <vector>

using namespace std;

typedef vector<vector<int>> Matrix;

// Matris toplama/çıkarma yardımcı fonksiyonları
Matrix add(const Matrix& A, const Matrix& B, int size) {
    Matrix res(size, vector<int>(size));
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            res[i][j] = A[i][j] + B[i][j];
    return res;
}

Matrix subtract(const Matrix& A, const Matrix& B, int size) {
    Matrix res(size, vector<int>(size));
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            res[i][j] = A[i][j] - B[i][j];
    return res;
}

Matrix strassen(const Matrix& A, const Matrix& B, int n) {
    if (n <= 64) { // Base case: Standart çarpım
        Matrix C(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++)
            for (int k = 0; k < n; k++)
                for (int j = 0; j < n; j++)
                    C[i][j] += A[i][k] * B[k][j];
        return C;
    }

    int newSize = n / 2;
    Matrix a11(newSize, vector<int>(newSize)), a12(newSize, vector<int>(newSize)),
           a21(newSize, vector<int>(newSize)), a22(newSize, vector<int>(newSize)),
           b11(newSize, vector<int>(newSize)), b12(newSize, vector<int>(newSize)),
           b21(newSize, vector<int>(newSize)), b22(newSize, vector<int>(newSize));

    for (int i = 0; i < newSize; i++) {
        for (int j = 0; j < newSize; j++) {
            a11[i][j] = A[i][j];
            a12[i][j] = A[i][j + newSize];
            a21[i][j] = A[i + newSize][j];
            a22[i][j] = A[i + newSize][j + newSize];
            b11[i][j] = B[i][j];
            b12[i][j] = B[i][j + newSize];
            b21[i][j] = B[i + newSize][j];
            b22[i][j] = B[i + newSize][j + newSize];
        }
    }

    Matrix p1 = strassen(add(a11, a22, newSize), add(b11, b22, newSize), newSize);
    Matrix p2 = strassen(add(a21, a22, newSize), b11, newSize);
    Matrix p3 = strassen(a11, subtract(b12, b22, newSize), newSize);
    Matrix p4 = strassen(a22, subtract(b21, b11, newSize), newSize);
    Matrix p5 = strassen(add(a11, a12, newSize), b22, newSize);
    Matrix p6 = strassen(subtract(a21, a11, newSize), add(b11, b12, newSize), newSize);
    Matrix p7 = strassen(subtract(a12, a22, newSize), add(b21, b22, newSize), newSize);

    Matrix c11 = add(subtract(add(p1, p4, newSize), p5, newSize), p7, newSize);
    Matrix c12 = add(p3, p5, newSize);
    Matrix c21 = add(p2, p4, newSize);
    Matrix c22 = add(subtract(add(p1, p3, newSize), p2, newSize), p6, newSize);

    Matrix C(n, vector<int>(n));
    for (int i = 0; i < newSize; i++) {
        for (int j = 0; j < newSize; j++) {
            C[i][j] = c11[i][j];
            C[i][j + newSize] = c12[i][j];
            C[i + newSize][j] = c21[i][j];
            C[i + newSize][j + newSize] = c22[i][j];
        }
    }
    return C;
}