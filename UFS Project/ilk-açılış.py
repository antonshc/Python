#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

def gerekli_kütüphaneler():  # bunlar olmadan program düzgün çalışmayabilir
    os.system('sudo apt-get install python3-pip --yes')
    os.system('sudo pip install requests')
    os.system('sudo pip install netinterfaces')
    os.system('sudo pip3 install requests')
    os.system('sudo pip3 install netifaces')
    os.system('sudo pip3 install netinterfaces')

gerekli_kütüphaneler()

os.system("sudo python3 UFS.py")

exit()
