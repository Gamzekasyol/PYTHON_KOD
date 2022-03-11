#LİSTE/SET

liste=['a','b','c','d','e','a']
#listeye f eklemek istiyoruz

liste=liste+ ['f']
print(liste)

#ya da APPEND komutu
liste.append('g')
print(liste)


#POP= Listenin son elemanını gösterir.
print(liste.pop())
print(liste.pop(4))

sayilar=['4','7','3','9','4','8']

#SORT=Sayıları sıralar.
sayilar.sort()
print(sayilar)

#REVERSE=Sayıları tersten sıralar.
sayilar.reverse()
print(sayilar)

sayilar=['4','7','3','9','4','8']
#SET=Listedeki tekrar eden elemanları çıkarır.
print(set(sayilar))

#TUPLE=Değiştirlemez tipteki listeler.
liste=['a','b','c','d','e','a']
tup=("a","b","c","d","e","a")



#ÖRN                             
liste[0]=12312            
print(liste)

#tup(0)=123
#print(tup)

#Count=Kaç tane olduğunu gösterir.
x=tup.count("a")
print(x)

#İndex=kacıncı indexste olduğun gösterir.
y=tup.index("b")
print(y)




#DİCTİONARY

dict1={"isim":"mesut","yas":32,"lokasyon":"berlin"}
print(dict1)


dict2= {
    "isim":"mesut",
    "yas":32,
    "dogdugu_sehir":"istanbul",
    "yasadigi_sehir":"berlin"}
print(dict2)


dict3= {
    "isim":"mesut",
    "yas":32,
    "lokasyon":{
         "dogdugu_sehir":"istanbul",
          "yasadigi_sehir":"berlin"}
} 
print(dict3)

print(dict2["yas"])
#print(dict3["lokasyon","yasadıgı_sehir"])   bul bunu

print(dict2.keys())
print(dict2.values())
print(dict2.items())


























