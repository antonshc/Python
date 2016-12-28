#!/usr/bin/python3
import urllib.request
import time
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

# KONTROL BLOK BAŞLANGICI
def açılış_kontrol():
    os.system('clear')
    print('\nSistem kontrol ediliyor')
    time.sleep(1)
    print('\nİnternet bağlantısı kontrol ediliyor')
    internet_kontrol(durum_bağlı="Sistemin internete bağlı durumda",
                     durum_kopuk="Sistemin internet bağlantısı bulunamadı\nTekrar deneniyor",
                     sonsuz_döngü="Hayır")
    print('\nProgram açılışına devam ediliyor')
    time.sleep(3)
    os.system('clear')
    print('''\

        Tüm kontroller yapıldı program açılıyor
    Açılıyor: 3
    ''')
    time.sleep(1)
    os.system('clear')
    print('''\

        Tüm kontroller yapıldı program açılıyor
    Açılıyor: 2
    ''')
    time.sleep(1)
    os.system('clear')
    print('''\

        Tüm kontroller yapıldı program açılıyor
    Açılıyor: 1
    ''')
    time.sleep(1)
    os.system('clear')
    hakkında()
def internet_kontrol(
        durum_bağlı,
        durum_kopuk,
        sonsuz_döngü):
    while True: # İnternet kontrol döngüsü
        try:
            time.sleep(2)
            site = urllib.request.urlopen('https://calap.co')
            print('\n'+durum_bağlı)
            break
        except urllib.error.URLError:
            if sonsuz_döngü == "Hayır":
                for tur in (1, 2, 3):
                    print('\n' + durum_kopuk)
                    time.sleep(1.5)
                # İnternetsiz Şekilde çalışmasi için bu aralıktaki kod bloğunu kaldırın
                print('''\
                    Program internetsizlik sebebiyle öldü
                    Sistem internete bağlanınca tekrar deneyin
                ''')
                exit()
                # İnternetsiz Şekilde çalışmasi için bu aralıktaki kod bloğunu kaldırın
                break
            else:
                print('\n' + durum_kopuk)
                time.sleep(1.5) # # # #  adaw #
# KONTROL BLOK SONU

açılış_kontrol()

komutlar = """\

Multiload Indicator -> multiload            |   Bütün uygulamaları yükle -> hepsi
Sıcaklık ölçer -> sensors                   |   Sistemi güncelle -> güncelle
İnternet hızı ölçer -> speedtest            |   Ekranı temizle -> temizle
Veri trafiği ölçer -> vnstat                |
Veri takip edici -> traceroute              |   Program hakkında -> hakkında
Tor modülleri -> tor                        |   Programdan çık -> çık
Proxy değiştirici -> proxychains            |   Programı kapatıp yeniden aç -> yenile
Spotify -> spotify                          |
Bittorrent istemcisi -> torrent             |
FTP istemcisi -> filezilla                  |
IRC sohbet istemcisi -> hexchat             |
Ağ tarayıcı -> netdiscover                  |
Medya oynatıcı -> vlc                       |
Skype -> skype                              |
Git istemcisi -> gitkraken                  |

""" # Buraya yeni özellikleri eklemeyi unutma, eklemezsen ekranda görünmez
def geçici_dizin_oluştur():
    os.system('clear')
    print('\nGeçici çalışma dizini oluşturuluyor')
    print('Çalışma dizini değiştiriliyor-> /temp\n')
    os.system('sudo mkdir temp')
def geçici_dizin_sil():
    os.system('sudo rmdir temp')
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
def yükle_vlc():
    try:
        os.system('clear')
        print('\nVideo oynatıcı kuruluyor\n')
        os.system('sudo apt-get install vlc --yes')
        os.system('clear')
        print('\nVideo oynatıcı başarıyla kuruldu\n')
    except:
        os.system('clear')
        print('\nVideo oynatıcı başarıyla KURULAMADI\n')
def yükle_skype():
    try:
        geçici_dizin_oluştur()
        print('\nSkype indiriliyor\n')
        os.system('cd temp && sudo wget https://download.skype.com/linux/skype-ubuntu-precise_4.3.0.37-1_i386.deb -O skype.deb')
        print('\nSkype kurulumuna başlanıyor')
        os.system('cd temp && sudo dpkg -i skype.deb')
        print('\nSkype başarıyla kuruldu\n')
        print('İndirilen dosyalar temizleniyor...\n')
        os.system('cd temp && sudo rm skype.deb')
        geçici_dizin_sil()
    except:
        os.system('clear')
        print('\nSkype başarıyla KURULAMADI\n')
def yükle_gitkraken():
    try:
        geçici_dizin_oluştur()
        print('\nGitKraken indiriliyor\n')
        os.system('cd temp && sudo wget https://release.gitkraken.com/linux/gitkraken-amd64.deb -O gitkraken.deb')
        print('\nGitKraken kurulumuna başlanıyor')
        os.system('cd temp && sudo dpkg -i gitkraken.deb')
        print('\nGitKraken başarıyla kuruldu\n')
        print('İndirilen dosyalar temizleniyor...\n')
        os.system('cd temp && sudo rm gitkraken.deb')
        geçici_dizin_sil()
    except:
        os.system('clear')
        print('\nSkype başarıyla KURULAMADI\n')
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
def platform_kapat_aç():
    os.system('clear')
    print('\nUFS Platformu kapatılıyor')
    time.sleep(3)
    os.system('python3 UFS_yenile.py')
    exit() #

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
    elif a == "vlc":
        yükle_vlc()
    elif a == "skype":
        yükle_skype()
    elif a == "gitkraken":
        yükle_gitkraken()
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
        yükle_vlc()
        yükle_skype()
        yükle_gitkraken()
    elif a == "temizle":
        os.system('clear')
    elif a == "hakkında":
        hakkında()
    elif a == "yenile":
        platform_kapat_aç()
    else:
        os.system('clear')
        print('\nDostum çok yanlış şeyler girdin anlamadım')
        print('Böyle acayip komutlarım yok ->', a)