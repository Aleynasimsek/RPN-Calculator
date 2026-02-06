#!/bin/bash

# PostgreSQL servisini başlat
sudo service postgresql start
sleep 5

# 'ubuntu' kullanıcısı için bir veritabanı rolü oluştur
# Şifre: 1234
sudo -u postgres psql -c "CREATE USER ubuntu WITH SUPERUSER PASSWORD '1234';"

# Ders için bir veritabanı oluştur
sudo -u postgres createdb -O ubuntu odev_db

# SQL dosyasını içeri aktar
# Not: Codespaces projeyi /workspaces/REPO_ADI altına atar.
# '*' işareti repo adı ne olursa olsun dosyayı bulmasını sağlar.
sudo -u postgres psql -d okul_db -f /workspaces/*/odev.sql

echo "Veritabanı kurulumu tamamlandı! 'deucs_db' hazır. Şifre: 1234"


