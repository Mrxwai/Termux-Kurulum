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
    print(sari+ """

------------
| uname -a | -> Çekirdek hakkında genel bilgi edinmemizi sağlar
------------

----------
| whoami |  ->  Hangi yetki ile işlem yaptığımızı gösterir
----------

---------
| clear |  -> Ekranı temizler
---------

-------
| pwd |  -> Ekrana bulunduğunuz dizinin çıktısını verir
-------

------
| ls |  -> Dizini listeler
------

------
| cd |  -> Dizine geçiş yapar. "cd .." ise bir önceki dizine geçer
------

------
| cp |  -> Dosyayı kopyalar
------

------
| mv |  -> Dosyayı taşır
------

---------
| mkdir |  -> Dosyayı oluşturur
---------

------
| rm |  -> Dosyayı siler
------

------------
| chmod +x |  -> Çalıştırma düzenleme ve okuma yetkisi verir
------------

------------
| ifconfig |  -> Yerel ip adresini gösterir
------------

------------
| route -n |  -> Modeminizin yerel ağ adresini gösterir
------------

--------
| nano |  ->  Metin düzenleme ve kod yazma komutudur
--------

-------
| man |   -> detaylı yardım alma komutudur
-------
""")

    input(yesil+"\n\nGeri dönmek İçin Enter'a Basınız!")

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
    os.system("pip2 install wafwoof")
    os.system("pip2 install mechanize")
    os.system("pip2 install requests")
    os.system("pip2 install termcolor")
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
    print("""
Önemli: Lütfen, önce paket kurulumları bölümünden termux için gerekli olan paketlerin kurulumunu yapınız!
    """)
    print(yesil+'\n [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Bilgi Toplama')
    print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+' Sızma ve Sömürü')
    print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+' Web Uygulamaları')
    print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+' Dos & DDos')
    print(yesil+' [ '+rr+ '5' +yesil+' ] '+mavi+'->'+sari+' Sms Spam')
    print(yesil+' [ '+rr+ '6' +yesil+' ] '+mavi+'->'+sari+' Phising')
    print(yesil+' [ '+rr+ '7' +yesil+' ] '+mavi+'->'+sari+' İşletim Sistemleri')
    print(yesil+' [ '+rr+ '8' +yesil+' ] '+mavi+'->'+sari+' Terminal Özelleştirme')
    print(yesil+' [ '+rr+ '9' +yesil+' ] '+mavi+'->'+sari+' Ekstra Tuşlar')
    print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
    print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Çıkış')
    secim = input(yesil+"\n\n [+] İşlem No: ")
    if secim == "1":#Bilgi Toplama
        os.system("clear && toilet -f mono12 -F metal MRXWAI")
        print(kirmizi+'=================')
        print(kirmizi+   '|'+rr+' Bilgi Toplama '+kirmizi+'|')
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
            os.system("cd $HOME && git clone https://github.com/rajkumardusad/IP-Tracer.git && cd IP-Tracer && chmod +x * && bash install.sh && cd $HOME && cd Mrxwai && python termux.py")

        elif ony == "2":
            os.system("git clone https://github.com/vpphacker/ipinfo.git && cd ipinfo && chmod +x * && bash install.sh && cd $HOME && cd Mrxwai && python termux.py")

        elif ony == "3":
            os.system("cd $HOME && git clone https://github.com/thewhiteh4t/seeker.git && cd seeker/ && chmod 777 * && bash termux_install.sh && cd $HOME && cd Mrxwai && python termux.py")

        elif ony == "4":
            os.system("cd $HOME && git clone https://github.com/noob-hackers/grabcam && cd grabcam && chmod 777 * && pip install lolcat && cd $HOME && cd Mrxwai && python termux.py")

        elif ony == "5":
            os.system("cd $HOME && git clone https://github.com/sherlock-project/sherlock && cd sherlock && chmod +x * && python3 -m pip install -r requirements.txt && cd $HOME && cd Mrxwai && python termux.py")

        elif ony == "6":
            os.system("cd $HOME && git clone https://github.com/issamelferkh/userrecon && cd userrecon && chmod +x * && cd $HOME && cd Mrxwai && python termux.py")

        elif ony == "7":
            os.system("cd $HOME && apt install perl wget gzip make && wget https://sno.phy.queensu.ca/~phil/exiftool/Image-ExifTool-11.19.tar.gz && gzip -dc Image-ExifTool-*.tar.gz | tar -xf -&& perl Makefile.PL && make install && cd $HOME && cd Mrxwai && python termux.py")

        elif ony == "8":
            os.system("cd $HOME && git clone https://github.com/laramies/theHarvester && cd theHarvester && chmod +x * && python3 -m pip install pipenv && python3 -m pip install pipenv && cd $HOME && cd Mrxwai && python termux.py")

        elif ony == "9":
            os.system("cd $HOME && git clone https://github.com/kancotdiq/ipcs && cd ipcs && chmod +x * && cd $HOME && cd Mrxwai && python termux.py")

        elif ony == "99":
            arac_kurulumları()
        elif ony == "00":
            ana_menu()


    elif secim == "2":#Sızma ve Sömürü
        os.system("clear && toilet -f mono12 -F metal MRXWAI")
        print(kirmizi+'===================')
        print(kirmizi+  '|'+rr+' Sızma ve Sömürü '+kirmizi+'|')
        print(kirmizi+'===================')
        print(yesil+'\n\n [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Metasploit')
        print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+' Malicious')
        print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+' ApkTool')
        print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+' Ngrok')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Ana Menü')
        s = input(yesil+"\n\n [+] İşlem No: ")
        if s == "1":
            os.system("pkg install metasploit -y && python termux.py")
        elif s == "2":
            os.system("cd $HOME && git clone https://github.com/TheSploit/Sploit-Malicious && cd Sploit-Malicious && chmod +x * && pip2 install -r requirements.txt && cd $HOME && cd Mrxwai && python termux.py ")

        elif s == "3":
            os.system("cd $HOME && git clone https://github.com/Lexiie/Termux-Apktool && cd Termux-Apktool && chmod x * && dpkg -i apktool_2.3.4_all.deb && cd $HOME && cd Mrxwai && python termux.py")

        elif s == "4":
            pass

        elif s == "99":
            arac_kurulumları()
        elif s == "00":
            ana_menu()

    elif secim == "3":#Web Uygulamaları
        os.system("clear && toilet -f mono12 -F metal MRXWAI")
        print(kirmizi+'====================')
        print(kirmizi+  '|'+rr+' Web Uygulamaları '+kirmizi+'|')
        print(kirmizi+'====================')
        print(yesil+'\n [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Waf Woof ')
        print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+' Red Hawk ')
        print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+' Recon-Dog ')
        print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+' Pure Blood ')
        print(yesil+' [ '+rr+ '5' +yesil+' ] '+mavi+'->'+sari+' Optiva-Framework ')
        print(yesil+' [ '+rr+ '6' +yesil+' ] '+mavi+'->'+sari+' Ow-Scan ')
        print(yesil+' [ '+rr+ '7' +yesil+' ] '+mavi+'->'+sari+' Admin King ')
        print(yesil+' [ '+rr+ '8' +yesil+' ] '+mavi+'->'+sari+' Sublist3r ')
        print(yesil+' [ '+rr+ '8' +yesil+' ] '+mavi+'->'+sari+' XG-Dork ')
        print(yesil+' [ '+rr+ '8' +yesil+' ] '+mavi+'->'+sari+' Sqlmap ')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Ana Menü')
        a = input(yesil+"\n\n [+] İşlem No: ")
        if a == "1":
            os.system("pip2 install wafw00f && python termux.py")

        elif a == "2":
            os.system("cd $HOME && git clone https://github.com/Tuhinshubhra/RED_HAWK && cd RED_HAWK && chmod +x * && cd $HOME && cd Mrxwai && python termux.py")

        elif a == "3":
            os.system("cd $HOME && git clone https://github.com/UltimateHackers/ReconDog && cd ReconDog && chmod +x * && cd $HOME && cd Mrxwai && python termux.py")

        elif a == "4":
            os.system("cd $HOME && git clone https://github.com/shakenetwork/pureblood && cd pureblood && chmod +x * && pip install -r requirements.txt && cd Mrxwai && python termux.py")

        elif a == "5":
            os.system("cd $HOME && git clone https://github.com/joker25000/Optiva-Framework && cd Optiva-Framework && chmod +x * && bash installer.sh && cd Mrxwai && python termux.py")

        elif a == "6":
            os.system("cd $HOME && git clone https://github.com/Gameye98/OWScan && cd OWScan && chmod +x * && cd Mrxwai && python termux.py")

        elif a == "7":
            os.system("cd $HOME && git clone https://github.com/vpphacker/Adminking.git && cd Adminking  &&  chmod +x * &&  cd $HOME && cd Mrxwai && python termux.py")

        elif a == "8":
            os.system("cd $HOME && git clone https://github.com/aboul3la/Sublist3r && cd Sublist3r &&  chmod +x * &&  cd $HOME && cd Mrxwai && python termux.py")

        elif a == "8":
            os.system("cd $HOME && git clone https://github.com/E4rr0r4/XGDork.git && cd XGDork &&  chmod 777 * && cd $HOME && cd Mrxwai && python termux.py")

        elif a == "9":
            os.system("cd $HOME && git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev && cd sqlmap && chmod +x * && cd Mrxwai && python termux.py")

        elif a == "99":
            arac_kurulumları()
        elif a == "00":
            ana_menu()

    elif secim == "4":#Dos & DDoS
        os.system("clear && toilet -f mono12 -F metal MRXWAI")
        print(kirmizi+'==============')
        print(kirmizi+  '|'+rr+' DoS & DDoS '+kirmizi+'|')
        print(kirmizi+'==============')
        print(yesil+'\n [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Golden Eye')
        print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+' Hammer')
        print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+' Xerxes')
        print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+' Hulk')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Ana Menü')
        b = input(yesil+"\n\n [+] İşlem No: ")
        if b == "1":
            os.system("cd $HOME && git clone https://github.com/jseidl/GoldenEye && cd GoldenEye chmod +x * && cd $HOME && cd Mrxwai && python termux.py")

        elif b =="2":
            os.system("cd $HOME && git clone https://github.com/cyweb/hammer  && cd hammer && chmod +x * && cd $HOME && cd Mrxwai && python termux.py")

        elif b =="3":
            os.system("cd $HOME && git clone https://github.com/zanyarjamal/xerxes && cd xerxes && chmod +x * && cd $HOME && cd Mrxwai && python termux.py")

        elif b =="4":
            os.system("cd $HOME && git  clone https://github.com/grafov/hulk && cd hulk && chmod +x * && cd $HOME && cd Mrxwai && python termux.py")

        elif b == "99":
            arac_kurulumları()
        elif b == "00":
            ana_menu()

    elif secim == "5":#Sms Spam
        os.system("clear && toilet -f mono12 -F metal MRXWAI")
        print(kirmizi+'============')
        print(kirmizi+  '|'+rr+' Sms Spam '+kirmizi+'|')
        print(kirmizi+'============')
        print(yesil+'\n [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Impulse')
        print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+' Reborn')
        print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+' Tbomb')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Ana Menü')
        c = input(yesil+"\n\n [+] İşlem No: ")
        if c == "1":
            os.system("cd $HOME && git clone https://github.com/LimerBoy/Impulse && cd Impulse/ && chmod +x * && pip install -r requirements.txt && cd $HOME && cd Mrxwai && python termux.py")

        elif c == "2":
            os.system("git clone https://github.com/4nat/Reborn/ && cd Renorn/ && chmod +x * && cd $HOME && cd Mrxwai && python termux.py")

        elif c == "3":
            os.system("cd $HOME && git clone https://github.com/TheSpeedX/TBomb && cd TBomb  && chmod +x * && cd $HOME && cd Mrxwai && python termux.py")

        elif c == "99":
            arac_kurulumları()
        elif c == "00":
            ana_menu()

    elif secim == "6":#Phising
            os.system("clear && toilet -f mono12 -F metal MRXWAI")
            print(kirmizi+'===========')
            print(kirmizi+  '|'+rr+' Phising '+kirmizi+'|')
            print(kirmizi+'===========')
            print(yesil+'\n [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Hidden Eye')
            print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+' Shell Phish')
            print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+' Social Phish')
            print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+' Black Eye')

            print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
            print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Ana Menü')
            d = input(yesil+"\n\n [+] İşlem No: ")
            if d == "1":
                os.system("cd $HOME &&  && cd Mrxwai && python termux.py ")
            elif d == "2":
                os.system("cd $HOME && git clone https://github.com/kaankadirkilic/shellphish-1 && cd shellphish && bash shellphish.sh && cd Mrxwai && python termux.py ")
            elif d == "3":
                os.system("cd $HOME && git clone https://github.com/UndeadSec/SocialFish.git  && cd SocialFish && chmod +x * && pip2 install -r requirements.txt && cd Mrxwai && python termux.py ")
            elif d == "4":
                os.system("cd $HOME && git clone https://github.com/thelinuxchoice/blackeye  && cd blackeye  && chmod +x * && cd Mrxwai && python termux.py ")

            elif d == "99":
                arac_kurulumları()
            elif d == "00":
                ana_menu()

    elif secim == "7":#İşletim Sistemleri
        os.system("clear && toilet -f mono12 -F metal MRXWAI")
        print(kirmizi+'======================')
        print(kirmizi+  '|'+rr+' İşletim Sistemleri '+kirmizi+'|')
        print(kirmizi+'======================')
        print(yesil+'\n\n [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Ubuntu')
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Debian')
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Kali Linux')
        print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+' Kali Nethunter')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Ana Menü')
        opt = input(yesil+'\n\n [+] İşlem No: ')
        if opt == "1":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh && cd $HOME && cd Mrxwai && python termux.py")
        elif opt == "2":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh && cd $HOME && cd Mrxwai && python termux.py")

        elif opt == "3":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh && cd $HOME && cd Mrxwai && python termux.py")

        elif opt == "4":
            os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh && cd $HOME && cd Mrxwai && python termux.py")

        elif opt == "99":
            arac_kurulumları()
        elif opt == "00":
            ana_menu()

    elif secim == "8":#Terminal Özelleştirme
        os.system("clear && toilet -f mono12 -F metal MRXWAI")
        print(kirmizi+'================')
        print(kirmizi+  '|'+rr+' Özelleştirme '+kirmizi+'|')
        print(kirmizi+'================')
        print(yesil+'\n [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'Z-Shell')
        #print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'')
        #print(yesil+' [ '+rr+ '1' +yesil+' ] '+mavi+'->'+sari+'')
        print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Geri')
        print(sari+' [ '+rr+ '00' +sari+' ] '+mavi+'->'+rr+' Ana Menü')
        opt = input(yesil+'\n\n [+] İşlem No: ')
        if opt == "1":
            os.system("cd $HOME && git clone https://github.com/khansaad1275/termux-ohmyzsh && cd termux-ohmyzsh && chmod +x * && bash install.sh && cd $HOME && cd Mrxwai && python termux.py ")
        elif opt == "99":
            arac_kurulumları()
        elif opt == "00":
            ana_menu()

    elif secim == "9":#Ekstra Tuşlar
        os.system("""mkdir $HOME/.termux/ ;echo "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]" >> $HOME/.termux/termux.properties && termux-reload-settings && sleep 1 && exit""")

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
        """)
    input(yesil+"\nGeri Dönmek İçin Enter'a Basınız!")

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
    print(yesil+' [ '+rr+ '2' +yesil+' ] '+mavi+'->'+sari+' Paket Kurulumları')
    print(yesil+' [ '+rr+ '3' +yesil+' ] '+mavi+'->'+sari+' Araç Kurulumları')
    print(yesil+' [ '+rr+ '4' +yesil+' ] '+mavi+'->'+sari+' İletişim')
    print(sari+'\n [ '+rr+ '99' +sari+' ] '+mavi+'->'+rr+' Çıkış')


#Döngü Bölümü
while True:
    os.system("pkg install toilet -y")
    ana_menu()
    onay = input(yesil+"\n\n [+] İşlem No: ")
    if onay == "1":
        linux_komutları()

    elif onay == "2":
        paket_kurulumları()

    elif onay == "3":
        arac_kurulumları()

    elif onay == "4":
        iletisim()

    elif onay == "99":
        kapat()

    else :
        print(mavi+"\nHatalı Giriş Yaptınız!")
        time.sleep(1)
