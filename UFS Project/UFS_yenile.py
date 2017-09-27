#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import time
# UFS yeniden başlatma aracı
def UFS_yeniden_başlat():
    os.system('clear')
    print('\nUFS platformu yeniden başlatılıyor')
    time.sleep(3)
    print('\n\nSİSTEM YENİDEN BAŞLATMA\n\n')
    time.sleep(3)
    os.system('clear')
    print('''\

        Tüm kontroller yapıldı program yeniden başlatılıyor
    Başlıyor: 3
    ''')
    time.sleep(1)
    os.system('clear')
    print('''\

        Tüm kontroller yapıldı program yeniden başlatılıyor
    Başlıyor: 2
    ''')
    time.sleep(1)
    os.system('clear')
    print('''\

        Tüm kontroller yapıldı program yeniden başlatılıyor
    Başlıyor: 1
    ''')
    time.sleep(1)
    os.system('python3 UFS.py')
    exit()

UFS_yeniden_başlat()
