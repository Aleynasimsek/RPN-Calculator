# RPN Hesap Makinesi (Ödev 2)

Bu proje, **Ters Polonya Notasyonu (Reverse Polish Notation - RPN)** mantığıyla çalışan bir hesap makinesi uygulamasıdır. Verilen matematiksel ifadeleri yığın (stack) yapısı kullanarak hesaplar.

## 📝 Ödev Tanımı
Ödev kapsamında aşağıdaki sınıf diyagramına uygun bir RPN hesap makinesi gerçekleştirilmiştir:
* **Girdi:** `3 4 +` -> **Çıktı:** `7`
* **Girdi:** `3 4 2 + -` -> **Çıktı:** `3`
* **Girdi:** `2 3 4 5 * + -` -> **Karşılığı:** `((5*4)+3)-2`

### 🏗️ Mimari ve Sınıflar
Proje, "Has-A" ilişkisi ile birbirine bağlı 4 ana bileşenden oluşur:

1.  **Calculator (Ana Sınıf):** Hesap makinesinin beynidir.
2.  **Stack (Yığın):** İşlemlerin gerçekleştirilmesi için gerekli LIFO (Last In First Out) yapısını sağlar.
3.  **Operator (Soyut Sınıf):** Farklı operatörler (Toplama, Çıkarma, Çarpma, Bölme) için temel sınıftır.
    * *Adder, Subtracter, Multiplier, Divider* alt sınıfları mevcuttur.
4.  **CalculatorGui:** Kullanıcı ile etkileşime giren (Girdi alma, Sonuç gösterme) arayüz sınıfıdır.

### 🚀 Örnek Senaryo
Büyük bir girdinin adım adım işlenmesi:
**Girdi:** `15 7 1 1 + − ÷ 3 × 2 1 1 + + −`

| Adım | İşlem | Yığın Durumu (Kırmızı: Yığındaki Sayılar) |
| :--- | :--- | :--- |
| 1 | `15 7 1 1` ekle | `15, 7, 1, 1` |
| 2 | `+` (1+1) | `15, 7, 2` |
| 3 | `-` (7-2) | `15, 5` |
| 4 | `÷` (15/5) | `3` |
| 5 | `3` ekle | `3, 3` |
| 6 | `×` (3*3) | `9` |
| ... | ... | ... |
| **Sonuç** | **=** | **5** |

### ✅ İstenen Özellikler ve Kontroller
* **Hata Yönetimi:** Sıfıra bölme, eksik operatör veya eksik operand durumlarında program çökmez, hata mesajı verir.
* **Loglama:** Oluşan hatalar `error_log.txt` dosyasına kaydedilir.

---

## 🛠️ Kurulum ve Test
Bu projeyi GitHub Codespaces üzerinde çalıştırmak için:

1.  **Terminali açın.**
2.  **Otomatik Testleri Başlatın:**
    ```bash
    python3 lab50-v6.py tests
    ```
    *(Bu komut C# kodunu derler ve senaryoları test eder)*

3.  **Manuel Çalıştırma:**
    ```bash
    mono Calculator.exe
    ```