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

Bütün uygulamaları yükle -> hepsi
Sistemi güncelle -> güncelle

Ekranı temizle -> temizle

Yardım -> hakkında
Programdan çık -> çık

"""
os.system('clear')
print(ascii_art)
print(açılış_konuşmam)
# Değişken bloğu
a = "" #girilen komut
b = "" #kullanıcı kontrol (E/H)
# Değişken bloğu

while True:

    a = input('\n     Komutları görmek için \'komutlar\' yazın\nKomut: ')
    if a == "çık":
        os.system('clear')
        b = input('Çıkmak istediğinden emin misin? (E/H)\nCevap: ')
        if b == "E":
            os.system('clear')
            print('...', '...', '...', 'Program kapatılıyor', '...', '...', '...', sep='\n')
            exit()
        elif b == "H":
            os.system('clear')
            print('Çıkmak istemediğine sevindim program çalışmaya devam edecek')
        else:
            print('Geçersiz işlem:', b, 'program çalışacak')
    elif a == "komutlar":
        os.system('clear')
        print(komutlar)
    elif a == "multiload":
        try:
            os.system('clear')
            print('\nMultiload Indicator kuruluyor\n')
            os.system('sudo apt-get install indicator-multiload --yes')
            os.system('clear')
            print('\nMultiload Indicator başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nMultiload Indicator başarıyla KURULAMADI')
    elif a == "sensors":
        try:
            os.system('clear')
            print('\nSıcaklık ölçer kuruluyor\n')
            os.system('sudo apt-get install lm-sensors --yes')
            os.system('clear')
            print('\nSıcaklık ölçer başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nSıcaklık ölçer başarıyla KURULAMADI')
    elif a == "speedtest":
        try:
            os.system('clear')
            print('\nİnternet hızı ölçer kuruluyor\n')
            os.system('sudo apt-get install speedtest-cli --yes')
            os.system('clear')
            print('\nİnternet hızı başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nİnternet hızı başarıyla KURULAMADI')
    elif a == "vnstat":
        try:
            os.system('clear')
            print('\nVeri trafiği ölçer kuruluyor\n')
            os.system('sudo apt-get install vnstat --yes')
            os.system('clear')
            print('\nVeri trafiği başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nVeri trafiği başarıyla KURULAMADI')
    elif a == "traceroute":
        try:
            os.system('clear')
            print('\nVeri takip edici kuruluyor\n')
            os.system('sudo apt-get install traceroute --yes')
            os.system('clear')
            print('\nVeri takip edici başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nVeri takip edici başarıyla KURULAMADI')
    elif a == "tor":
        try:
            os.system('clear')
            print('\nTor modülleri kuruluyor\n')
            os.system('sudo apt-get install tor --yes')
            os.system('clear')
            print('\nTor modüllerü başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nTor modülleri başarıyla KURULAMADI')
    elif a == "proxychains":
        try:
            os.system('clear')
            print('\nProxy değiştirici kuruluyor\n')
            os.system('sudo apt-get install proxychains --yes')
            os.system('clear')
            print('\nProxy değiştirici başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nProxy değiştirici başarıyla KURULAMADI')
    elif a == "spotify":
        try:
            os.system('clear')
            print('Yetki anahtarları giriliyor')
            os.system('sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886')
            print('\nUbuntu kütüphanesine ekleniyor')
            os.system('echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list')
            print('\nKütüphane güncelleniyor')
            os.system('sudo apt-get update')
            print('\nSpotify kurulumuna başlanıyor')
            os.system('sudo apt-get install spotify-client --yes')
            os.system('clear')
            print('\nSpotify başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nSpotify başarıyla KURULAMADI')
    elif a == "torrent":
        try:
            os.system('clear')
            print('\nTorrent istemcisi kuruluyor\n')
            os.system('sudo apt-get install qbittorrent --yes')
            os.system('clear')
            print('\nTorrent istemcisi başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nTorrent istemcisi başarıyla KURULAMADI')
    elif a == "filezilla":
        try:
            os.system('clear')
            print('\nFTP istemcisi kuruluyor\n')
            os.system('sudo apt-get install filezilla --yes')
            os.system('clear')
            print('\nFTP istemcisi başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nFTP istemcisi başarıyla KURULAMADI')
    elif a == "torrent":
        try:
            os.system('clear')
            print('\nIRC sohbet istemcisi kuruluyor\n')
            os.system('sudo apt-get install hexchat --yes')
            os.system('clear')
            print('\nIRC sohbet istemcisi başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nIRC sohbet istemcisi başarıyla KURULAMADI')

    elif a == "güncelle":
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

    elif a == "hepsi":
        try:
            os.system('clear')
            print('\nMultiload Indicator kuruluyor\n')
            os.system('sudo apt-get install indicator-multiload --yes')
            os.system('clear')
            print('\nMultiload Indicator başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nMultiload Indicator başarıyla KURULAMADI')
        try:
            os.system('clear')
            print('\nSıcaklık ölçer kuruluyor\n')
            os.system('sudo apt-get install lm-sensors --yes')
            os.system('clear')
            print('\nSıcaklık ölçer başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nSıcaklık ölçer başarıyla KURULAMADI')
        try:
            os.system('clear')
            print('\nİnternet hızı ölçer kuruluyor\n')
            os.system('sudo apt-get install speedtest-cli --yes')
            os.system('clear')
            print('\nİnternet hızı başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nİnternet hızı başarıyla KURULAMADI')
        try:
            os.system('clear')
            print('\nVeri trafiği ölçer kuruluyor\n')
            os.system('sudo apt-get install vnstat --yes')
            os.system('clear')
            print('\nVeri trafiği başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nVeri trafiği başarıyla KURULAMADI')
        try:
            os.system('clear')
            print('\nVeri takip edici kuruluyor\n')
            os.system('sudo apt-get install traceroute --yes')
            os.system('clear')
            print('\nVeri takip edici başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nVeri takip edici başarıyla KURULAMADI')
        try:
            os.system('clear')
            print('\nTor modülleri kuruluyor\n')
            os.system('sudo apt-get install tor --yes')
            os.system('clear')
            print('\nTor modüllerü başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nTor modülleri başarıyla KURULAMADI')
        try:
            os.system('clear')
            print('\nProxy değiştirici kuruluyor\n')
            os.system('sudo apt-get install proxychains --yes')
            os.system('clear')
            print('\nProxy değiştirici başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nProxy değiştirici başarıyla KURULAMADI')
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
        try:
            os.system('clear')
            print('\nTorrent istemcisi kuruluyor\n')
            os.system('sudo apt-get install qbittorrent --yes')
            os.system('clear')
            print('\nTorrent istemcisi başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nTorrent istemcisi başarıyla KURULAMADI')
        try:
            os.system('clear')
            print('\nFTP istemcisi kuruluyor\n')
            os.system('sudo apt-get install filezilla --yes')
            os.system('clear')
            print('\nFTP istemcisi başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nFTP istemcisi başarıyla KURULAMADI')
        try:
            os.system('clear')
            print('\nIRC sohbet istemcisi kuruluyor\n')
            os.system('sudo apt-get install hexchat --yes')
            os.system('clear')
            print('\nIRC sohbet istemcisi başarıyla kuruldu\n')
        except:
            os.system('clear')
            print('\nIRC sohbet istemcisi başarıyla KURULAMADI')

    elif a == "temizle":
        os.system('clear')
    elif a == "hakkında":
        os.system('clear')
        print(ascii_art)
        print(açılış_konuşmam)
    else:
        os.system('clear')
        print('\nDostum çok yanlış şeyler girdin anlamadım')
        print('Böyle acayip komutlarım yok ->', a)
