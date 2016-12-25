#!/usr/bin/python3

import os

ascii_art = """\
              _________
            / MUSTAFA /|
           /  ÇALAP  / |_
          / GURURLA /  //|
         /  SUNAR  /  ////|
        |   _ _    | 8o////|
        | /'// )_  |   8///|
        |/ // // ) |   8o///|
        / // // //,|  /  8//|
       / // // /// | /   8//|
      / // // ///__|/    8//|
     /.(_)// /// |       8///|
    (_)' `(_)//| |       8////|___________
   (_) /_\ (_)'| |        8///////////////
   (_) \"/ (_)'|_|         8/////////////
    (_)._.(_) d' Hb         8oooooooopb'
      `(_)'  d'  H`b
            d'   `b`b
           d'     H `b
          d'      `b `b
         d'           `b
        d'             `b

"""
açılış_konuşmam = """\
Bu yazılım Mustafa ÇALAP tarafından Ubuntu kurulum sonrası gerekli olan uygulamaları yüklemesi için kodlanmıştır.
Yazılımın sürümünü github.com/nexus38 adresinden kontrol edebilirsiniz.

--- BAZI İŞLEMLER İÇİN YÖNETİCİ YETKİSİ GEREKEBİLİR ---

@Version: 0.0.1
@Author: Mustafa ÇALAP
@Github: nexus38
@Website: https://calap.co

"""
def hakkında():
    os.system('clear')
    print(ascii_art)
    print(açılış_konuşmam)
hakkında()

komutlar = """\

Multiload Indicator -> multiload
Sıcaklık ölçer -> sensors
İnternet hızı ölçer -> speedtest
Veri trafiği ölçer -> vnstat
Veri takip edici -> traceroute
Tor modülleri -> tor
Proxy değiştirici -> proxychains
Spotify -> spotify
Bittorrent istemcisi -> torrent
FTP istemcisi -> filezilla
IRC sohbet istemcisi -> hexchat
Ağ tarayıcı -> netdiscover

Bütün uygulamaları yükle -> hepsi
Sistemi güncelle -> güncelle
Ekranı temizle -> temizle


Hakkında -> hakkında
Programdan çık -> çık

"""

def yükle_multiload():
    try:
        os.system('clear')
        print('\nMultiload Indicator kuruluyor\n')
        os.system('sudo apt-get install indicator-multiload --yes')
        os.system('clear')
        print('\nMultiload Indicator başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nMultiload Indicator başarıyla KURULAMADI')
def yükle_sensors():
    try:
        os.system('clear')
        print('\nSıcaklık ölçer kuruluyor\n')
        os.system('sudo apt-get install lm-sensors --yes')
        os.system('clear')
        print('\nSıcaklık ölçer başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nSıcaklık ölçer başarıyla KURULAMADI')
def yükle_speedtest():
    try:
        os.system('clear')
        print('\nİnternet hızı ölçer kuruluyor\n')
        os.system('sudo apt-get install speedtest-cli --yes')
        os.system('clear')
        print('\nİnternet hızı başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nİnternet hızı başarıyla KURULAMADI')
def yükle_vnstat():
    try:
        os.system('clear')
        print('\nVeri trafiği ölçer kuruluyor\n')
        os.system('sudo apt-get install vnstat --yes')
        os.system('clear')
        print('\nVeri trafiği başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nVeri trafiği başarıyla KURULAMADI')
def yükle_traceroute():
    try:
        os.system('clear')
        print('\nVeri takip edici kuruluyor\n')
        os.system('sudo apt-get install traceroute --yes')
        os.system('clear')
        print('\nVeri takip edici başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nVeri takip edici başarıyla KURULAMADI')
def yükle_tor():
    try:
        os.system('clear')
        print('\nTor modülleri kuruluyor\n')
        os.system('sudo apt-get install tor --yes')
        os.system('clear')
        print('\nTor modüllerü başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nTor modülleri başarıyla KURULAMADI')
def yükle_proxychains():
    try:
        os.system('clear')
        print('\nProxy değiştirici kuruluyor\n')
        os.system('sudo apt-get install proxychains --yes')
        os.system('clear')
        print('\nProxy değiştirici başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nProxy değiştirici başarıyla KURULAMADI')
def yükle_spotify():
    try:
        os.system('clear')
        print('Yetki anahtarları giriliyor')
        os.system(
            'sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886')
        print('\nUbuntu kütüphanesine ekleniyor')
        os.system(
            'echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list')
        print('\nKütüphane güncelleniyor')
        os.system('sudo apt-get update')
        print('\nSpotify kurulumuna başlanıyor')
        os.system('sudo apt-get install spotify-client --yes')
        os.system('clear')
        print('\nSpotify başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nSpotify başarıyla KURULAMADI')
