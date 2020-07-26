#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import colorama
from colorama import Fore, Back, Style

#Renkler
rr= (Style.RESET_ALL)
mavi= (Fore.BLUE)
kirmizi= (Fore.RED)
yesil = (Fore.GREEN)
beyaz= (Fore.WHITE)
sari= (Fore.YELLOW)
siyah= (Fore.BLACK)
ciyan= (Fore.CYAN)
magenta= (Fore.MAGENTA)
#Renkler



#Fonksiyonlar
def linux_komutları():
    os.system("clear && toilet -f mono12 -F metal MRXWAI")
    print(kirmizi+  '====================')
    print(kirmizi+     '|'+rr+'  Temel Komutlar  '+kirmizi+'|')
    print(kirmizi+  '====================')
    print(sari + """

whoami     --> Hangi yetki ile işlem yaptığımızı gösterir

uname -a   --> Çekirdek genel bilgisi,sürümü vs. hakkında tam
kapsamlı bilgi edinmemizi sağlar.

pwd        --> Ekrana bulunduğunuz dizinin çıktısını verir.

clear      --> Ekranı temizler

ls         --> Dizini listeler

cd         --> Dizine geçiş yapar. " cd .. " ise bir önceki dizine
geçer

cp         --> Dosyayı kopyalar

mv         --> Dosyayı taşır

mkdir      --> Bulunduğumuz dizinde dosya oluşturmamızı sağlar.

rm -rf     --> Dosya siler

chmod +x   --> Çalıştırma düzenleme ve silme yetkisi verir

nano       --> Bu kodun sayesinde metin düzenleyebilir ve kendi
araçlarınızı yazabilirsiniz.

ifconfig   --> Yerel ip adresini gösterir.

route -n   --> Kendi modeminizin local ip adresini gösterir.

date       --> Tarih ve saati gösterir

cal        --> Takvimi gösterir.

man        --> detaylı yardım alma komutudur""")

    input(yesil+"\n\nGeri dönmek İçin Enter'a Basınız!")

def python_kodları():
    pass

def paket_kurulumları():
    os.system("clear && toilet -f mono12 -F metal MRXWAI")
    print(rr + """\nPaket kurulumları Bölümüne Hoş Geldiniz. Yaklaşık 500 MB'lık
bir kurulum işlemimiz olacaktır.""")
    print("\n")
    print(sari+"\nKuruluma -> 5")
    time.sleep(1)
    print(sari+"\nKuruluma -> 4")
    time.sleep(1)
    print(sari+"\nKuruluma -> 3")
    time.sleep(1)
    print(sari+"\nKuruluma -> 2")
    time.sleep(1)
    print(sari+"\nKuruluma -> 1""")
    time.sleep(1)
    print(sari+"\nKurulum Başladı!")
    os.system("termux-setup-storage")
    os.system("apt install sudo -y")
    os.system("apt install tsu -y")
    os.system("apt update -y && apt upgrade -y")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install unstable-repo -y")
    os.system("pkg install root-repo -y")
    os.system("pkg install figlet -y")
    os.system("pkg install cowsay -y")
    os.system("apt install fish -y")
    os.system("pkg install wget -y")
    os.system("pkg install curl -y")
    os.system("pkg install nmap -y")
    os.system("pkg install hydra -y")
    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pip install --upgrade pip")
    os.system("python3 -m pip install --upgrade pip")
    os.system("python -m pip install colorama")
    os.system("pip3 install one-lin3r")
    os.system("pip install requests")
    os.system("pip install wordlist")
    os.system("pkg install proot -y")
    os.system("pkg install chroot -y")
    os.system("pkg install openssh -y")
    os.system("pkg install openssl -y")
    os.system("pkg install php -y")
    os.system("pkg install perl -y")
    os.system("pkg install ruby -y")
    os.system("pkg install nodejs -y")
    os.system("pkg install nano -y")
    os.system("pkg install vim -y")
    os.system("pkg install neofetch -y")
    os.system("pkg install cmatrix -y")
    os.system("pkg install man -y")
    os.system("gem install lolcat -y")
    print(sari+'\nKurulum Bitti!')
    time.sleep(1)
    ana_menu()

