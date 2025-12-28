import random
import os

# Girdi dosyalarını oluşturma
def create_inputs():
    if not os.path.exists("inputs"):
        os.makedirs("inputs")

    # 1. SIRALAMA İÇİN INPUTLAR (Merge & Quick)
    sizes = {"small": 1000, "medium": 5000, "large": 10000}
    
    for name, size in sizes.items():
        with open(f"inputs/input_{name}.txt", "w") as f:
            f.write(f"{size}\n") # İlk satır eleman sayısı
            nums = [random.randint(1, 100000) for _ in range(size)]
            f.write(" ".join(map(str, nums)))
        print(f"input_{name}.txt oluşturuldu.")

    # 2. STRASSEN İÇİN MATRİS INPUTLARI (Mutlaka 2'nin kuvveti olmalı)
    # n=64 (4096 eleman), n=128 (16384 eleman), n=256 (65536 eleman)
    matrix_sizes = {"small": 64, "medium": 128, "large": 256}
    
    for name, n in matrix_sizes.items():
        with open(f"inputs/matrix_{name}.txt", "w") as f:
            f.write(f"{n}\n") # İlk satır n (matris boyutu n x n)
            # İki matris gerekiyor (A ve B)
            for _ in range(2): # İki matris için döngü
                for _ in range(n): # Her satır için
                    row = [random.randint(1, 10) for _ in range(n)]
                    f.write(" ".join(map(str, row)) + "\n")
        print(f"matrix_{name}.txt oluşturuldu.")

if __name__ == "__main__":
    create_inputs()