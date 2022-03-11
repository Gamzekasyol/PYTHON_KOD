from tkinter import*


ekran=Tk()
ekran.title()
ekran.geometry("500x500")

x=Label(text="birinci sayı")
x.place(x=20,y=30)

x=Entry()
x.place(x=80,y=30)

y=Label(text="ikinci sayı")
y.place(x=20,y=50)

y=Entry()
y.place(x=80,y=50)

sonuc=Label(text="sonuc")
sonuc.place(x=60,y=100)


def hesap():
    son=int(x.get())+int(y.get())
    sonuc["text"]=son 


buton=Button(text="hesapla",command=hesap)
buton.place(x=60,y=80)
