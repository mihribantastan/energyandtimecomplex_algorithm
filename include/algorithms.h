#ifndef ALGORITHMS_H
#define ALGORITHMS_H

#include <vector>

typedef std::vector<std::vector<int>> Matrix;

void mergeSort(std::vector<int>& arr, int l, int r);
void quickSort(std::vector<int>& arr, int low, int high);
Matrix strassen(Matrix A, Matrix B, int n);

#endif