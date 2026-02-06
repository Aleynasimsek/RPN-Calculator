import check50
import check50.csharp

@check50.check(points=10)
def exists():
    """Dosya Kontrolü: Calculator.cs var mi?"""
    check50.exists("Calculator.cs")

@check50.check(exists, points=10)
def compiles():
    """Derleme Kontrolü: Kod hatasiz derleniyor mu?"""
    check50.csharp.compile("Calculator.cs")

@check50.check(compiles, points=10)
def test_simple_addition():
    """Basit Toplama: 3 4 + -> 7"""
    check50.run("mono Calculator.exe").stdin("3 4 +").stdout("7").exit(0)

@check50.check(compiles, points=10)
def test_homework_example_2():
    """Odev Ornegi 2: 3 4 2 + - -> 3"""
    # Kaynak: Odev dokumani madde [4]
    check50.run("mono Calculator.exe").stdin("3 4 2 + -").stdout("3").exit(0)

@check50.check(compiles, points=10)
def test_decimal_multiplication():
    """Ondalikli Sayi Testi: 2.5 4 * -> 10"""
    # Kodun double tipini dogru kullandigini test eder
    check50.run("mono Calculator.exe").stdin("2.5 4 *").stdout("10").exit(0)

@check50.check(compiles, points=10)
def test_negative_result():
    """Negatif Sonuc Testi: 5 8 - -> -3"""
    check50.run("mono Calculator.exe").stdin("5 8 -").stdout("-3").exit(0)

@check50.check(compiles, points=10)
def test_long_expression():
    """Karmasik RPN: 15 7 1 1 + - / 3 * 2 1 1 + + - -> 5"""
    input_str = "15 7 1 1 + - / 3 * 2 1 1 + + -"
    check50.run("mono Calculator.exe").stdin(input_str).stdout("5").exit(0)

@check50.check(compiles, points=10)
def test_divide_by_zero():
    """Hata Testi 1: Sifira Bolme (10 0 /)"""
    # Program cokmemeli, hata mesaji vermeli
    check50.run("mono Calculator.exe").stdin("10 0 /").stdout("(?i)hata|sıfıra bölme|exception").exit(0)

@check50.check(compiles, points=10)
def test_missing_operand():
    """Hata Testi 2: Eksik Operand (5 +)"""
    # Kaynak: Odev dokumani madde [34] - Islem icin yeterli sayi yok
    check50.run("mono Calculator.exe").stdin("5 +").stdout("(?i)hata|eksik|empty").exit(0)

@check50.check(compiles, points=10)
def test_unknown_operator():
    """Hata Testi 3: Tanimsiz Operator (5 3 &)"""
    # Kaynak: Odev dokumani madde [34]
    check50.run("mono Calculator.exe").stdin("5 3 &").stdout("(?i)hata|tanımsız|unknown").exit(0)
