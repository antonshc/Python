#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import time
import os
MAVI, KIRMIZI, BEYAZ, SARI, MACENTA, YEŞİL, SON = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'  # RENKLER

# ANA FONKSİYON
# Yeni özellikleri buraya ekle
def ana_döngü():
    try:
        while True:  # sonsuz döngü
            a = ""  # girilen komut
            b = ""  # kullanıcı kontrol (E/H)
            a = input('\n     {3}Komutları görmek için \'komutlar\' yazın\n{1}Komut: '.format(YEŞİL, SARI, KIRMIZI, BEYAZ, MAVI, SON))

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

            if a == "çık" or a == "q":
                programdan_çık()
            elif a == "komutlar":
                os.system('clear')
                print(komutlar.format(YEŞİL, SARI, KIRMIZI, BEYAZ, SON))
            elif a == "1":
                yükle_multiload()
            elif a == "2":
                yükle_sensors()
            elif a == "3":
                yükle_speedtest()
            elif a == "4":
                yükle_vnstat()
            elif a == "5":
                yükle_traceroute()
            elif a == "6":
                yükle_tor()
            elif a == "7":
                yükle_proxychains()
            elif a == "8":
                yükle_spotify()
            elif a == "9":
                yükle_torrent()
            elif a == "10":
                yükle_filezilla()
            elif a == "11":
                yükle_hexchat()
            elif a == "12":
                yükle_netdiscover()
            elif a == "13":
                yükle_vlc()
            elif a == "14":
                yükle_skype()
            elif a == "15":
                yükle_gitkraken()
            elif a == "16":
                yükle_megasync()
            elif a == "17":
                yükle_youtube_dl()
            elif a == "18":
                yükle_atom_editör()
            elif a == "19":
                yükle_opera42_stable()
            elif a == "20":
                yükle_steam()
            elif a == "666":
                os.system('clear')
                b = input('Güncellendikten sonra sistem kapatılsın mı? (E/H)\nCevap: ')
                if b == "E" or b == "e":
                    sistem_güncelle(güncellendikten_sonra_sistemi_kapat='evet')
                elif b == "H" or b == "h":
                    sistem_güncelle(güncellendikten_sonra_sistemi_kapat='hayır')
                else:
                    print('Geçersiz işlem:', b, 'program çalışacak')
            elif a == "999":
                sistem_güncelle(güncellendikten_sonra_sistemi_kapat='hayır')
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
                yükle_opera42_stable()
                yükle_steam()
                yükle_atom_editör()
                yükle_youtube_dl()
                yükle_megasync()
            elif a == "0":
                os.system('clear')
            elif a == "h":
                hakkında()
            elif a == "000":
                platform_kapat_aç()
            else:
                os.system('clear')
                print('\n{0}Dostum çok yanlış şeyler girdin anlamadım'.format(KIRMIZI))
                print('{0}Böyle acayip komutlarım yok ->'.format(BEYAZ), a)
    except KeyboardInterrupt:
        kontrol_c(nerede="ortasında")

# KLAVYEDEN ÇIKIŞ KONTROLÜ
def kontrol_c(nerede):
    try:
        if nerede == "açılışta":
            os.system('clear')
            b = input('Sanırım çıkacak gibisin doğru mu? (E/H)')
            if b == "E" or b == "e":
                os.system('clear')
                time.sleep(1.5)
                exit()
            elif b == "H" or b == "h":
                açılış_kontrol()
            else:
                os.system('clear')
                print('Dostum çok enteresan işler yapıyosun')
                print('Karşı önlem olarak programı baştan açıyorum')
                time.sleep(1.5)
                açılış_kontrol()
        elif nerede == "ortasında":
            os.system('clear')
            b = input('Sanırım çıkacak gibisin doğru mu? (E/H)')
            if b == "E" or b == "e":
                os.system('clear')
                time.sleep(1.5)
                exit()
            elif b == "H" or b == "h":
                ana_döngü()
            else:
                os.system('clear')
                print('Dostum çok enteresan işler yapıyosun')
                print('Karşı önlem olarak programı baştan açıyorum')
                time.sleep(1.5)
                açılış_kontrol()
    except KeyboardInterrupt:
        os.system('clear')
        print('E sende yeter ama artık çıkacaksan çık tamam')
        exit()
    except:
        os.system('clear')
        print('Bişeyler çok ters gitti ama anlamadım\nPlatformu baştan açıyorum')
        time.sleep(2)
        açılış_kontrol()

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

