🧮 RPN Hesap Makinesi (Ödev 2)
Bu proje, Ters Polonya Notasyonu (Reverse Polish Notation - RPN) mantığıyla çalışan bir hesap makinesi uygulamasıdır. Verilen matematiksel ifadeleri yığın (stack) yapısı kullanarak hesaplar.

📝 Ödev Tanımı
Ödev kapsamında aşağıdaki sınıf diyagramına uygun bir RPN hesap makinesi gerçekleştirilmiştir:

Girdi: 3 4 + -> Çıktı: 7

Girdi: 3 4 2 + - -> Çıktı: 3

Girdi: 2 3 4 5 * + - -> Karşılığı: ((5*4)+3)-2

🏗️ Mimari ve Sınıflar
Proje, "Has-A" ilişkisi ile birbirine bağlı 4 ana bileşenden oluşur:

Calculator (Ana Sınıf): Hesap makinesinin beynidir.

Stack (Yığın): İşlemlerin gerçekleştirilmesi için gerekli LIFO (Last In First Out) yapısını sağlar.

Operator (Soyut Sınıf): Farklı operatörler için temel sınıftır. Adder, Subtracter, Multiplier, Divider alt sınıfları mevcuttur.

CalculatorGui: Kullanıcı ile etkileşime giren arayüz sınıfıdır.

🚀 Örnek Senaryo
Girdi: 15 7 1 1 + − ÷ 3 × 2 1 1 + + −

Adım	İşlem	Yığın Durumu
1	15, 7, 1, 1 ekle	15, 7, 1, 1
2	+ (1+1)	15, 7, 2
3	- (7-2)	15, 5
4	÷ (15/5)	3
...	...	...
Son	Sonuç	5
✅ İstenen Özellikler ve Kontroller
Hata Yönetimi: Sıfıra bölme, eksik operatör veya eksik operand durumlarında program çökmez, kullanıcıya anlamlı bir hata mesajı verir.

Loglama: Oluşan hatalar otomatik olarak error_log.txt dosyasına kaydedilir.

🛠️ Kurulum ve Çalıştırma (Codespaces)
Bu proje, Ubuntu 24.04 tabanlı özel bir Docker ortamında yapılandırılmıştır. Gerekli tüm derleyiciler otomatik olarak yüklüdür.

1. Kodun Derlenmesi

C# kaynak kodunu derleyerek çalıştırılabilir (.exe) dosya oluşturmak için:

Bash
mcs Calculator.cs -out:Calculator.exe
2. Manuel Çalıştırma

Programı kendi girdilerinizle test etmek için:

Bash
mono Calculator.exe
3. Otomatik Test ve Puanlama

Kodun doğruluğunu ve hata kontrollerini (sıfıra bölme vb.) otomatik olarak test etmek için:

Bash
python3 check.py
