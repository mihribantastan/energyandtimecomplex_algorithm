import os
import subprocess
import csv

# Watt değerleri (Simülasyon)
POWER_VALS = {"merge": 15.2, "quick": 18.5, "strassen": 26.8}

# Dosya yolları (Senin klasör yapına göre)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXE_PATH = os.path.join(BASE_DIR, "build", "program.exe")
INPUTS_DIR = os.path.join(BASE_DIR, "inputs")
RESULTS_CSV = os.path.join(BASE_DIR, "results", "result.csv")

def main():
    # Derleme adımı
    cpp_files = [os.path.join(BASE_DIR, "src", f) for f in ["main.cpp", "mergesort.cpp", "quicksort.cpp", "strassen.cpp"]]
    subprocess.run(["g++", "-O3"] + cpp_files + ["-o", EXE_PATH])

    results = []
    # Test senaryoları (Senin input dosyalarınla eşleşmeli)
    tests = [
        ("merge", "input_small.txt", 1000),
        ("merge", "input_medium.txt", 5000),
        ("merge", "input_large.txt", 10000),
        ("quick", "input_small.txt", 1000),
        ("quick", "input_medium.txt", 5000),
        ("quick", "input_large.txt", 10000),
        ("strassen", "matrix_small.txt", 64),
        ("strassen", "matrix_medium.txt", 128),
        ("strassen", "matrix_large.txt", 256)
    ]

    for algo, file_name, n in tests:
        in_path = os.path.join(INPUTS_DIR, file_name)
        process = subprocess.run([EXE_PATH, algo, in_path], capture_output=True, text=True)
        
        try:
            t_sec = float(process.stdout.strip()) / 1_000_000
            energy = POWER_VALS[algo] * t_sec
            results.append({"Algorithm": algo, "N": n, "Time(s)": round(t_sec, 6), "Energy(J)": round(energy, 6)})
            print(f"Tamamlandı: {algo} ({file_name})")
        except:
            print(f"Hata: {algo} için {file_name} okunamadı.")

    # CSV Yazdırma
    with open(RESULTS_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Algorithm", "N", "Time(s)", "Energy(J)"])
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    main()