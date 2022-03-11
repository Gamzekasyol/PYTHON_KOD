x=0

while x<10:
    print(x, "değeri 10 dan küçüktür.")
    x += 1

#.....................................................................

kullanici1 = {
    'ad': 'Ferhat',
    'soyad': 'Ibrik',
    'uzmanlik': ['Front-End']
}
kullanici2 = {
    'ad': 'Gokce',
    'soyad': 'Gün',
    'uzmanlik': ['Tasarim']
}
kullanici3 = {
    'ad': 'Mesut',
    'soyad': 'Gün',
    'uzmanlik': ['Front-End']
}

# Soru 1: Ferhat Ibrik Kullanicisinin uzmanlik alanlarini döndür
print(kullanici1["uzmanlik"])



kullanici_listesi = [kullanici1, kullanici2, kullanici3] 


# Soru 2: Front-end alanindaki uzmanlarin isimlerini döndür
for kullanici in kullanici_listesi:
    if kullanici["uzmanlik"]==["Front-End"]:
        print(kullanici["ad"])

    else:
        print("kullsnıcı bulunamadı")





# Soru 3: Mesut kullanicisi Yazilim ögrendi, bilgileri güncelle!
kullanici3["uzmanlik"].append("yazilim")
print(kullanici3)



# Soru 4: 1den fazla uzmanlik alani olan kullanicilari döndür (Hint: length)

for kullanici in kullanici_listesi:
    if len(kullanici["uzmanlik"])>1:
        print(kullanici)

kullanici_yaslari_listesi = [22, 34, 32]
# Soru 5: zip kullanarak iki listeyi birlestir ve yasi 30'dan az olan kullanicilar kimler?

for kullanici,yas in zip(kullanici_listesi,kullanici_yaslari_listesi):
        if yas<30:
            print(kullanici)



# Soru 6: deger isimli degiskene atanan sayinin asal olup olmadigini söyle!
# Hint Asal sayi: kendinden ve 1'den baska böleni olmayan sayilar örnek 2,3,5,7

deger=7
x=deger-1
while x>1:
    if deger%x==0:
        print(deger,"sayısı asal sayı değil.")
        break
    else:
        x-=1
else:
    print(deger,"sayısı asal  sayıdır.")




#def bes_dondur():
#   return(5)
#print(bes_dondur())

 


#buyuk_sayi_dondur(5,10)
#def metin_yaz(a,b):
 #   buyuk_sayi=buyuk_sayi_dondur(a,b)
  #  sablon_metin=(buyuk_sayi,"daha büyük sayıdır.")
   # print(sablon_metin)
#print(metin_yaz(5,10))


def bes_bastir():
    print(5)



a=bes_bastir()
print(a)



def bes_dondur():
    return(5)
b=bes_dondur()
print(b)














    

