import pandas as pd
import matplotlib.pyplot as plt
import os

# Dosya yollarını belirlemek için
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "results", "result.csv")
SAVE_DIR = os.path.join(BASE_DIR, "results")

def create_improved_plots():
    if not os.path.exists(CSV_PATH): return
    df = pd.read_csv(CSV_PATH)

    # --- ZAMAN GRAFİĞİ (LOGARİTMİK ÖLÇEK) ---
    plt.figure(figsize=(10, 6))
    for algo in df['Algorithm'].unique():
        subset = df[df['Algorithm'] == algo]
        plt.plot(subset['N'], subset['Time(s)'], marker='o', label=algo)
    
    plt.yscale('log')  # Logaritmik ölçek
    plt.title('Zaman Karmaşıklığı (Logaritmik Ölçek)', fontsize=14)
    plt.xlabel('Girdi Boyutu (n)')
    plt.ylabel('Saniye (Log Scale)')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.legend()
    plt.savefig(os.path.join(SAVE_DIR, "zaman_log.png"))
    plt.close()

    # --- ENERJİ GRAFİĞİ (AYRIK ANALİZ) ---
    plt.figure(figsize=(10, 6))
    # Sadece sorting algoritmalarını ayrıca gösteren bir alt grafik veya renk kodlaması
    plt.yscale('log')
    high_level = df[df['Level'] == 'High']
    plt.bar(high_level['Algorithm'], high_level['Energy(J)'], color=['blue', 'orange', 'green'])
    plt.title('Enerji Tüketimi E(n) (Logaritmik Ölçek)', fontsize=14)
    plt.ylabel('Joule (Log Scale)')
    plt.savefig(os.path.join(SAVE_DIR, "enerji_log.png"))
    print("✅ Yeni ve anlaşılır grafikler 'results' klasörüne kaydedildi.")

if __name__ == "__main__":
    create_improved_plots()