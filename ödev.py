from tkinter import*
import math

pencere=Tk()
pencere.title("HESAP MAKİNESİ")
pencere.geometry("500x500")


sayibir=Label(text="1. sayı=")
sayibir.place(x=40,y=40)

girdibir=Entry()
girdibir.place(x=140,y=40)

sayiiki=Label(text="2. sayı=")
sayiiki.place(x=40,y=60)


girdiiki=Entry()
girdiiki.place(x=140,y=60)

sonuc=Label(text="SONUÇ=")
sonuc.place(x=100,y=80)



def topla():
    print("toplama işlemi")
    islem=int(girdibir.get())+int(girdiiki.get())
    print(islem)
    sonuc["text"]=int(girdibir.get()),"+",int(girdiiki.get()),"=",islem
    
toplama=Button(text="+",command=topla)
toplama.place(x=60,y=100)



def cikar():
    print("çıkarma işlemi")
    islem=int(girdibir.get())-int(girdiiki.get())
    print(islem)
    sonuc["text"]=int(girdibir.get()),"-",int(girdiiki.get()),"=",islem
    
cıkarma=Button(text="-",command=cikar)
cıkarma.place(x=40,y=100)

def bol():
    print("bölme işlemi")
    islem=int(girdibir.get())/int(girdiiki.get())
    print(islem)
    sonuc["text"]=int(girdibir.get()),"/",int(girdiiki.get()),"=",islem
bolme=Button(text="/",command=bol)
bolme.place(x=80,y=100)


def carp():
    print("çarpma  işlemi")
    islem=int(girdibir.get())*int(girdiiki.get())
    print(islem)
    sonuc["text"]=int(girdibir.get()),"x",int(girdiiki.get()),"=",islem
carpma=Button(text="x",command=carp)
carpma.place(x=100,y=100)


def sin():
    print("sin işlemi")
    islem=math.sin(math.radians(int(girdibir.get())))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"sin","=",islem
sinus=Button(text="sin ",command=sin)
sinus.place(x=130,y=130)

def cos():
    print("cos işlemi")
    islem=math.cos(math.radians(int(girdibir.get())))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"cos","=",islem
cosinus=Button(text="cos",command=cos)
cosinus.place(x=40,y=130)

def tan():
    print("tan işlemi")
    islem=math.tan(math.radians(int(girdibir.get())))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"tan","=",islem
tanjant=Button(text="tan",command=tan)
tanjant.place(x=70,y=130)

def cot():
    print("cot işlemi")
    islem=math.cot(math.radians(int(girdibir.get())))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"cot","=",islem
cotanjant=Button(text="cot",command=cot)
cotanjant.place(x=100,y=130)

def us():
    print("üssü  işlemi")
    islem=math.pow(int(girdibir.get()),int(girdiiki.get()))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"^",int(girdiiki.get()),"=",islem
ussu=Button(text="xʸ",command=us)
ussu.place(x=140,y=190)

def kok():
    print("kök işlemi")
    islem=math.sqrt(int(girdibir.get()))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"√","=",islem
kok=Button(text="√",command=kok)
kok.place(x=140,y=100)

def pi():
    print("pi işlemi")
    islem=math.pi
    print(islem)
    sonuc["text"]=int(girdibir.get()),"π","=",islem
pi=Button(text="π",command=pi)
pi.place(x=120,y=100)

def faktoriel():
    print("faktöriel işlemi")
    islem=math.factorial(int(girdibir.get()))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"!","=",islem
faktoriel=Button(text="!",command=faktoriel)
faktoriel.place(x=40,y=160)

def log():
    print("logaritma işlemi")
    islem=math.log(int(girdibir.get()))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"log","=",islem
log=Button(text="log",command=log)
log.place(x=60,y=160)

def log10():
    print("logaritma işlemi")
    islem=math.log10(int(girdibir.get()))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"log10","=",islem
log10=Button(text="log10",command=log10)
log10.place(x=90,y=160)

def log2():
    print("logaritma işlemi")
    islem=math.log2(int(girdibir.get()))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"log2","=",islem
log2=Button(text="log2",command=log2)
log2.place(x=130,y=160)

def exp():
    print("exp işlemi")
    islem=math.exp(int(girdibir.get()))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"exp",int(girdiiki.get()),"=",islem
exp=Button(text="exp",command=exp)
exp.place(x=40,y=190)

def mutlak():
    print("mutlak değer işlemi")
    islem=math.fabs(int(girdibir.get()))
    print(islem)
    sonuc["text"]=int(girdibir.get())," IxI","=",islem
mutlak=Button(text="IxI",command=mutlak)
mutlak.place(x=70,y=190)

def kesirlisayi():
    print("kesirli sayı  işlemi")
    islem=(1/(int(girdibir.get())))
    print(islem)
    sonuc["text"]=int(girdibir.get())," 1/x","=",islem
kesirlisayi=Button(text="1/x",command=kesirlisayi)
kesirlisayi.place(x=90,y=190)

def e():
    print("kesirli sayı  işlemi")
    islem=math.e
    print(islem)
    sonuc["text"]=int(girdibir.get()),"e","=",islem
e=Button(text="e",command=e)
e.place(x=120,y=190)

def kare():
    print("kare alma işlemi")
    islem=(int(girdibir.get())**(2))
    print(islem)
    sonuc["text"]=int(girdibir.get()),"**",2,"=",islem
kare=Button(text="x²",command=kare)
kare.place(x=40,y=220)



mainloop()

