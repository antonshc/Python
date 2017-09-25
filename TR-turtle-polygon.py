#!/usr/bin/python3
# -*- coding: utf-8 -*-
import turtle
kenar_uzunlugu = 0
kenar_sayisi = 0

kenar_uzunlugu = int(input("Kenar uzunluğu: "))  # girilen kenar uzunluğu değerini integer olarak değişkene atar
kenar_sayisi = int(input("Kenar sayısı: "))      # girilen kenar sayısı değerini integer olarak değişkene atar

sc = turtle.Screen()                             # pencere oluşturur
tu = turtle.Turtle()                             # kaplumbağayı oluşturur

sc.title("Muz Cumhuriyeti")                      # pencere başlığını değiştirir
sc.bgcolor("lightblue")                          # pencere arkaplan rengini değiştirir
tu.color("red")                                  # kaplumbağa rengini değiştirir

tu.penup()                                       # bu ve aşağıdaki 3 satır kaplumbağayı pencerede yeniden konumlandırır
tu.setx(-60)
tu.sety(-130)
tu.pendown()

try:                                             # aşağıdaki kodları çalıştırmayı dener
    for i in range(kenar_sayisi):                # girilen kenar sayısı kadar döngü oluşturur
        tu.forward(kenar_uzunlugu)               # girilen kenar uzunluğu kadar kaplumbağayı ilerletir
        tu.left(360 / kenar_sayisi)              # kaplumbağayı şeklin dış açısına göre döndürür
    print("\nKenar uzunluğu", str(kenar_uzunlugu), "birim olan", str(kenar_sayisi), "kenarlı bir şekil oluşturuldu.")
except:                                          # yukarıdaki kodlar hata verirse aşağıdakileri çalıştırır
    print("Program kapandı.")
    exit()
sc.exitonclick()                                 # pencerede bir yere tıklanıncaya kadar programın kapanmasını engeller