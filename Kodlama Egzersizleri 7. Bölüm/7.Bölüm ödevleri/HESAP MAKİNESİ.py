from tkinter import *
def yazı(x):
    a = len(ekran.get())
    ekran.insert(a,str(x))
    print(x)

hesap = 5
sayı1 = 0


def işlem(x):
    global hesap
    hesap = x
    global sayı1
    sayı1 = float(ekran.get())
    print(hesap)
    print(sayı1)
    ekran.delete(0,'end')

sayı2 = 0
def hesaplayıcı():
    global sayı2
    sayı2 = float(ekran.get())
    print(sayı2)
    global hesap
    işlemsonucu = 0
    if(hesap == 0):
        işlemsonucu = sayı1 + sayı2
    elif(hesap == 1):
        işlemsonucu = sayı1 - sayı2
    elif(hesap == 2):
        işlemsonucu = sayı1 * sayı2
    elif(hesap == 3):
        işlemsonucu = sayı1 / sayı2
    ekran.delete(0,'end')
    ekran.insert(0,str(işlemsonucu))

pencere = Tk()
pencere.wm_geometry("250x250")

ekran = Entry(font = "Verdana 14 bold",width =15 ,justify=RIGHT)
ekran.place(x = 20,y = 20)

b = []

for i in range(1,10):
    b.append(Button(text=str(i),font = "Verdana 14 bold",command = lambda x = i:yazı(x)))


sıra = 0


for i in range (0,3):
    for j in range (0,3):
        b[sıra].place(x = 20+j *50,y =50+i*50)
        sıra += 1

işlemler = []

for i in range(0,4):
    işlemler.append(Button(font ="Verdana 14 bold",width = 2,command = lambda x = i:işlem(x)))
işlemler[0]['text'] = "+"
işlemler[1]['text'] = "-"
işlemler[2]['text'] = "*"
işlemler[3]['text'] = "/"
for i in range(0,4):
    işlemler[i].place(x = 170,y = 50+50*i)

sıfır_butonu = Button(text = "0",font = "Verdana 14 bold",command = lambda x = 0:yazı(x))
sıfır_butonu.place(x=20 , y=200)

nokta_butonu = Button(text = ".",font = "Verdana 14 bold",width = 2,command = lambda x=".":yazı(x))
nokta_butonu.place(x=70 , y=200)

eşittir_butonu = Button(text = "=",fg = "ORANGE",font = "Verdana 14 bold",command=hesaplayıcı)
eşittir_butonu.place(x=120 , y=200)




pencere.mainloop()