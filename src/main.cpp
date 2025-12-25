#include <iostream>
#include <vector>
#include <fstream>
#include <chrono>
#include <string>
#include <utility> // for std::pair

// Kendi yazdığın header dosyaları
#include "mergesort.h"
#include "quicksort.h"
#include "strassen.h"

using namespace std;
using namespace std::chrono;

// Yardımcı fonksiyon: Dosyadan vektör (sıralama için) okur
vector<int> readVector(string filename) {
    ifstream file(filename);
    int size;
    file >> size;
    vector<int> data(size);
    for (int i = 0; i < size; i++) {
        file >> data[i];
    }
    return data;
}

// Yardımcı fonksiyon: Dosyadan iki matris (Strassen için) okur
pair<Matrix, Matrix> readMatrices(string filename, int& n) {
    ifstream file(filename);
    file >> n;
    Matrix A(n, vector<int>(n)), B(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) file >> A[i][j];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) file >> B[i][j];
    return {A, B};
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        cerr << "Kullanim: program <algoritma> <input_dosyasi>" << endl;
        return 1;
    }

    string algo = argv[1];
    string inputFile = argv[2];
    
    // Ölçüm değişkenleri
    high_resolution_clock::time_point start, stop;

    if (algo == "merge" || algo == "quick") {
        vector<int> data = readVector(inputFile);
        
        start = high_resolution_clock::now();
        if (algo == "merge") {
            mergeSort(data, 0, data.size() - 1);
        } else {
            quickSort(data, 0, data.size() - 1);
        }
        stop = high_resolution_clock::now();

    } else if (algo == "strassen") {
        int n;
        auto matrices = readMatrices(inputFile, n);
        
        start = high_resolution_clock::now();
        Matrix result = strassen(matrices.first, matrices.second, n);
        stop = high_resolution_clock::now();
    }

    // Mikrosaniye cinsinden süreyi hesapla
    auto duration = duration_cast<microseconds>(stop - start);

    // Python'un yakalaması için sadece sayıyı yazdırıyoruz
    cout << duration.count() << endl;

    return 0;
}