def yükle_torrent():
    try:
        os.system('clear')
        print('\nTorrent istemcisi kuruluyor\n')
        os.system('sudo apt-get install qbittorrent --yes')
        os.system('clear')
        print('\nTorrent istemcisi başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nTorrent istemcisi başarıyla KURULAMADI')
def yükle_filezilla():
    try:
        os.system('clear')
        print('\nFTP istemcisi kuruluyor\n')
        os.system('sudo apt-get install filezilla --yes')
        os.system('clear')
        print('\nFTP istemcisi başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nFTP istemcisi başarıyla KURULAMADI')
def yükle_hexchat():
    try:
        os.system('clear')
        print('\nIRC sohbet istemcisi kuruluyor\n')
        os.system('sudo apt-get install hexchat --yes')
        os.system('clear')
        print('\nIRC sohbet istemcisi başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nIRC sohbet istemcisi başarıyla KURULAMADI')
def yükle_netdiscover():
    try:
        os.system('clear')
        print('\nAğ tarayıcı kuruluyor\n')
        os.system('sudo apt-get install netdiscover --yes')
        os.system('clear')
        print('\nAğ tarayıcı başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nAğ tarayıcı başarıyla KURULAMADI\n')
def sistem_güncelle():
    try:
        os.system('clear')
        print('\nSistem güncellemesi başlatılıyor\n')
        print('Gereksiz şeyler temizleniyor\n')
        os.system('sudo apt-get autoclean --yes')
        os.system('sudo apt-get autoremove --yes')
        print('\nGüncelleme modülleri başlatılıyor\n')
        os.system('sudo apt-get upgrade --yes')
        os.system('sudo apt-get update --yes')
        print('\nGüncelleme işlemleri başarıyla tamamlamlandı\n')
    except:
        os.system('clear')
        print('\nGüncelleme işlemleri başarıyla TAMAMLANAMADI')

while True:  # sonsuz döngü
    a = ""  # girilen komut
    b = ""  # kullanıcı kontrol (E/H)
    a = input('\n     Komutları görmek için \'komutlar\' yazın\nKomut: ')
    def programdan_çık():
        os.system('clear')
        b = input('Çıkmak istediğinden emin misin? (E/H)\nCevap: ')
        if b == "E" or b == "e":
            os.system('clear')
            print("""\
            ***
                ***
                    ***
                        KAPANIŞ SEKANSI BAŞLATILIYOR
                    ***
                ***
            ***
                        TEKRAR GÖRÜŞMEK ÜZERE DOSTUM""")
            exit()
        elif b == "H" or b == "h":
            os.system('clear')
            print('Çıkmak istemediğine sevindim program çalışmaya devam edecek')
        else:
            print('Geçersiz işlem:', b, 'program çalışacak')

    if a == "çık":
        programdan_çık()
    elif a == "komutlar":
        os.system('clear')
        print(komutlar)
    elif a == "multiload":
        yükle_multiload()
    elif a == "sensors":
        yükle_sensors()
    elif a == "speedtest":
        yükle_speedtest()
    elif a == "vnstat":
        yükle_vnstat()
    elif a == "traceroute":
        yükle_traceroute()
    elif a == "tor":
        yükle_tor()
    elif a == "proxychains":
        yükle_proxychains()
    elif a == "spotify":
        yükle_spotify()
    elif a == "torrent":
        yükle_torrent()
    elif a == "filezilla":
        yükle_filezilla()
    elif a == "hexchat":
        yükle_hexchat()
    elif a == "netdiscover":
        yükle_netdiscover()
    elif a == "güncelle":
        sistem_güncelle()
    elif a == "hepsi":
        sistem_güncelle()
        yükle_filezilla()
        yükle_hexchat()
        yükle_multiload()
        yükle_netdiscover()
        yükle_proxychains()
        yükle_sensors()
        yükle_speedtest()
        yükle_spotify()
        yükle_tor()
        yükle_torrent()
        yükle_traceroute()
        yükle_vnstat()
    elif a == "temizle":
        os.system('clear')
    elif a == "hakkında":
        hakkında()
    else:
        os.system('clear')
        print('\nDostum çok yanlış şeyler girdin anlamadım')
        print('Böyle acayip komutlarım yok ->', a)