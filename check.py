import urllib.request
import subprocess
import os
import sys

# SENİN GIST LİNKİN
TEST_URL = "https://gist.githubusercontent.com/Aleynasimsek/a58a16fa2adfbbbde27e907574ed0fbb/raw/0d3ebc3dd7e8375f740e757fef3bf759bc73495c/__init__.py"

def run_tests():
    print("🔄 Güncel test kriterleri sunucudan alınıyor...")
    
    # Klasör yoksa oluştur
    if not os.path.exists("tests"):
        os.makedirs("tests")

    try:
        # Dosyayı indir ve üzerine yaz
        urllib.request.urlretrieve(TEST_URL, "tests/__init__.py")
        print("✅ Test dosyası güncellendi. Sınav başlıyor!\n")
        
        # Test motorunu çalıştır
        subprocess.run([sys.executable, "lab50-v6.py", "tests"])
        
    except Exception as e:
        print(f"❌ Hata: Test dosyası indirilemedi. İnternet bağlantınızı kontrol edin.\n{e}")

if __name__ == "__main__":
    run_tests()