metin="Gamze K"

print(metin[3])
print(metin[2:]) #iki dahil
print(metin[:4]) #dört dahil değil
print(metin[2:4])
print(metin[1:4:2]) # iki iki atlar

print(len(metin)) #len=uzunluk
#CONCATENATİON(birleştirme) ÖZELLİĞİ

print(metin + "öğren")
print(metin.upper()) #upper= büyük
print(metin.lower()) #lower= küçük
print(metin.split()) #splt=ayırma

#ilk ve son harfi alma
for i in metin.split():
     print(i[0],end="")
