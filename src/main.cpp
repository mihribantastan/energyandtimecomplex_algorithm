#include <iostream>
#include <fstream>
#include <chrono>
#include <string>
#include "../include/algorithms.h"

using namespace std;
using namespace std::chrono;

int main(int argc, char* argv[]) {
    // Argüman kontrolü
    if (argc < 3) return 1;
    string algo = argv[1];
    string file_path = argv[2];
    
    ifstream fin(file_path);
    int n; fin >> n;

    high_resolution_clock::time_point t1, t2;

    // Algoritma seçimi ve zaman ölçümü
    if (algo == "strassen") {
        Matrix A(n, vector<int>(n)), B(n, vector<int>(n));
        for(int i=0; i<n; i++) for(int j=0; j<n; j++) fin >> A[i][j];
        for(int i=0; i<n; i++) for(int j=0; j<n; j++) fin >> B[i][j];
        t1 = high_resolution_clock::now();
        strassen(A, B, n);
        t2 = high_resolution_clock::now();
    } else {
        vector<int> arr(n);
        for(int i=0; i<n; i++) fin >> arr[i];
        t1 = high_resolution_clock::now();
        if (algo == "merge") mergeSort(arr, 0, n-1);
        else quickSort(arr, 0, n-1);
        t2 = high_resolution_clock::now();
    }

    // Zamanı mikro saniye cinsinden yazdır
    cout << duration_cast<microseconds>(t2 - t1).count() << endl;
    return 0;
}