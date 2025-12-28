import csv
import os

# Dosya yollarını belirlemek için
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_INPUT = os.path.join(BASE_DIR, "results", "result.csv")
EXCEL_OUTPUT = os.path.join(BASE_DIR, "results", "Algoritma_Analiz_Raporu.csv")

def convert_to_excel_compatible():
    if not os.path.exists(CSV_INPUT):
        print(f"Hata: {CSV_INPUT} dosyası bulunamadı! Önce deneyi çalıştırın.")
        return

    # Mevcut veriyi okumak için
    with open(CSV_INPUT, 'r', encoding='utf-8') as f_in:
        reader = csv.reader(f_in)
        data = list(reader)

    # Excel'in kolonları tanıması için ';' ayırıcı ve 'utf-8-sig' (BOM) kullanıyoruz
    with open(EXCEL_OUTPUT, 'w', newline='', encoding='utf-8-sig') as f_out:
        # Noktalı virgül (;) Excel'in kolonları direkt ayırmasını sağlar
        writer = csv.writer(f_out, delimiter=';')
        writer.writerows(data)
    
    print(f"\n✅ İşlem Başarılı!")
    print(f"📁 Konum: {EXCEL_OUTPUT}")
    print("👉 Bu dosyayı Excel ile açtığında kolonların ayrıldığını göreceksin.")

if __name__ == "__main__":
    convert_to_excel_compatible()