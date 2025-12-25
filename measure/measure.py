import os
import subprocess
import csv
import math

# Güç Katsayıları (Watt)
POWER_VALS = {"merge": 15.2, "quick": 18.5, "strassen": 26.8}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXE_PATH = os.path.join(BASE_DIR, "build", "program.exe")
INPUTS_DIR = os.path.join(BASE_DIR, "inputs")
RESULTS_CSV = os.path.join(BASE_DIR, "results", "result.csv")

def estimate_complexity(n1, t1, n2, t2):
    """İki nokta arasındaki artıştan üstel karmaşıklığı (power) hesaplar."""
    if t1 <= 0 or t2 <= 0: return 0
    return math.log(t2 / t1) / math.log(n2 / n1)

def main():
    tests = [
        ("merge", "input_small.txt", 1000, "Low"),
        ("merge", "input_medium.txt", 5000, "Medium"),
        ("merge", "input_large.txt", 10000, "High"),
        ("quick", "input_small.txt", 1000, "Low"),
        ("quick", "input_medium.txt", 5000, "Medium"),
        ("quick", "input_large.txt", 10000, "High"),
        ("strassen", "matrix_small.txt", 64, "Low"),
        ("strassen", "matrix_medium.txt", 128, "Medium"),
        ("strassen", "matrix_large.txt", 256, "High")
    ]

    raw_data = []
    print("Ölçümler ve Karmaşıklık Analizi Başlıyor...")

    for algo, file_name, n, level in tests:
        in_path = os.path.join(INPUTS_DIR, file_name)
        process = subprocess.run([EXE_PATH, algo, in_path], capture_output=True, text=True)
        
        if process.returncode == 0:
            t_sec = float(process.stdout.strip()) / 1_000_000
            energy = POWER_VALS[algo] * t_sec
            raw_data.append({"algo": algo, "n": n, "t": t_sec, "e": energy, "level": level})

    # Sonuçları işleme ve O(n) hesaplama
    final_results = []
    for i in range(len(raw_data)):
        current = raw_data[i]
        
        # Karmaşıklığı bir önceki seviyeye göre hesapla (Small -> Medium, Medium -> Large)
        if current["level"] == "Low":
            observed_o = "N/A (Base)"
            observed_e = "N/A (Base)"
        else:
            prev = raw_data[i-1]
            o_power = estimate_complexity(prev["n"], prev["t"], current["n"], current["t"])
            e_power = estimate_complexity(prev["n"], prev["e"], current["n"], current["e"])
            observed_o = f"O(n^{o_power:.2f})"
            observed_e = f"E(n^{e_power:.2f})"

        final_results.append({
            "Algorithm": current["algo"],
            "Level": current["level"],
            "N": current["n"],
            "Time(s)": round(current["t"], 6),
            "Observed_O(n)": observed_o,
            "Energy(J)": round(current["e"], 6),
            "Observed_E(n)": observed_e
        })

    # CSV Yazdırma
    fieldnames = ["Algorithm", "Level", "N", "Time(s)", "Observed_O(n)", "Energy(J)", "Observed_E(n)"]
    with open(RESULTS_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(final_results)

    print(f"\nAnaliz Tamamlandı! '{RESULTS_CSV}' dosyasını inceleyebilirsin.")

if __name__ == "__main__":
    main()