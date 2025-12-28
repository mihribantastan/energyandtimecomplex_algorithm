#include "../include/algorithms.h"

// Matris toplama
Matrix add(Matrix A, Matrix B, int n) {
    Matrix res(n, std::vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) res[i][j] = A[i][j] + B[i][j];
    return res;
}

// Matris çıkarma
Matrix sub(Matrix A, Matrix B, int n) {
    Matrix res(n, std::vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) res[i][j] = A[i][j] - B[i][j];
    return res;
}

// Strassen algoritması
Matrix strassen(Matrix A, Matrix B, int n) {
    if (n <= 2) {
        Matrix C(n, std::vector<int>(n, 0));
        for(int i=0; i<n; i++)
            for(int k=0; k<n; k++)
                for(int j=0; j<n; j++) C[i][j] += A[i][k] * B[k][j];
        return C;
    }
    int k = n / 2;
    Matrix a11(k, std::vector<int>(k)), a12(k, std::vector<int>(k)), a21(k, std::vector<int>(k)), a22(k, std::vector<int>(k));
    Matrix b11(k, std::vector<int>(k)), b12(k, std::vector<int>(k)), b21(k, std::vector<int>(k)), b22(k, std::vector<int>(k));

    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            a11[i][j] = A[i][j]; a12[i][j] = A[i][j+k]; a21[i][j] = A[i+k][j]; a22[i][j] = A[i+k][j+k];
            b11[i][j] = B[i][j]; b12[i][j] = B[i][j+k]; b21[i][j] = B[i+k][j]; b22[i][j] = B[i+k][j+k];
        }
    }

    Matrix p1 = strassen(add(a11, a22, k), add(b11, b22, k), k);
    Matrix p2 = strassen(add(a21, a22, k), b11, k);
    Matrix p3 = strassen(a11, sub(b12, b22, k), k);
    Matrix p4 = strassen(a22, sub(b21, b11, k), k);
    Matrix p5 = strassen(add(a11, a12, k), b22, k);
    Matrix p6 = strassen(sub(a21, a11, k), add(b11, b12, k), k);
    Matrix p7 = strassen(sub(a12, a22, k), add(b21, b22, k), k);

    Matrix c11 = add(sub(add(p1, p4, k), p5, k), p7, k);
    Matrix c12 = add(p3, p5, k);
    Matrix c21 = add(p2, p4, k);
    Matrix c22 = add(sub(add(p1, p3, k), p2, k), p6, k);

    Matrix C(n, std::vector<int>(n));
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            C[i][j] = c11[i][j]; C[i][j+k] = c12[i][j];
            C[i+k][j] = c21[i][j]; C[i+k][j+k] = c22[i][j];
        }
    }
    return C;
}