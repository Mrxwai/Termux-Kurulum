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


os.system("clear")
print (yesil+"""
    __  ___                         _ 
   /  |/  /_____  ___      ______ _(_)
  / /|_/ / ___/ |/_/ | /| / / __ `/ / 
 / /  / / /  _>  < | |/ |/ / /_/ / /  
/_/  /_/_/  /_/|_| |__/|__/\__,_/_/                                        
       	""")
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
print(yesil+"\nKurulum Başladı!")
os.system("termux-setup-storage")
os.system("apt update -y && apt upgrade -y")
os.system("pkg update -y && pkg upgrade -y")
os.system("apt install tsu -y")
os.system("pkg install unstable-repo -y")
os.system("pkg install root-repo -y")
os.system("pkg install figlet -y")
os.system("pkg install cowsay -y")
os.system("apt install fish -y")
os.system("pkg install wget -y")
os.system("pkg install curl -y")
os.system("pkg install python")
os.system("pkg install python2")
os.system("pip install --upgrade pip")
os.system("python3 -m pip install --upgrade pip")
os.system("pip3 install one-lin3r")
os.system("pip3 install requests")
os.system("pip3 install wordlist")
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
os.system("pkg install man -y")
os.system("""mkdir $HOME/.termux/ ;echo "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]" >> $HOME/.termux/termux.properties && termux-reload-settings && sleep 1 &&logout""")
        