@Version: 0.1.4
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
    try:
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
    except KeyboardInterrupt:
        kontrol_c(nerede="açılışta")
def internet_kontrol(
        durum_bağlı,
        durum_kopuk,
        sonsuz_döngü):
    # İnternet kontrolünde bug var
    # İnternet olduğu halde bağlı değil uyarısı veriyor
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
                    time.sleep(1)
                # İnternetsiz Şekilde çalışmasi için bu aralıktaki kod bloğunu kaldırın
                print('''\
                    Program internetsizlik sebebiyle çökebilir
                    Sistem internete bağlanınca tekrar deneyin
                ''')
                # exit()
                # İnternetsiz Şekilde çalışmasi için bu aralıktaki kod bloğunu kaldırın
                break
            else:
                print('\n' + durum_kopuk)
                time.sleep(1.5)
        except KeyboardInterrupt:
            kontrol_c(nerede="açılışta")
# KONTROL BLOK SONU

açılış_kontrol()  # Programı başlatan komut

komutlar = """\

{4}[{0}1{4}]  {1}Multiload indicator         {4}|   [{2}999{4}] Hepsini yükle
{4}[{0}2{4}]  {1}Sıcaklık ölçer              {4}|   [{2}666{4}] {0}Sistemi güncelle
{4}[{0}3{4}]  {1}İnternet hızı ölçer         {4}|   [{3}0{4}]   {1}Ekranı temizle
{4}[{0}4{4}]  {1}Veri trafiği ölçer          {4}|
{4}[{0}5{4}]  {1}Veri takip edici            {4}|   [{1}h{4}]   Hakkında
{4}[{0}6{4}]  {1}Tor modülleri               {4}|   [{3}000{4}] {1}Kapat/Aç
{4}[{0}7{4}]  {1}Proxy değiştirici           {4}|   [{2}q{4}]   ÇIK
{4}[{0}8{4}]  {1}Spotify                     {4}|
{4}[{0}9{4}]  {1}qBittorrent                 {4}|   [{0}15{4}]  {1}GitKraken
{4}[{0}10{4}] {1}Filezilla                   {4}|   [{0}16{4}]  {1}MegaSync
{4}[{0}11{4}] {1}Hexchat                     {4}|   [{0}17{4}]  {1}Youtube indirici
{4}[{0}12{4}] {1}Netdiscover                 {4}|   [{0}18{4}]  {1}Atom editör
{4}[{0}13{4}] {1}VLC player                  {4}|   [{0}19{4}]  {1}Opera tarayıcı v42
{4}[{0}14{4}] {1}Skype                       {4}|   [{0}20{4}]  {1}Steam platformu

"""  # Buraya yeni özellikleri eklemeyi unutma, eklemezsen ekranda görünmez
def geçici_dizin_oluştur():
    os.system('clear')
    print('\nGeçici çalışma dizini oluşturuluyor')
    print('Çalışma dizini değiştiriliyor-> /temp\n')
    os.system('sudo mkdir temp')
def geçici_dizin_sil():
    print('\nİndirilen dosyalar \'temp\' adlı klasörde depolanmıştır.')
    # os.system('cd temp && sudo rm * && cd ..')
    # os.system('sudo rmdir temp')
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
        #  os.system('cd temp && sudo rm skype.deb')  //indirilen dosyaları kullanıcı kendisi siler
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
        #  os.system('cd temp && sudo rm gitkraken.deb')  /indirilenleri kullanıcı kendisi siler
        geçici_dizin_sil()
    except:
        os.system('clear')
        print('\nGitKraken başarıyla KURULAMADI\n')
def yükle_megasync():
    try:
        geçici_dizin_oluştur()
        print('\nMegaSync indiriliyor\n')
        os.system('cd temp && sudo wget https://mega.nz/linux/MEGAsync/xUbuntu_16.04/amd64/megasync-xUbuntu_16.04_amd64.deb -O mega.deb')
        print('\nMegaSync kurulumuna başlanıyor')
        os.system('cd temp && sudo dpkg -i mega.deb')
        print('\nMegaSync başarıyla kuruldu\n')
        print('İndirilen dosyalar temizleniyor...\n')
        #  os.system('cd temp && sudo rm mega.deb')  //indirilenleri kullanıcı kendisi siler
        geçici_dizin_sil()
    except:
        os.system('clear')
        print('\nMegaSync başarıyla KURULAMADI\n')
