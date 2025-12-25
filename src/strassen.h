#ifndef STRASSEN_H
#define STRASSEN_H

#include <vector>

// Matrix tipini burada tanımlıyoruz ki main.cpp de görebilsin
typedef std::vector<std::vector<int>> Matrix;

Matrix strassen(const Matrix& A, const Matrix& B, int n);

#endif