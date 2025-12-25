import subprocess
import time
import csv
import random
import os

POWER_RATINGS = {
    "merge": 15.0,
    "quick": 18.0,
    "strassen": 28.0  # Strassen daha fazla güç tüketir
}

def generate_test_case(algo, size):
    input_path = f"../inputs/input_{algo}_{size}.txt"
    with open(input_path, 'w') as f:
        if algo == "strassen":
            # Matris boyutu n, sonra n x n matris A, sonra n x n matris B
            f.write(f"{size}\n")
            for _ in range(2 * size): # A ve B matrisleri için toplam 2*size satır
                row = [random.randint(1, 100) for _ in range(size)]
                f.write(" ".join(map(str, row)) + "\n")
        else:
            # Sıralama için: n ve n tane sayı
            f.write(f"{size}\n")
            nums = [random.randint(1, 100000) for _ in range(size)]
            f.write(" ".join(map(str, nums)) + "\n")
    return input_path

def run_benchmark(algo, input_file):
    # C++ executable yolunu kendi build sistemine göre ayarla
    exe_path = "../build/program" if os.name != 'nt' else "../build/program.exe"
    result = subprocess.run([exe_path, algo, input_file], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Hata: {result.stderr}")
        return 0
    return float(result.stdout.strip())

def main():
    # Strassen için n değeri 2'nin kuvveti olmalı: 64, 128, 256
    # Sıralama için: 1000, 5000, 10000
    test_configs = [
        ("merge", 1000), ("merge", 5000), ("merge", 10000),
        ("quick", 1000), ("quick", 5000), ("quick", 10000),
        ("strassen", 64), ("strassen", 128), ("strassen", 256)
    ]
    
    results = []
    
    for algo, size in test_configs:
        print(f"Test Ediliyor: {algo} - Boyut: {size}")
        input_path = generate_test_case(algo, size)
        
        # C++'dan gelen zaman (mikrosaniye)
        duration_micros = run_benchmark(algo, input_path)
        duration_sec = duration_micros / 1_000_000
        
        # Enerji = P * T
        energy = POWER_RATINGS[algo] * duration_sec
        
        results.append({
            "Algoritma": algo,
            "Girdi_Boyutu": size,
            "Sure_Sn": f"{duration_sec:.6f}",
            "Guc_Watt": POWER_RATINGS[algo],
            "Enerji_Joule": f"{energy:.6f}"
        })

    # CSV'ye kaydet
    with open('../results/result.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print("İşlem tamam! Sonuçlar results/result.csv dosyasında.")

if __name__ == "__main__":
    main()