def yükle_youtube_dl():
    try:
        os.system('clear')
        print('\nYoutube video indirici kuruluyor\n')
        os.system('sudo apt-get install youtube-dl --yes')
        os.system('clear')
        print('\nYoutube video indirici kuruldu\n')
    except:
        os.system('clear')
        print('\nYoutube video indirici başarıyla KURULAMADI\n')
def yükle_atom_editör():
    try:
        geçici_dizin_oluştur()
        print('\nAtom Editör indiriliyor\n')
        os.system('cd temp && sudo wget https://atom-installer.github.com/v1.13.0/atom-amd64.deb -O atom.deb')
        print('\nAtom Editör kurulumuna başlanıyor')
        os.system('cd temp && sudo dpkg -i atom.deb')
        print('\nAtom Editör başarıyla kuruldu\n')
        print('İndirilen dosyalar temizleniyor...\n')
        #  os.system('cd temp && sudo rm atom.deb')  //indirilenleri kullanıcı kendisi siler
        geçici_dizin_sil()
    except:
        os.system('clear')
        print('\nAtom Editör başarıyla KURULAMADI\n')
def yükle_opera42_stable():
    try:
        geçici_dizin_oluştur()
        print('\nOpera Tarayıcı sürüm: 42 indiriliyor\n')
        os.system('cd temp && sudo wget https://download1.operacdn.com/pub/opera/desktop/42.0.2393.137/linux/opera-stable_42.0.2393.137_amd64.deb -O opera_v42.deb')
        print('\nOpera Tarayıcı sürüm: 42 kurulumuna başlanıyor')
        os.system('cd temp && sudo dpkg -i opera_v42.deb')
        print('\nOpera Tarayıcı sürüm: 42 başarıyla kuruldu\n')
        print('İndirilen dosyalar temizleniyor...\n')
        #  os.system('cd temp && sudo rm opera_v42.deb')  /indirilenleri kullanıcı kendisi siler
        geçici_dizin_sil()
    except:
        os.system('clear')
        print('\nOpera Tarayıcı sürüm: 42 başarıyla KURULAMADI\n')
def yükle_steam():
    try:
        geçici_dizin_oluştur()
        print('\nSteam indiriliyor\n')
        os.system('cd temp && sudo wget http://repo.steampowered.com/steam/archive/precise/steam_latest.deb -O steam.deb')
        print('\nSteam kurulumuna başlanıyor')
        os.system('cd temp && sudo dpkg -i steam.deb')
        print('\nSteam başarıyla kuruldu\n')
        print('İndirilen dosyalar temizleniyor...\n')
        #  os.system('cd temp && sudo rm steam.deb')  /indirilenleri kullanıcı kendisi siler
        geçici_dizin_sil()
    except:
        os.system('clear')
        print('\nSteam başarıyla KURULAMADI\n')

def sistem_güncelle(güncellendikten_sonra_sistemi_kapat):
    if güncellendikten_sonra_sistemi_kapat == 'evet':
        try:
            os.system('clear')
            print('\nSistem güncellemesi başlatılıyor\n')
            print('Gereksiz şeyler temizleniyor\n')
            os.system('sudo apt-get autoclean --yes')
            os.system('sudo apt-get autoremove --yes')
            print('\nGüncelleme modülleri başlatılıyor\n')
            os.system('sudo apt-get update --yes')
            os.system('sudo apt-get upgrade --yes')
            print('\nGüncelleme işlemleri başarıyla tamamlamlandı\n')
            print('GÜNCELLEME TAMAMLANDI SİSTEM KAPATILIYOR')
            os.system('sudo shutdown -h now')
        except:
            os.system('clear')
            print('\nGüncelleme işlemleri başarıyla TAMAMLANAMADI')
    elif güncellendikten_sonra_sistemi_kapat == 'hayır':
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
    exit()


ana_döngü()