def arac_kurulumları():
    os.system("clear && toilet -f mono12 -F metal MRXWAI")
    print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Bilgi Toplama')
    print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+' Sızma ve Sömürü')
    print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+' Web Uygulamaları')
    print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+' Dos & DDos')
    print(yesil+' [ '+rr+ '5' +yesil+' ] '+mavi+'->'+sari+' Sms Spam')
    print(yesil+' [ '+rr+ '6' +yesil+' ] '+mavi+'->'+sari+' Sosyal Medya')
    print(yesil+' [ '+rr+ '7' +yesil+' ] '+mavi+'->'+sari+' İşletim Sistemleri')
    print(yesil+' [ '+rr+ '8' +yesil+' ] '+mavi+'->'+sari+' Terminal Özelleştirme')
    print(yesil+' [ '+rr+ '9' +yesil+' ] '+mavi+'->'+sari+' Ekstra Tuşlar')
    print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
    print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Çıkış')
    secim = input(yesil+"\n\n [+] İşlem No: ")
    if secim == "1":#Bilgi Toplama
        os.system("clear && toilet -f mono12 -F metal MRXWAI")
        print(kirmizi+'=================')
        print(rr+     '| Bilgi Toplama |')
        print(kirmizi+'=================')
        print("")
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Ip Tracer')
        print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+' Ip Info')
        print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+' Seeker')
        print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+' Grabcam')
        print(yesil+' [ '+rr+ '5' +yesil+' ] '+mavi+'->'+sari+' Sherlock')
        print(yesil+' [ '+rr+ '6' +yesil+' ] '+mavi+'->'+sari+' UserRecon')
        print(yesil+' [ '+rr+ '7' +yesil+' ] '+mavi+'->'+sari+' Exiftool')
        print(yesil+' [ '+rr+ '8' +yesil+' ] '+mavi+'->'+sari+' Harvester')
        print(yesil+' [ '+rr+ '9' +yesil+' ] '+mavi+'->'+sari+' Ipcs')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Ana Menü')
        ony = input(yesil+"\n\n [+] İşlem No: ")
        if ony == "1":
            pass
        elif ony == "2":
            pass
        elif ony == "3":
            pass
        elif ony == "4":
            pass
        elif ony == "5":
            pass
        elif ony == "6":
            pass
        elif ony == "7":
            pass
        elif ony == "8":
            pass
        elif ony == "9":
            pass
        elif ony == "99":
            arac_kurulumları()
        elif ony == "00":
            ana_menu()
    elif secim == "2":#Sızma ve Sömürü
        print(kirmizi+'===================')
        print(rr+     '| Sızma Ve Sömürü |')
        print(kirmizi+'===================')
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'Metasploit')
        print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+'Malicious')
        print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+'ApkTool')
        print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+'Ngrok')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+'\n [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+'Ana Menü')
        s = input(yesil+"\n\n[+] İşlem No: ")
        if s == "1":
            pass
            #os.system("pkg install metasploit -y && python termux.py")
        elif s == "2":
            os.system("cd $HOME && git clone https://github.com/TheSploit/Sploit-Malicious && cd Sploit-Malicious && pip2 install -r requirements.txt && cd $HOME && cd Mrxwai && python termux.py ")
        elif s == "3":
            pass
            #os.system("")
        elif s == "4":
            pass
            #os.system("")
        elif s == "5":
            pass
            #os.system("")
        elif s == "99":
            pass
            #os.system("")
        elif s == "00":
            pass
            #os.system("")




    elif secim == "3":#Web Uygulamaları
        pass

    elif secim == "4":#Dos & DDoS
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'Golden Eye')
        print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+'Hammer')
        print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+'Xerxes')
        print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+'Hulk')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+'\n [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+'Ana Menü')

    elif secim == "5":#Sms Spam
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'Impulse')
        print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+'Reborn')
        print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+'Tbomb')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+'\n [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+'Ana Menü')

    elif secim == "6":#Sosyal Medya
            print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'Hidden Eye')
            print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'Shell Phish')
            print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'Social Phish')
            print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'Black Eye')
            print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'Weeman')
            print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
            print(sari+'\n [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+'Ana Menü')

    elif secim == "7":#İşletim Sistemleri
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Ubuntu')
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Debian')
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Kali Linux')
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Kali Nethunter')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+'\n [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Ana Menü')
        opt = input(yesil+'İşlem No : ')
        if opt == "1":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh && cd $HOME && cd Mrxwai && python termux.py ")


        elif opt == "2":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh && cd $HOME && cd Mrxwai && python termux.py")
        elif opt == "3":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh && cd $HOME && cd Mrxwai && python termux.py")
        elif opt == "4":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh && cd $HOME && cd Mrxwai && python termux.py")

    elif secim == "8":#Terminal Özelleştirme
        os.system("clear && toilet -f mono12 -F metal MRXWAI")
        print(kirmizi+'=================')
        print(rr+     '| Özelleştirme  |')
        print(kirmizi+'=================')
        print(yesil+'\n [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'Z-shell')
        #print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'')
        #print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+'Ana Menü')
        opt = input(yesil+'\n\n[+] İşlem No: ')
        if opt == "1":
            os.system("cd $HOME   cd $HOME && cd Mrxwai && python termux.py ")
            os.system("git clone https://github.com/khansaad1275/termux-ohmyzsh")
            os.system("cd termux-ohmyzsh")
            os.system("chmod +x *")
            os.system("cd $HOME")
            os.system("python yeni.py")

        elif opt == "99":
            arac_kurulumları()
        elif opt == "00":
            ana_menu()

    elif secim == "9":#Ekstra Tuşlar
        os.system("""mkdir $HOME/.termux/ ;echo "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]" >> $HOME/.termux/termux.properties && termux-reload-settings && sleep 1 && logout""")

    elif secim == "99":#Ana Menüye Dön
        ana_menu()

    elif secim == "00":#Kapat
        kapat()

def iletisim():
    os.system("clear && toilet -f mono12 -F metal MRXWAI")
    print(rr+"""
Buradan Soru Ve İstekleriniz İçin Ulaşabilirsiniz :""")
    print(sari+"""

        [+] Instagram -> umutbektas25
        [+] Telegram  -> Mrxwai
        [+] Mail      -> umutbektas25@gmail.com
        [+] Discord   ->""")
    input(yesil+"\n\nGeri Dönmek İçin Enter'a Basınız!")

def kapat():
    os.system("\ncowsay Görüşmek Üzere")
    time.sleep(0.50)
    exit()

def ana_menu():
    os.system("clear && toilet -f mono12 -F metal MRXWAI")
    print(beyaz +
"""Bu program Umut Bektaş tarafından sizlerin daha KOLAY ve bir o
kadar da ETKİLİ biçimde telefon üzerinden hacking işlemlerini
kavrayıp pratikte kullanabilmeyi öğrenmeniz için yazıldı.
Hiç bir sorumluluk tarafımca kabullenilemez!""")
    print("""

    """)
    print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Temel Linux Komutları')
    print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+' Temel Python Kodları')
    print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+' Paket Kurulumları')
    print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+' Araç Kurulumları')
    print(yesil+' [ '+rr+ '5' +yesil+' ] '+mavi+'->'+sari+' İletişim')
    print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Çıkış')


#Döngü Bölümü
while True:
    ana_menu()
    onay = input(yesil+"\n\n [+] İşlem No: ")
    if onay == "1":
        linux_komutları()

    elif onay == "2":
        python_kodları()
    elif onay == "3":
        paket_kurulumları()
    elif onay == "4":
        arac_kurulumları()
    elif onay == "5":
        iletisim()
    elif onay == "99":
        kapat()
    else :
        print(mavi+"\nHatalı Giriş Yaptınız!")
        time.sleep(1)
