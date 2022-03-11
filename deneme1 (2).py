from tkinter import*


ekran=Tk()
ekran.title("gamze")
ekran.geometry("500x500")



label1=Label(text="Birinci sayı")
label1.place(x=30,y=10)

girdibir=Entry()
girdibir.place(x=100,y=10)

label2=Label(text="ikinci sayı")
label2.place(x=30,y=30)

girdiiki=Entry()
girdiiki.place(x=100,y=30)


sonuc=Label(text="sonuç=")
sonuc.place(x=120,y=10)

def topla():
    islem=int(girdibir.get())+int(girdiiki.get())
    sonuc["text"]=int(girdibir.get()),"+",int(girdiiki.get()),"=",islem

butonbir=Button(text="+",command=topla)
butonbir.place(x=30,y=50)
