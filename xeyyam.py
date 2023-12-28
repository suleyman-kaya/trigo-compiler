import re
import sympy as sp
import sys

def keep_trig_functions_only(text):
    # Trigonometrik fonksiyonları tutan regex
    trig_pattern = r'(sin|cos|tan|cot|sec|csc)\(([^)]+)\)'
    # Trigonometrik fonksiyonları bul
    trig_functions = re.findall(trig_pattern, text)
    # Sadece trigonometrik fonksiyonları birleştir
    trig_values = []
    for func, value in trig_functions:
        angle_rad = sp.rad(float(value))
        if func == 'sin':
            result = sp.sin(angle_rad)
        elif func == 'cos':
            result = sp.cos(angle_rad)
        elif func == 'tan':
            result = sp.tan(angle_rad)
        elif func == 'cot':
            result = 1 / sp.tan(angle_rad)
        elif func == 'sec':
            result = sp.sec(angle_rad)
        elif func == 'csc':
            result = 1 / sp.sin(angle_rad)
        trig_values.append(result)
    cleaned_text = ''.join(["1" if val.equals(1) else "0" for val in trig_values])
    return cleaned_text

def clean_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            # Sadece trigonometrik fonksiyonları tut
            trig_functions_text = keep_trig_functions_only(content)
            # Temizlenmiş içeriği yeni bir dosyaya yaz
            with open("cleaned_" + file_name, 'w') as cleaned_file:
                cleaned_file.write(trig_functions_text)
            print("Dosya temizlendi ve 'cleaned_" + file_name + "' olarak kaydedildi.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")

# Kullanım
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python script.py dosya_adı")
    else:
        dosya_adı = sys.argv[1]
        clean_text_file(dosya_adı)
