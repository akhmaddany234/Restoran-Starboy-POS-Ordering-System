from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
import openpyxl
from datetime import datetime
import time
import locale

class PelangganMixin:
#---------------------------------------------------------------------------------program login pelanggan---------------------------------------------------------------------------------------------------------------------
    #membuat tampilan baru setelah mengeklik pelanggan, pelanggan diminta menginputkan user
    def loginpelanggan(self):
        self.tampilan.destroy()
        self.window_pelanggan = Tk()
        self.window_pelanggan.geometry('1280x680')
        
        img2 = Image.open("tampilan/nama customer.jpg")  
        self.pelangganlogin = ImageTk.PhotoImage(img2)
        label_gambarpelanggan = Label(self.window_pelanggan, image=self.pelangganlogin)
        label_gambarpelanggan.pack(pady=0)

        #memberi entry pada penginputan nama
        Label(self.window_pelanggan, text="NAMA:", font= ("Times New Roman",30,'bold'),bg='#FCF6DB',width=10,height=0).place(x=520, y=275)
        self.namapelanggan = StringVar()
        Entry(self.window_pelanggan,textvariable=self.namapelanggan,font=("Times New Roman",25),borderwidth=0,width=20,justify="center").place(x=473, y=340) #justify dibuat untuk tulisan dari tengah

        #membuat tombol ok
        self.pelanggan_ok = Button(self.window_pelanggan,text= 'OK',font = ("Times New Roman", 25, 'bold') ,width=5,height=1 , bg="#7D0B00",activebackground='#7D0B00',bd=0,fg="white",command=self.menumakanan,cursor='hand2')
        self.pelanggan_ok.place(x=587,y=410)



    #tampilan selanjutnya ketika pelanggan telah memasukkan username
    def menumakanan(self):
        self.window_pelanggan.destroy()
        self.slide5 = Tk()  #Toplevel(self.window_pelanggan)
        self.slide5.geometry('1280x680')
                
        img4 = Image.open("tampilan/5.jpg")
        self.tampilan_menumakanan = ImageTk.PhotoImage(img4)
        label_gambarmenumakanan = Label(self.slide5, image=self.tampilan_menumakanan)
        label_gambarmenumakanan.pack(pady=0)


        self.Jumlah_Makanan1 = Label(self.slide5,text=self.Makanan1,bg='#fffdd0')
        self.Jumlah_Makanan1.place(x=575-5,y=158)
        self.Jumlah_Makanan2 = Label(self.slide5,text=self.Makanan2,bg='#fffdd0')
        self.Jumlah_Makanan2.place(x=811-3,y=158)
        self.Jumlah_Makanan3 = Label(self.slide5,text=self.Makanan3,bg='#fffdd0')
        self.Jumlah_Makanan3.place(x=1111-15,y=158)
        self.Jumlah_Makanan4 = Label(self.slide5,text=self.Makanan4,bg='#fffdd0')
        self.Jumlah_Makanan4.place(x=130-10,y=392+8)
        self.Jumlah_Makanan5 = Label(self.slide5,text=self.Makanan5,bg='#fffdd0')
        self.Jumlah_Makanan5.place(x=358,y=392+10)
        self.Jumlah_Makanan6 = Label(self.slide5,text=self.Makanan6,bg='#fffdd0')
        self.Jumlah_Makanan6.place(x=575,y=392+10)
        self.Jumlah_Makanan7 = Label(self.slide5,text=self.Makanan7,bg='#fffdd0')
        self.Jumlah_Makanan7.place(x=809,y=392+10)  
        self.Jumlah_Makanan8 = Label(self.slide5,text=self.Makanan8,bg='#fffdd0')
        self.Jumlah_Makanan8.place(x=1110-12,y=392+10)
        self.Jumlah_Makanan9 = Label(self.slide5,text=self.Makanan9,bg='#fffdd0')
        self.Jumlah_Makanan9.place(x=130-10,y=392+250)

        
        # Plus_Button (Baris 1)
        ButPlus1 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan1)
        ButPlus1.place(x=612-9,y=158)
        ButPlus2 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan2)
        ButPlus2.place(x=846-6,y=158)
        ButPlus3 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan3)
        ButPlus3.place(x=1146-14,y=158)

        # Plus_Button (Baris 2)
        ButPlus4 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan4)
        ButPlus4.place(x=165-10,y=390+10)
        ButPlus5 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan5)
        ButPlus5.place(x=400,y=390+10)
        ButPlus6 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan6)
        ButPlus6.place(x=608,y=390+10)
        ButPlus7 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan7)
        ButPlus7.place(x=846,y=390+10)
        ButPlus8 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan8)
        ButPlus8.place(x=1146-12,y=390+10)
        ButPlus9 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan9)
        ButPlus9.place(x=165-10,y=390+250)
        
        # Minus_Button (Baris 1)
        ButMin1 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan1)
        ButMin1.place(x=530,y=158)
        ButMin2 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan2)
        ButMin2.place(x=765+3,y=158)
        ButMin3 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan3)
        ButMin3.place(x=1065-13,y=158)

        # MinButton (Baris 2)
        ButMin4 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan4)
        ButMin4.place(x=88-10,y=390+10)
        ButMin5 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan5)
        ButMin5.place(x=309,y=390+10)
        ButMin6 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan6)
        ButMin6.place(x=530,y=390+10)
        ButMin7 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan7)
        ButMin7.place(x=765,y=390+10)
        ButMin8 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan8)
        ButMin8.place(x=1065-12,y=390+10)
        ButMin9 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan9)
        ButMin9.place(x=88-10,y=390+250)

        ButNext = Button(self.slide5,text='SELANJUTNYA',width=17,height=1,borderwidth=0,bg='#ff8e84',command=self.Menu_Minuman,cursor='hand2',activebackground='#ff8e84')
        ButNext.place(x=1077, y=610)
        
    def tambah_Makanan1(self):
        self.Makanan1 += 1
        self.Jumlah_Makanan1['text'] = self.Makanan1
    def tambah_Makanan2(self):
        self.Makanan2 += 1
        self.Jumlah_Makanan2['text'] = self.Makanan2
    def tambah_Makanan3(self):
        self.Makanan3 += 1
        self.Jumlah_Makanan3['text'] = self.Makanan3
    def tambah_Makanan4(self):
        self.Makanan9 += 1
        self.Jumlah_Makanan4['text'] = self.Makanan4
    def tambah_Makanan5(self):
        self.Makanan5 += 1
        self.Jumlah_Makanan5['text'] = self.Makanan5
    def tambah_Makanan6(self):
        self.Makanan6 += 1
        self.Jumlah_Makanan6['text'] = self.Makanan6
    def tambah_Makanan7(self):
        self.Makanan7 += 1
        self.Jumlah_Makanan7['text'] = self.Makanan7
    def tambah_Makanan8(self):
        self.Makanan8 += 1
        self.Jumlah_Makanan8['text'] = self.Makanan8
    def tambah_Makanan9(self):
        self.Makanan9 += 1
        self.Jumlah_Makanan9['text'] = self.Makanan9

    def kurang_Makanan1(self):
        self.Makanan1 -= 1
        self.Jumlah_Makanan1['text'] = self.Makanan1
    def kurang_Makanan2(self):
        self.Makanan2 -= 1
        self.Jumlah_Makanan2['text'] = self.Makanan2
    def kurang_Makanan3(self):
        self.Makanan3 -= 1
        self.Jumlah_Makanan3['text'] = self.Makanan3
    def kurang_Makanan4(self):
        self.Makanan4 -= 1
        self.Jumlah_Makanan4['text'] = self.Makanan4
    def kurang_Makanan5(self):
        self.Makanan5 -= 1
        self.Jumlah_Makanan5['text'] = self.Makanan5
    def kurang_Makanan6(self):
        self.Makanan6 -= 1
        self.Jumlah_Makanan6['text'] = self.Makanan6
    def kurang_Makanan7(self):
        self.Makanan7 -= 1
        self.Jumlah_Makanan7['text'] = self.Makanan7
    def kurang_Makanan8(self):
        self.Makanan8 -= 1
        self.Jumlah_Makanan8['text'] = self.Makanan8
    def kurang_Makanan9(self):
        self.Makanan9 -= 1
        self.Jumlah_Makanan9['text'] = self.Makanan9

    def BackToMakanan(self):
        self.Slide6.destroy()
        self.slide5 = Tk()  #Toplevel(self.window_pelanggan)
        self.slide5.geometry('1280x680')
                
        img4 = Image.open("tampilan/5.jpg")
        self.tampilan_menumakanan = ImageTk.PhotoImage(img4)
        label_gambarmenumakanan = Label(self.slide5, image=self.tampilan_menumakanan)
        label_gambarmenumakanan.pack(pady=0)

         
        self.Jumlah_Makanan1 = Label(self.slide5,text=self.Makanan1,bg='#fffdd0')
        self.Jumlah_Makanan1.place(x=575-5,y=158)
        
        self.Jumlah_Makanan2 = Label(self.slide5,text=self.Makanan2,bg='#fffdd0')
        self.Jumlah_Makanan2.place(x=811-3,y=158)
        
        self.Jumlah_Makanan3 = Label(self.slide5,text=self.Makanan3,bg='#fffdd0')
        self.Jumlah_Makanan3.place(x=1111-15,y=158)

        # Inisiasi Makanan (Baris 2)
        
        self.Jumlah_Makanan4 = Label(self.slide5,text=self.Makanan4,bg='#fffdd0')
        self.Jumlah_Makanan4.place(x=130-10,y=392+8)
        
        self.Jumlah_Makanan5 = Label(self.slide5,text=self.Makanan5,bg='#fffdd0')
        self.Jumlah_Makanan5.place(x=358,y=392+10)
        
        self.Jumlah_Makanan6 = Label(self.slide5,text=self.Makanan6,bg='#fffdd0')
        self.Jumlah_Makanan6.place(x=575,y=392+10)
        
        self.Jumlah_Makanan7 = Label(self.slide5,text=self.Makanan7,bg='#fffdd0')
        self.Jumlah_Makanan7.place(x=809,y=392+10)
          
        self.Jumlah_Makanan8 = Label(self.slide5,text=self.Makanan8,bg='#fffdd0')
        self.Jumlah_Makanan8.place(x=1110-12,y=392+10)

        self.Jumlah_Makanan9 = Label(self.slide5,text=self.Makanan9,bg='#fffdd0')
        self.Jumlah_Makanan9.place(x=130-10,y=392+250)
        
        # Plus_Button (Baris 1)
        ButPlus1 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan1)
        ButPlus1.place(x=612-9,y=158)
        ButPlus2 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan2)
        ButPlus2.place(x=846-6,y=158)
        ButPlus3 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan3)
        ButPlus3.place(x=1146-14,y=158)

        # Plus_Button (Baris 2)
        ButPlus4 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan4)
        ButPlus4.place(x=165-10,y=390+10)
        ButPlus5 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan5)
        ButPlus5.place(x=400,y=390+10)
        ButPlus6 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan6)
        ButPlus6.place(x=608,y=390+10)
        ButPlus7 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan7)
        ButPlus7.place(x=846,y=390+10)
        ButPlus8 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan8)
        ButPlus8.place(x=1146-12,y=390+10)
        ButPlus9 = Button(self.slide5,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Makanan9)
        ButPlus9.place(x=165-10,y=390+250)
        
        # Minus_Button (Baris 1)
        ButMin1 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan1)
        ButMin1.place(x=530,y=158)
        ButMin2 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan2)
        ButMin2.place(x=765+3,y=158)
        ButMin3 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan3)
        ButMin3.place(x=1065-13,y=158)

        # MinButton (Baris 2)
        ButMin4 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan4)
        ButMin4.place(x=88-10,y=390+10)
        ButMin5 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan5)
        ButMin5.place(x=309,y=390+10)
        ButMin6 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan6)
        ButMin6.place(x=530,y=390+10)
        ButMin7 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan7)
        ButMin7.place(x=765,y=390+10)
        ButMin8 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan8)
        ButMin8.place(x=1065-12,y=390+10)
        ButMin9 = Button(self.slide5,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Makanan9)
        ButMin9.place(x=88-10,y=390+250)


        ButNext = Button(self.slide5,text='SELANJUTNYA',width=17,height=1,borderwidth=0,bg='#ff8e84',command=self.Menu_Minuman,cursor='hand2',activebackground='#ff8e84')
        ButNext.place(x=1077, y=610)
        
    def tambah_Makanan1(self):
        self.Makanan1 += 1
        self.Jumlah_Makanan1['text'] = self.Makanan1
    def tambah_Makanan2(self):
        self.Makanan2 += 1
        self.Jumlah_Makanan2['text'] = self.Makanan2
    def tambah_Makanan3(self):
        self.Makanan3 += 1
        self.Jumlah_Makanan3['text'] = self.Makanan3
    def tambah_Makanan4(self):
        self.Makanan4 += 1
        self.Jumlah_Makanan4['text'] = self.Makanan4
    def tambah_Makanan5(self):
        self.Makanan5 += 1
        self.Jumlah_Makanan5['text'] = self.Makanan5
    def tambah_Makanan6(self):
        self.Makanan6 += 1
        self.Jumlah_Makanan6['text'] = self.Makanan6
    def tambah_Makanan7(self):
        self.Makanan7 += 1
        self.Jumlah_Makanan7['text'] = self.Makanan7
    def tambah_Makanan8(self):
        self.Makanan8 += 1
        self.Jumlah_Makanan8['text'] = self.Makanan8
    def tambah_Makanan9(self):
        self.Makanan9 += 1
        self.Jumlah_Makanan9['text'] = self.Makanan9

    def kurang_Makanan1(self):
        self.Makanan1 -= 1
        self.Jumlah_Makanan1['text'] = self.Makanan1
    def kurang_Makanan2(self):
        self.Makanan2 -= 1
        self.Jumlah_Makanan2['text'] = self.Makanan2
    def kurang_Makanan3(self):
        self.Makanan3 -= 1
        self.Jumlah_Makanan3['text'] = self.Makanan3
    def kurang_Makanan4(self):
        self.Makanan4 -= 1
        self.Jumlah_Makanan4['text'] = self.Makanan4
    def kurang_Makanan5(self):
        self.Makanan5 -= 1
        self.Jumlah_Makanan5['text'] = self.Makanan5
    def kurang_Makanan6(self):
        self.Makanan6 -= 1
        self.Jumlah_Makanan6['text'] = self.Makanan6
    def kurang_Makanan7(self):
        self.Makanan7 -= 1
        self.Jumlah_Makanan7['text'] = self.Makanan7
    def kurang_Makanan8(self):
        self.Makanan8 -= 1
        self.Jumlah_Makanan8['text'] = self.Makanan8
    def kurang_Makanan9(self):
        self.Makanan9 -= 1
        self.Jumlah_Makanan9['text'] = self.Makanan9



    def Menu_Minuman(self):
        self.slide5.destroy()
        self.Slide6 = Tk()
        self.Slide6.title("Food")
        self.Slide6.geometry('1280x1080')
        self.Slide6.resizable(False,False)

        # Background
        background_image = Image.open("tampilan/6.jpg")
        bg_img = ImageTk.PhotoImage(background_image)
        
        bg_label = Label(self.Slide6, image=bg_img)
        bg_label.image = bg_img  
        bg_label.place(x=0, y=3) 
        
        # Inisiasi Hitungan (Baris 1)
        self.Jumlah_Minuman1 = Label(self.Slide6,text=self.Minuman1,bg='#fffdd0')
        self.Jumlah_Minuman1.place(x=575,y=167)
        self.Jumlah_Minuman2 = Label(self.Slide6,text=self.Minuman2,bg='#fffdd0')
        self.Jumlah_Minuman2.place(x=811,y=167)
        self.Jumlah_Minuman3 = Label(self.Slide6,text=self.Minuman3,bg='#fffdd0')
        self.Jumlah_Minuman3.place(x=1111,y=167)

        # Inisiasi Minuman (Baris 2)
        self.Jumlah_Minuman4 = Label(self.Slide6,text=self.Minuman4,bg='#fffdd0')
        self.Jumlah_Minuman4.place(x=130,y=392)
        self.Jumlah_Minuman5 = Label(self.Slide6,text=self.Minuman5,bg='#fffdd0')
        self.Jumlah_Minuman5.place(x=358,y=392)
        self.Jumlah_Minuman6 = Label(self.Slide6,text=self.Minuman6,bg='#fffdd0')
        self.Jumlah_Minuman6.place(x=575,y=392)
        self.Jumlah_Minuman7 = Label(self.Slide6,text=self.Minuman7,bg='#fffdd0')
        self.Jumlah_Minuman7.place(x=809,y=392)  
        self.Jumlah_Minuman8 = Label(self.Slide6,text=self.Minuman8,bg='#fffdd0')
        self.Jumlah_Minuman8.place(x=1110,y=392)

        # Plus_Button (Baris 1)
        ButPlus1 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman1)
        ButPlus1.place(x=612,y=165)
        ButPlus2 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman2)
        ButPlus2.place(x=846,y=165)
        ButPlus3 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman3)
        ButPlus3.place(x=1146,y=165)

        # Plus_Button (Baris 2)
        ButPlus4 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman4)
        ButPlus4.place(x=165,y=390)
        ButPlus5 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman5)
        ButPlus5.place(x=400,y=390)
        ButPlus6 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman6)
        ButPlus6.place(x=608,y=390)
        ButPlus7 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman7)
        ButPlus7.place(x=846,y=390)
        ButPlus8 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman8)
        ButPlus8.place(x=1146,y=390)
        
        # Minus_Button (Baris 1)
        ButMin1 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman1)
        ButMin1.place(x=530,y=165)
        ButMin2 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman2)
        ButMin2.place(x=765,y=165)
        ButMin3 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman3)
        ButMin3.place(x=1065,y=165)

        # Minus_Button (Baris 2)
        ButMin4 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman4)
        ButMin4.place(x=88,y=390)
        ButMin5 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman5)
        ButMin5.place(x=309,y=390)
        ButMin6 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman6)
        ButMin6.place(x=530,y=390)
        ButMin7 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman7)
        ButMin7.place(x=765,y=390)
        ButMin8 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman8)
        ButMin8.place(x=1065,y=390)

        # Next Button
        ButNext = Button(self.Slide6,text='SELANJUTNYA',width=17,height=1,borderwidth=0,bg='#ff8e84',command=self.Menu_Jajan,cursor='hand2',activebackground='#ff8e84')
        ButNext.place(x=1077, y=616)

        # Previous Button
        ButPrev = Button(self.Slide6,text='KEMBALI',width=17,height=1,borderwidth=0,bg='#ff8e84',cursor='hand2',command=self.BackToMakanan,activebackground='#ff8e84')
        ButPrev.place(x=70, y=617)



    def tambah_Minuman1(self):
        self.Minuman1 += 1
        self.Jumlah_Minuman1['text'] = self.Minuman1
    def tambah_Minuman2(self):
        self.Minuman2 += 1
        self.Jumlah_Minuman2['text'] = self.Minuman2
    def tambah_Minuman3(self):
        self.Minuman3 += 1
        self.Jumlah_Minuman3['text'] = self.Minuman3
    def tambah_Minuman4(self):
        self.Minuman4 += 1
        self.Jumlah_Minuman4['text'] = self.Minuman4
    def tambah_Minuman5(self):
        self.Minuman5 += 1
        self.Jumlah_Minuman5['text'] = self.Minuman5
    def tambah_Minuman6(self):
        self.Minuman6 += 1
        self.Jumlah_Minuman6['text'] = self.Minuman6
    def tambah_Minuman7(self):
        self.Minuman7 += 1
        self.Jumlah_Minuman7['text'] = self.Minuman7
    def tambah_Minuman8(self):
        self.Minuman8 += 1
        self.Jumlah_Minuman8['text'] = self.Minuman8

    def kurang_Minuman1(self):
        self.Minuman1 -= 1
        self.Jumlah_Minuman1['text'] = self.Minuman1
    def kurang_Minuman2(self):
        self.Minuman2 -= 1
        self.Jumlah_Minuman2['text'] = self.Minuman2
    def kurang_Minuman3(self):
        self.Minuman3 -= 1
        self.Jumlah_Minuman3['text'] = self.Minuman3
    def kurang_Minuman4(self):
        self.Minuman4 -= 1
        self.Jumlah_Minuman4['text'] = self.Minuman4
    def kurang_Minuman5(self):
        self.Minuman5 -= 1
        self.Jumlah_Minuman5['text'] = self.Minuman5
    def kurang_Minuman6(self):
        self.Minuman6 -= 1
        self.Jumlah_Minuman6['text'] = self.Minuman6
    def kurang_Minuman7(self):
        self.Minuman7 -= 1
        self.Jumlah_Minuman7['text'] = self.Minuman7
    def kurang_Minuman8(self):
        self.Minuman8 -= 1
        self.Jumlah_Minuman8['text'] = self.Minuman8


    def Menu_Jajan(self):

        self.Slide6.destroy()
        self.slide7 = Tk()
        self.slide7.title('Additional Food')
        self.slide7.geometry('1280x1080')
        self.slide7.resizable(False,False)
        # Background
        background_image = Image.open("tampilan/7.jpg")
        bg_img = ImageTk.PhotoImage(background_image)
        
        bg_label = Label(self.slide7, image=bg_img)
        bg_label.image = bg_img  
        bg_label.place(x=0, y=3) 

    
        # Inisiasi Hitungan (Baris 1)
        
        self.Jumlah_Jajan1 = Label(self.slide7,text=self.Jajan1,bg='#fffdd0')
        self.Jumlah_Jajan1.place(x=575,y=167)
        
        self.Jumlah_Jajan2 = Label(self.slide7,text=self.Jajan2,bg='#fffdd0')
        self.Jumlah_Jajan2.place(x=820,y=167)
        
        self.Jumlah_Jajan3 = Label(self.slide7,text=self.Jajan3,bg='#fffdd0')
        self.Jumlah_Jajan3.place(x=1111,y=167)

        # Inisiasi Jajan (Baris 2)
        
        self.Jumlah_Jajan4 = Label(self.slide7,text=self.Jajan4,bg='#fffdd0')
        self.Jumlah_Jajan4.place(x=130,y=392)
        
        self.Jumlah_Jajan5 = Label(self.slide7,text=self.Jajan5,bg='#fffdd0')
        self.Jumlah_Jajan5.place(x=358,y=392)
        
        self.Jumlah_Jajan6 = Label(self.slide7,text=self.Jajan6,bg='#fffdd0')
        self.Jumlah_Jajan6.place(x=575,y=392)
        
        self.Jumlah_Jajan7 = Label(self.slide7,text=self.Jajan7,bg='#fffdd0')
        self.Jumlah_Jajan7.place(x=822,y=392)
          
        self.Jumlah_Jajan8 = Label(self.slide7,text=self.Jajan8,bg='#fffdd0')
        self.Jumlah_Jajan8.place(x=1110,y=392)

        # Plus_Button (Baris 1)
        ButPlus1 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan1)
        ButPlus1.place(x=612,y=165)
        ButPlus2 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan2)
        ButPlus2.place(x=855,y=165)
        ButPlus3 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan3)
        ButPlus3.place(x=1146,y=165)

        # Plus_Button (Baris 2)
        ButPlus4 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan4)
        ButPlus4.place(x=165,y=390)
        ButPlus5 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan5)
        ButPlus5.place(x=400,y=390)
        ButPlus6 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan6)
        ButPlus6.place(x=608,y=390)
        ButPlus7 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan7)
        ButPlus7.place(x=860,y=390)
        ButPlus8 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan8)
        ButPlus8.place(x=1146,y=390)
        
        # Minus_Button (Baris 1)
        ButMin1 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan1)
        ButMin1.place(x=530,y=165)
        ButMin2 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan2)
        ButMin2.place(x=780,y=165)
        ButMin3 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan3)
        ButMin3.place(x=1065,y=165)

        # Minus_Button (Baris 2)
        ButMin4 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan4)
        ButMin4.place(x=88,y=390)
        ButMin5 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan5)
        ButMin5.place(x=309,y=390)
        ButMin6 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan6)
        ButMin6.place(x=530,y=390)
        ButMin7 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan7)
        ButMin7.place(x=775,y=390)
        ButMin8 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan8)
        ButMin8.place(x=1065,y=390)

        # Next Button
        ButNext = Button(self.slide7,text='SELANJUTNYA',width=17,height=1,borderwidth=0,bg='#ff8e84',command=self.Pembayaran,cursor='hand2',activebackground='#ff8e84')
        ButNext.place(x=1077, y=616)

        # Previous Button
        ButPrev = Button(self.slide7,text='KEMBALI',width=17,height=1,borderwidth=0,bg='#ff8e84',cursor='hand2',activebackground='#ff8e84',command=self.Minuman)
        ButPrev.place(x=70, y=617)

    def tambah_jajan1(self):
        self.Jajan1 += 1
        self.Jumlah_Jajan1['text'] = self.Jajan1
    def tambah_jajan2(self):
        self.Jajan2 += 1
        self.Jumlah_Jajan2['text'] = self.Jajan2
    def tambah_jajan3(self):
        self.Jajan3 += 1
        self.Jumlah_Jajan3['text'] = self.Jajan3
    def tambah_jajan4(self):
        self.Jajan4 += 1
        self.Jumlah_Jajan4['text'] = self.Jajan4
    def tambah_jajan5(self):
        self.Jajan5 += 1
        self.Jumlah_Jajan5['text'] = self.Jajan5
    def tambah_jajan6(self):
        self.Jajan6 += 1
        self.Jumlah_Jajan6['text'] = self.Jajan6
    def tambah_jajan7(self):
        self.Jajan7 += 1
        self.Jumlah_Jajan7['text'] = self.Jajan7
    def tambah_jajan8(self):
        self.Jajan8 += 1
        self.Jumlah_Jajan8['text'] = self.Jajan8

    def kurang_jajan1(self):
        self.Jajan1 -= 1
        self.Jumlah_Jajan1['text'] = self.Jajan1
    def kurang_jajan2(self):
        self.Jajan2 -= 1
        self.Jumlah_Jajan2['text'] = self.Jajan2
    def kurang_jajan3(self):
        self.Jajan3 -= 1
        self.Jumlah_Jajan3['text'] = self.Jajan3
    def kurang_jajan4(self):
        self.Jajan4 -= 1
        self.Jumlah_Jajan4['text'] = self.Jajan4
    def kurang_jajan5(self):
        self.Jajan5 -= 1
        self.Jumlah_Jajan5['text'] = self.Jajan5
    def kurang_jajan6(self):
        self.Jajan6 -= 1
        self.Jumlah_Jajan6['text'] = self.Jajan6
    def kurang_jajan7(self):
        self.Jajan7 -= 1
        self.Jumlah_Jajan7['text'] = self.Jajan7
    def kurang_jajan8(self):
        self.Jajan8 -= 1
        self.Jumlah_Jajan8['text'] = self.Jajan8




    def Pembayaran(self):
        self.slide7.destroy()
        self.slide8 = Tk()
        self.slide8.title('Payment Menu')
        self.slide8.geometry('1280x1080')
        self.slide8.resizable(False,False)
        # Background
        background_image = Image.open("tampilan/8.jpg")
        bg_img = ImageTk.PhotoImage(background_image)        
        bg_label = Label(self.slide8, image=bg_img)
        bg_label.image = bg_img  
        bg_label.place(x=0, y=3)

        # Masukkan uang
        Bayar_Button = Button(self.slide8,text='BAYAR',cursor='hand2',bg='#7d0b00',foreground='white',width=30,height=1,borderwidth=0,activebackground='#7d0b00',command=self.MetodePembayaran)
        Bayar_Button.place(x=535, y=617)

        ButPrev8 = Button(self.slide8,text='KEMBALI',width=17,height=1,borderwidth=0,bg='#ff8e84',cursor='hand2',activebackground='#ff8e84',command=self.BacktoJajan)
        ButPrev8.place(x=70, y=617)

        # Pengkondisian Makanan

        # Pengkondisian Minuman
        Label(self.slide8,text='',bg='#ffb4ae').pack(side='top',pady=67)

        HargaMakanan1 = 0
        HargaMakanan2 = 0
        HargaMakanan3 = 0
        HargaMakanan4 = 0
        HargaMakanan5 = 0
        HargaMakanan6 = 0
        HargaMakanan7 = 0
        HargaMakanan8 = 0
        HargaMakanan9 = 0
        locale.setlocale(locale.LC_ALL,"") 
        if self.Makanan1 > 0:
            HargaMakanan1 = self.Makanan1*18000
            Label(self.slide8,text=f'Ayam Goreng Sambel Rawit\t\t{self.Makanan1}\t\tRp. {locale.format_string("%.2f", HargaMakanan1, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Makanan2 > 0:
            HargaMakanan2 = self.Makanan2*10000
            Label(self.slide8,text=f'Telur Geprek\t\t\t{self.Makanan2}\t\tRp. {locale.format_string("%.2f",HargaMakanan2, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Makanan3 > 0:
            HargaMakanan3 = self.Makanan3*17000
            Label(self.slide8,text=f'Mie Goreng\t\t\t{self.Makanan3}\t\tRp. {locale.format_string("%.2f",HargaMakanan3, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Makanan4 > 0:
            HargaMakanan4 = self.Makanan4*20000
            Label(self.slide8,text=f'Daging Sambel Matah\t\t{self.Makanan4}\t\tRp. {locale.format_string("%.2f",HargaMakanan4, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Makanan5 > 0:
            HargaMakanan5 = self.Makanan5*12000
            Label(self.slide8,text=f'Lele Sambel Terasi\t\t{self.Makanan5}\t\tRp. {locale.format_string("%.2f",HargaMakanan5, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Makanan6 > 0:
            HargaMakanan6 = self.Makanan6*7000
            Label(self.slide8,text=f'Tempe Penyet\t\t\t{self.Makanan6}\t\tRp. {locale.format_string("%.2f",HargaMakanan6, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Makanan7 > 0:
            HargaMakanan7 = self.Makanan7*25000
            Label(self.slide8,text=f'Nasi Goreng\t\t\t{self.Makanan7}\t\tRp. {locale.format_string("%.2f",HargaMakanan7, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Makanan8 > 0:
            HargaMakanan8 = self.Makanan8*15000
            Label(self.slide8,text=f'Mujaer Mercon\t\t\t{self.Makanan8}\t\tRp. {locale.format_string("%.2f",HargaMakanan8, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Makanan9 > 0:
            HargaMakanan9 = self.Makanan9*5000
            Label(self.slide8,text=f'Nasi Putih\t\t\t{self.Makanan9}\t\tRp. {locale.format_string("%.2f",HargaMakanan9, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')

        HargaMinum1 = 0
        HargaMinum2 = 0
        HargaMinum3 = 0
        HargaMinum4 = 0
        HargaMinum5 = 0
        HargaMinum6 = 0
        HargaMinum7 = 0
        HargaMinum8 = 0
    
        if self.Minuman1 > 0:
            HargaMinum1 = self.Minuman1*5000
            Label(self.slide8,text=f'Es Jeruk\t\t\t\t{self.Minuman1}\t\tRp. {locale.format_string("%.2f",HargaMinum1, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Minuman2 > 0:
            HargaMinum2 = self.Minuman2*6000
            Label(self.slide8,text=f'Es Blewah\t\t\t{self.Minuman2}\t\tRp. {locale.format_string("%.2f",HargaMinum2, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Minuman3 > 0:
            HargaMinum3 = self.Minuman3*8000
            Label(self.slide8,text=f'Es Coklat\t\t\t{self.Minuman3}\t\tRp. {locale.format_string("%.2f",HargaMinum3, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Minuman4 > 0:
            HargaMinum4 = self.Minuman4*4000
            Label(self.slide8,text=f'Es Teh\t\t\t\t{self.Minuman4}\t\tRp. {locale.format_string("%.2f",HargaMinum4, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Minuman5 > 0:
            HargaMinum5 = self.Minuman5*10000
            Label(self.slide8,text=f'Es Buah\t\t\t\t{self.Minuman5}\t\tRp. {locale.format_string("%.2f",HargaMinum5, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Minuman6 > 0:
            HargaMinum6 = self.Minuman6*12000
            Label(self.slide8,text=f'Jus Alpukat\t\t\t{self.Minuman6}\t\tRp. {locale.format_string("%.2f",HargaMinum6, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Minuman7 > 0:
            HargaMinum7 = self.Minuman7*12000
            Label(self.slide8,text=f'Jus Semangka\t\t\t{self.Minuman7}\t\tRp. {locale.format_string("%.2f",HargaMinum7, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Minuman8 > 0:
            HargaMinum8 = self.Minuman8*7000
            Label(self.slide8,text=f'Dawet\t\t\t\t{self.Minuman8}\t\tRp. {locale.format_string("%.2f",HargaMinum8, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')

        # Pengkondisian Jajan    
        HargaJajan1 = 0
        HargaJajan2 = 0
        HargaJajan3 = 0
        HargaJajan4 = 0
        HargaJajan5 = 0
        HargaJajan6 = 0
        HargaJajan7 = 0
        HargaJajan8 = 0
        if self.Jajan1 > 0:
            HargaJajan1 = self.Jajan1*14000
            Label(self.slide8,text=f'Ayam Udang\t\t\t{self.Jajan1}\t\tRp. {locale.format_string("%.2f",HargaJajan1, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Jajan2 > 0:
            HargaJajan2 = self.Jajan2*11000
            Label(self.slide8,text=f'Hot Dog\t\t\t\t{self.Jajan2}\t\tRp. {locale.format_string("%.2f",HargaJajan2, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Jajan3 > 0:
            HargaJajan3 = self.Jajan3*8000
            Label(self.slide8,text=f'Cireng\t\t\t\t{self.Jajan3}\t\tRp. {locale.format_string("%.2f",HargaJajan3, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Jajan4 > 0:
            HargaJajan4 = self.Jajan4*6000
            Label(self.slide8,text=f'Dessert\t\t\t\t{self.Jajan4}\t\tRp. {locale.format_string("%.2f",HargaJajan4, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Jajan5 > 0:
            HargaJajan5 = self.Jajan5*10000
            Label(self.slide8,text=f'Corn dog\t\t\t\t{self.Jajan5}\t\tRp. {locale.format_string("%.2f",HargaJajan5, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Jajan6 > 0:
            HargaJajan6 = self.Jajan6*11500
            Label(self.slide8,text=f'Burger\t\t\t\t{self.Jajan6}\t\tRp. {locale.format_string("%.2f",HargaJajan6, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Jajan7 > 0:
            HargaJajan7 = self.Jajan7*8000
            Label(self.slide8,text=f'Tahu Kress\t\t\t{self.Jajan7}\t\tRp. {locale.format_string("%.2f",HargaJajan7, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        if self.Jajan8 > 0:
            HargaJajan8 = self.Jajan8*9000
            Label(self.slide8,text=f'Sosis\t\t\t\t{self.Jajan8}\t\tRp. {locale.format_string("%.2f",HargaJajan8, grouping=True)}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')

        self.Total = locale.format_string("%.2f",HargaMinum1 + HargaMinum2 + HargaMinum3 + HargaMinum4 + HargaMinum5 + HargaMinum6 + HargaMinum7 + HargaMinum8 + HargaJajan1 + HargaJajan2 + HargaJajan3 + HargaJajan4 + HargaJajan5 + HargaJajan6 + HargaJajan7 + HargaJajan8 + HargaMakanan1 + HargaMakanan2 + HargaMakanan3 + HargaMakanan4 + HargaMakanan5 + HargaMakanan6 + HargaMakanan7 + HargaMakanan8 + HargaMakanan9, grouping=True)
        
        Label(self.slide8,text="===========================================",font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')
        Label(self.slide8,text=f'Total\t\t{self.Total}',font=('Times New Roman',15,'bold'),bg='#fcf6db').pack(side='top')

      
    def MetodePembayaran(self):
        self.slide8.destroy()
        self.slide9 = Tk()
        self.slide9.title('Payment Menu')
        self.slide9.geometry('1280x1080')
        self.slide9.resizable(False,False)
        
        # Background
        background_image = Image.open("tampilan/9.jpg")
        bg_img = ImageTk.PhotoImage(background_image)
        
        bg_label = Label(self.slide9, image=bg_img)
        bg_label.image = bg_img  
        bg_label.place(x=0, y=3)

        # Button 
        self.photo = PhotoImage(file = r"logo/LOGO BRI.png") 
        self.BRIButtoon = Button(self.slide9,image=self.photo,width=230,height=230,borderwidth=0,bg='white',command=self.DariBRI,activebackground='white',cursor='hand2').place(x=182, y=268)
        
        self.photo2 = PhotoImage(file = r"logo/TUNAI.png") 
        self.TunaiButton = Button(self.slide9,image=self.photo2,width=256,height=210,borderwidth=0,activebackground='white',bg='white',command=self.DariTunai,cursor='hand2').place(x=512, y=268)
        
        self.photo3 = PhotoImage(file = r"logo/QRIS.png") 
        self.QrisButton = Button(self.slide9,image=self.photo3,width=265,height=210,borderwidth=0,activebackground='white',bg='white',command=self.DariQRIS,cursor='hand2').place(x=860, y=275)

      


    def DariBRI(self):
        self.metode_pembayaran = "Transfer dari BRI"
        self.cetak_struk()

    def DariTunai(self):
        self.metode_pembayaran = "Tunai"
        self.cetak_struk()

    def DariQRIS(self):
        self.metode_pembayaran = "via QRIS"
        self.cetak_struk()

    def cetak_struk(self):
        self.slide9.destroy()
        self.slide10 = Tk()
        self.slide10.title('Struk Pembayaran')
        self.slide10.geometry('1280x1080')
        self.slide10.resizable(False,False)

        background_image = Image.open("tampilan/10.jpg")
        bg_img = ImageTk.PhotoImage(background_image)
        
        bg_label = Label(self.slide10, image=bg_img)
        bg_label.image = bg_img  
        bg_label.place(x=0, y=3)


        
        # Tampilkan informasi di struk
        nama = Label(self.slide10, text=self.namapelanggan.get(),bg='white').place(x=595, y=244)
        metode_pembayaran = Label(self.slide10, text=self.metode_pembayaran, bg="white").place(x=595, y= 276)
        localtime = time.asctime(time.localtime(time.time()))
        Tanggal = Label(self.slide10,text=localtime,bg='white').place(x=595, y=260)

        Label(self.slide10,text='',bg='#fcf6db').pack(side= "top", pady=150)
        Label(self.slide10,text="============================================",bg='white').place(x=460,y=300)
        self.HargaMakanan1 = 0
        self.HargaMakanan2 = 0
        self.HargaMakanan3 = 0
        self.HargaMakanan4 = 0
        self.HargaMakanan5 = 0
        self.HargaMakanan6 = 0
        self.HargaMakanan7 = 0
        self.HargaMakanan8 = 0
        self.HargaMakanan9 = 0

        if self.Makanan1 > 0:
            self.HargaMakanan1 = self.Makanan1*18000
            Label(self.slide10,text=f'Ayam Goreng Sambel Rawit\t{self.Makanan1}\t\tRp. {locale.format_string("%.2f",self.HargaMakanan1, grouping=True)}',bg='white').pack(side='top')
        if self.Makanan2 > 0:
            self.HargaMakanan2 = self.Makanan2*10000
            Label(self.slide10,text=f'Telur Geprek\t\t\t{self.Makanan2}\t\tRp. {locale.format_string("%.2f",self.HargaMakanan2, grouping=True)}',bg='white').pack(side='top')
        if self.Makanan3 > 0:
            self.HargaMakanan3 = self.Makanan3*17000
            Label(self.slide10,text=f'Mie Goreng\t\t\t{self.Makanan3}\t\tRp. {locale.format_string("%.2f",self.HargaMakanan3, grouping=True)}',bg='white').pack(side='top')
        if self.Makanan4 > 0:
            self.HargaMakanan4 = self.Makanan4*20000
            Label(self.slide10,text=f'Daging Sambel Matah\t\t{self.Makanan4}\t\tRp. {locale.format_string("%.2f",self.HargaMakanan4, grouping=True)}',bg='white').pack(side='top')
        if self.Makanan5 > 0:
            self.HargaMakanan5 = self.Makanan5*12000
            Label(self.slide10,text=f'Lele Sambel Terasi\t\t{self.Makanan5}\t\tRp. {locale.format_string("%.2f",self.HargaMakanan5, grouping=True)}',bg='white').pack(side='top')
        if self.Makanan6 > 0:
            self.HargaMakanan6 = self.Makanan6*7000
            Label(self.slide10,text=f'Tempe Penyet\t\t\t{self.Makanan6}\t\tRp. {locale.format_string("%.2f",self.HargaMakanan6, grouping=True)}',bg='white',justify='left').pack(side='top')
        if self.Makanan7 > 0:
            self.HargaMakanan7 = self.Makanan7*25000
            Label(self.slide10,text=f'Nasi Goreng\t\t\t{self.Makanan7}\t\tRp. {locale.format_string("%.2f",self.HargaMakanan7, grouping=True)}',bg='white').pack(side='top')
        if self.Makanan8 > 0:
            self.HargaMakanan8 = self.Makanan8*15000
            Label(self.slide10,text=f'Mujaer Mercon\t\t\t{self.Makanan8}\t\tRp. {locale.format_string("%.2f",self.HargaMakanan8, grouping=True)}',bg='white').pack(side='top')
        if self.Makanan9 > 0:
            self.HargaMakanan9 = self.Makanan9*5000
            Label(self.slide10,text=f'Nasi Putih\t\t\t{self.Makanan9}\t\tRp. {locale.format_string("%.2f",self.HargaMakanan9, grouping=True)}',bg='white').pack(side='top')

        # Pengkondisian Minuman
        self.HargaMinum1 = 0
        self.HargaMinum2 = 0
        self.HargaMinum3 = 0
        self.HargaMinum4 = 0
        self.HargaMinum5 = 0
        self.HargaMinum6 = 0
        self.HargaMinum7 = 0
        self.HargaMinum8 = 0
    
        if self.Minuman1 > 0:
            self.HargaMinum1 = self.Minuman1*5000
            Label(self.slide10,text=f'Es Jeruk\t\t\t\t{self.Minuman1}\t\tRp. {locale.format_string("%.2f",self.HargaMinum1, grouping=True)}',bg='white').pack(side='top')
        if self.Minuman2 > 0:
            self.HargaMinum2 = self.Minuman2*6000
            Label(self.slide10,text=f'Es Blewah\t\t\t{self.Minuman2}\t\tRp. {locale.format_string("%.2f",self.HargaMinum2, grouping=True)}',bg='white').pack(side='top')
        if self.Minuman3 > 0:
            self.HargaMinum3 = self.Minuman3*8000
            Label(self.slide10,text=f'Es Coklat\t\t\t{self.Minuman3}\t\tRp. {locale.format_string("%.2f",self.HargaMinum3, grouping=True)}',bg='white').pack(side='top')
        if self.Minuman4 > 0:
            self.HargaMinum4 = self.Minuman4*4000
            Label(self.slide10,text=f'Es Teh\t\t\t\t{self.Minuman4}\t\tRp. {locale.format_string("%.2f",self.HargaMinum4, grouping=True)}',bg='white').pack(side='top')
        if self.Minuman5 > 0:
            self.HargaMinum5 = self.Minuman5*10000
            Label(self.slide10,text=f'Es Buah\t\t\t\t{self.Minuman5}\t\tRp. {locale.format_string("%.2f",self.HargaMinum5, grouping=True)}',bg='white').pack(side='top')
        if self.Minuman6 > 0:
            self.HargaMinum6 = self.Minuman6*12000
            Label(self.slide10,text=f'Jus Alpukat\t\t\t{self.Minuman6}\t\tRp. {locale.format_string("%.2f",self.HargaMinum6, grouping=True)}',bg='white').pack(side='top')
        if self.Minuman7 > 0:
            self.HargaMinum7 = self.Minuman7*12000
            Label(self.slide10,text=f'Jus Semangka\t\t\t{self.Minuman7}\t\tRp. {locale.format_string("%.2f",self.HargaMinum7, grouping=True)}',bg='white').pack(side='top')
        if self.Minuman8 > 0:
            self.HargaMinum8 = self.Minuman8*7000
            Label(self.slide10,text=f'Es Dawet\t\t\t\t{self.Minuman8}\t\tRp. {locale.format_string("%.2f",self.HargaMinum8, grouping=True)}',bg='white').pack(side='top')

        # Pengkondisian Jajan    
        self.HargaJajan1 = 0
        self.HargaJajan2 = 0
        self.HargaJajan3 = 0
        self.HargaJajan4 = 0
        self.HargaJajan5 = 0
        self.HargaJajan6 = 0
        self.HargaJajan7 = 0
        self.HargaJajan8 = 0
        if self.Jajan1 > 0:
            self.HargaJajan1 = self.Jajan1*14000
            Label(self.slide10,text=f'Ayam Udang\t\t\t{self.Jajan1}\t\tRp. {locale.format_string("%.2f",self.HargaJajan1, grouping=True)}',bg='white').pack(side='top')
        if self.Jajan2 > 0:
            self.HargaJajan2 = self.Jajan2*11000
            Label(self.slide10,text=f'Hot Dog\t\t\t\t{self.Jajan2}\t\tRp. {locale.format_string("%.2f",self.HargaJajan2, grouping=True)}',bg='white').pack(side='top')
        if self.Jajan3 > 0:
            self.HargaJajan3 = self.Jajan3*8000
            Label(self.slide10,text=f'Cireng\t\t\t\t{self.Jajan3}\t\tRp. {locale.format_string("%.2f",self.HargaJajan3, grouping=True)}',bg='white').pack(side='top')
        if self.Jajan4 > 0:
            self.HargaJajan4 = self.Jajan4*6000
            Label(self.slide10,text=f'Dessert\t\t\t\t{self.Jajan4}\t\tRp. {locale.format_string("%.2f",self.HargaJajan4, grouping=True)}',bg='white').pack(side='top')
        if self.Jajan5 > 0:
            self.HargaJajan5 = self.Jajan5*10000
            Label(self.slide10,text=f'Corn dog\t\t\t{self.Jajan5}\t\tRp. {locale.format_string("%.2f",self.HargaJajan5, grouping=True)}',bg='white').pack(side='top')
        if self.Jajan6 > 0:
            self.HargaJajan6 = self.Jajan6*12000
            Label(self.slide10,text=f'Burger\t\t\t\t{self.Jajan6}\t\tRp. {locale.format_string("%.2f",self.HargaJajan6, grouping=True)}',bg='white').pack(side='top')
        if self.Jajan7 > 0:
            self.HargaJajan7 = self.Jajan7*8000
            Label(self.slide10,text=f'Tahu Kress\t\t\t{self.Jajan7}\t\tRp. {locale.format_string("%.2f",self.HargaJajan7, grouping=True)}',bg='white').pack(side='top')
        if self.Jajan8 > 0:
            self.HargaJajan8 = self.Jajan8*9000
            Label(self.slide10,text=f'Sosis\t\t\t\t{self.Jajan8}\t\tRp. {locale.format_string("%.2f",self.HargaJajan8, grouping=True)}',bg='white').pack(side='top')

        self.Total = locale.format_string("%.2f",self.HargaMinum1 + self.HargaMinum2 + self.HargaMinum3 + self.HargaMinum4 + self.HargaMinum5 + self.HargaMinum6 + self.HargaMinum7 + self.HargaMinum8 + self.HargaJajan1 + self.HargaJajan2 + self.HargaJajan3 + self.HargaJajan4 + self.HargaJajan5 + self.HargaJajan6 + self.HargaJajan7 + self.HargaJajan8 + self.HargaMakanan1 + self.HargaMakanan2 + self.HargaMakanan3 + self.HargaMakanan4 + self.HargaMakanan5 + self.HargaMakanan6 + self.HargaMakanan7 + self.HargaMakanan8 + self.HargaMakanan9, grouping=True)
        
        Label(self.slide10,text="===========================================",bg='white').pack(side='top')
        Label(self.slide10,text=f'Total\t\t\t\t\t\tRp. {self.Total}',bg='white').pack(side='top')
        Label(self.slide10,text="===========================================",bg='white').pack(side='top')
        Label(self.slide10,text='TERIMA KASIH \n TELAH MENGUNJUNGI RESTORAN \n STARBOY:)',bg='white').pack(side='top')

        ButSelesai = Button(self.slide10,text='SELESAI',width=17,height=1,borderwidth=0,bg='#ff8e84',command=self.Tulis,cursor='hand2',activebackground='#ff8e84')
        ButSelesai.place(x=1077, y=616)

    def Tulis(self):
        waktu_pembelian = datetime.now()
        showinfo('pemberitahuan',f'beri tahu kekasir kode struk anda:\n{waktu_pembelian.strftime("%d%m%H%M%S")}')


         # ------------------------------PENYIMPANAN RIWAYAT STRUK KEDALAM TXT------------------------------------ #
        with open('data_pelanggan/riwayat_pembeli.txt', 'a') as file:
            file.write('\t---------------------------------------------------------------------------------\n')
            file.write('\t|\t\t\t\t\t\t\t\t\t\t|\n')
            file.write('\t|\t\t\t\tJalan Jetis Kulon\t\t\t\t\t\t|\n\t|\t\t\tWonokromo - Wonokromo - Surabaya\t\t\t\t\t\t\t|\n\t|\t\t\t\tTelp.0851-6265-4664\t\t\t\t\t\t|\n')
            file.write('\t|\t===============================================================\t\t\t\t\t\t\t\t\t|\n')
            file.write(f'\t|\tNama\t\t\t\t: {self.namapelanggan.get()}\t\t\t\t\t|\n')
            file.write(f'\t|\tMetode Pembayaran\t\t\t\t: {self.metode_pembayaran}\t\t\t\t\t|\n')
            file.write(f'\t|\tTanggal \t\t\t\t: {waktu_pembelian.strftime("%d-%m-%Y %H-%M-%S")}\t\t\t\t\t|\n')
            file.write(f'\t|\tKode struk\t\t\t\t: {waktu_pembelian.strftime("%d%m%H%M%S")}\n')
            file.write(f'\t|\tPesanan\t\t\t\t:\t\t\t\t\t|\n')
            file.write('\t|\t===============================================================\t\t\t\t\t\t\t\t\t|\n')                
        #Makanan  
            if self.Makanan1 != 0:
                file.write(f'\t|\tAyam Goreng Sambel Rawit\t\t\t\t{self.Makanan1}\t\tRp. {self.HargaMakanan1}\t\t\t|\n')
            if self.Makanan2 != 0:
                file.write(f'\t|\tTelur Geprek\t\t\t\t{self.Makanan2}\t\tRp. {self.HargaMakanan2}\t\t\t|\n')
            if self.Makanan3 != 0:
                file.write(f'\t|\tMie Goreng\t\t\t\t{self.Makanan3}\t\tRp. {self.HargaMakanan3}\t\t\t|\n')
            if self.Makanan4 != 0:
                file.write(f'\t|\tDaging Sambel Matah\t\t\t\t{self.Makanan4}\t\tRp. {self.HargaMakanan4}\t\t\t|\n')
            if self.Makanan5 != 0:
                file.write(f'\t|\tLele Sambel Terasi\t\t\t\t{self.Makanan5}\t\tRp. {self.HargaMakanan5}\t\t\t|\n')
            if self.Makanan6 != 0:
                file.write(f'\t|\tTempe Penyet\t\t\t\t{self.Makanan6}\t\tRp. {self.HargaMakanan6}\t\t\t|\n')
            if self.Makanan7 != 0:
                file.write(f'\t|\tNasi Goreng\t\t\t\t{self.Makanan7}\t\tRp. {self.HargaMakanan7}\t\t\t|\n')
            if self.Makanan8 != 0:
                file.write(f'\t|\tMujaer Mercon\t\t\t\t{self.Makanan8}\t\tRp. {self.HargaMakanan8}\t\t\t|\n')
            if self.Makanan9 != 0:
                file.write(f'\t|\tNasi Putih\t\t\t\t{self.Makanan9}\t\tRp. {self.HargaMakanan9}\t\t\t|\n')

        # Minuman
            if self.Minuman1 != 0:
                file.write(f'\t|\tEs Jeruk\t\t\t\t{self.Minuman1}\t\tRp. {self.HargaMinum1}\t\t\t|\n')
            if self.Minuman2 != 0:
                file.write(f'\t|\tEs Blecenterah\t\t\t\t{self.Minuman2}\t\tRp. {self.HargaMinum2}\t\t\t|\n')
            if self.Minuman3 != 0:
                file.write(f'\t|\tEs Coklat\t\t\t\t{self.Minuman3}\t\tRp. {self.HargaMinum3}\t\t\t|\n')
            if self.Minuman4 != 0:
                file.write(f'\t|\tEs Teh\t\t\t\t{self.Minuman4}\t\tRp. {self.HargaMinum4}\t\t\t|\n')
            if self.Minuman5 != 0:
                file.write(f'\t|\tEs Buah\t\t\t\t{self.Minuman5}\t\tRp. {self.HargaMinum5}\t\t\t|\n')
            if self.Minuman6 != 0:
                file.write(f'\t|\tJus Alpukat\t\t\t\t{self.Minuman6}\t\tRp. {self.HargaMinum6}\t\t\t|\n')
            if self.Minuman7 != 0:
                file.write(f'\t|\tJus Semangka\t\t\t\t{self.Minuman7}\t\tRp. {self.HargaMinum7}\t\t\t|\n')
            if self.Minuman8 != 0:
                file.write(f'\t|\tDawet\t\t\t\t{self.Minuman8}\t\tRp. {self.HargaMinum8}\t\t\t|\n')

        # Jajanmas
            if self.Jajan1 != 0:
                file.write(f'\t|\tAyam Udang\t\t\t\t{self.Jajan1}\t\tRp. {self.HargaJajan1}\t\t\t|\n')
            if self.Jajan2 != 0:
                file.write(f'\t|\tHot Dog\t\t\t\t{self.Jajan2}\t\tRp. {self.HargaJajan2}\t\t\t|\n')
            if self.Jajan3 != 0:
                file.write(f'\t|\tCireng\t\t\t\t{self.Jajan3}\t\tRp. {self.HargaJajan3}\t\t\t|\n')
            if self.Jajan4 != 0:
                file.write(f'\t|\tDessert\t\t\t\t{self.Jajan4}\t\tRp. {self.HargaJajan4}\t\t\t|\n')
            if self.Jajan5 != 0:
                file.write(f'\t|\tCorn dog\t\t\t\t{self.Jajan5}\t\tRp. {self.HargaJajan5}\t\t\t|\n')
            if self.Jajan6 != 0:
                file.write(f'\t|\tBurger\t\t\t\t{self.Jajan6}\t\tRp. {self.HargaJajan6}\t\t\t|\n')
            if self.Jajan7 != 0:
                file.write(f'\t|\tTahu Kress\t\t\t\t{self.Jajan7}\t\tRp. {self.HargaJajan7}\t\t\t|\n')
            if self.Jajan8 != 0:
                file.write(f'\t|\tSosis\t\t\t\t{self.Jajan8}\t\tRp. {self.HargaJajan8}\t\t\t|\n')
            file.write('\t|\t===============================================================\t\t\t\t\t\t\t\t\t|\n')
            file.write(f'\t|\tTotal\t\t\t\t\t\tRp. {self.Total}\t\t\t|\n')
            file.write('\t|\t===============================================================\t\t\t\t\t\t\t\t\t|\n')
            file.write('\t|\t\t\t\t    TERIMA KASIH\t\t\t\t\t\t|\n\t|\t\t\t    TELAH MENGUNJUNGI RESTORAN\t\t\t\t\t\t\t|\n\t|\t\t\t\t     STARBOY:)\t\t\t\t\t\t|\n')
            file.write('\t|\t\t\t\t\t\t\t\t\t\t|\n')
            file.write('\t---------------------------------------------------------------------------------\n\n\n')
            file.write('_________________________________________________________________________________________________\n\n\n')


        #----------------------------------Menyimpan ke struk terbru------------------------------------
        nama_file = f'data_pelanggan/{waktu_pembelian.strftime("%d%m%H%M%S")}.txt'
        with open(nama_file, 'w') as file:
            file.write('\t\t\t       Jalan Jetis Kulon\n\t\tWonokromo - Wonokromo - Surabaya \n\t\t\t   Telp.0851-6265-4664\n')
            file.write('==============================================\n')
            file.write(f'Nama\t\t\t\t: {self.namapelanggan.get()}\n')
            file.write(f'Metode Pembayaran\t\t: {self.metode_pembayaran}\n')
            file.write(f'Tanggal \t\t\t\t: {waktu_pembelian.strftime("%d-%m-%Y %H-%M-%S")}\n')
            file.write(f'Kode struk\t\t\t: {waktu_pembelian.strftime("%d%m%H%M%S")}\n')
            file.write('==============================================\n')                
        # Makanan  
            if self.Makanan1 != 0:
                file.write(f'Ayam Goreng Sambel Rawit\t{self.Makanan1}\t\tRp. {self.HargaMakanan1}\n')
            if self.Makanan2 != 0:
                file.write(f'Telur Geprek\t\t\t{self.Makanan2}\t\tRp. {self.HargaMakanan2}\n')
            if self.Makanan3 != 0:
                file.write(f'Mie Goreng\t\t\t{self.Makanan3}\t\tRp. {self.HargaMakanan3}\n')
            if self.Makanan4 != 0:
                file.write(f'Daging Sambel Matah\t\t{self.Makanan4}\t\tRp. {self.HargaMakanan4}\n')
            if self.Makanan5 != 0:
                file.write(f'Lele Sambel Terasi\t\t{self.Makanan5}\t\tRp. {self.HargaMakanan5}\n')
            if self.Makanan6 != 0:
                file.write(f'Tempe Penyet\t\t\t{self.Makanan6}\t\tRp. {self.HargaMakanan6}\n')
            if self.Makanan7 != 0:
                file.write(f'Nasi Goreng\t\t\t{self.Makanan7}\t\tRp. {self.HargaMakanan7}\n')
            if self.Makanan8 != 0:
                file.write(f'Mujaer Mercon\t\t\t{self.Makanan8}\t\tRp. {self.HargaMakanan8}\n')
            if self.Makanan9 != 0:
                file.write(f'Nasi Putih\t\t\t{self.Makanan9}\t\tRp. {self.HargaMakanan9}\n')

        # Minuman
            if self.Minuman1 != 0:
                file.write(f'Es Jeruk\t\t\t\t{self.Minuman1}\t\tRp. {self.HargaMinum1}\n')
            if self.Minuman2 != 0:
                file.write(f'Es Blecenterah\t\t\t{self.Minuman2}\t\tRp. {self.HargaMinum2}\n')
            if self.Minuman3 != 0:
                file.write(f'Es Coklat\t\t\t{self.Minuman3}\t\tRp. {self.HargaMinum3}\n')
            if self.Minuman4 != 0:
                file.write(f'Es Teh\t\t\t\t{self.Minuman4}\t\tRp. {self.HargaMinum4}\n')
            if self.Minuman5 != 0:
                file.write(f'Es Buah\t\t\t\t{self.Minuman5}\t\tRp. {self.HargaMinum5}\n')
            if self.Minuman6 != 0:
                file.write(f'Jus Alpukat\t\t\t{self.Minuman6}\t\tRp. {self.HargaMinum6}\n')
            if self.Minuman7 != 0:
                file.write(f'Jus Semangka\t\t\t{self.Minuman7}\t\tRp. {self.HargaMinum7}\n')
            if self.Minuman8 != 0:
                file.write(f'Dawet\t\t\t\t{self.Minuman8}\t\tRp. {self.HargaMinum8}\n')

        # Jajan
            if self.Jajan1 != 0:
                file.write(f'Ayam Udang\t\t\t{self.Jajan1}\t\tRp. {self.HargaJajan1}\n')
            if self.Jajan2 != 0:
                file.write(f'Hot Dog\t\t\t\t{self.Jajan2}\t\tRp. {self.HargaJajan2}\n')
            if self.Jajan3 != 0:
                file.write(f'Cireng\t\t\t\t{self.Jajan3}\t\tRp. {self.HargaJajan3}\n')
            if self.Jajan4 != 0:
                file.write(f'Dessert\t\t\t\t{self.Jajan4}\t\tRp. {self.HargaJajan4}\n')
            if self.Jajan5 != 0:
                file.write(f'Corn dog\t\t\t{self.Jajan5}\t\tRp. {self.HargaJajan5}\n')
            if self.Jajan6 != 0:
                file.write(f'Burger\t\t\t\t{self.Jajan6}\t\tRp. {self.HargaJajan6}\n')
            if self.Jajan7 != 0:
                file.write(f'Tahu Kress\t\t\t{self.Jajan7}\t\tRp. {self.HargaJajan7}\n')
            if self.Jajan8 != 0:
                file.write(f'Sosis\t\t\t\t{self.Jajan8}\t\tRp. {self.HargaJajan8}\n')
            file.write('==============================================\n')
            file.write(f'Total\t\t\t\t\t\tRp. {self.Total}\n')
            file.write('==============================================\n')
            file.write('\t\t\t  TERIMA KASIH\n\t\tTELAH MENGUNJUNGI RESTORAN\n\t\t\t     STARBOY:)\n\n\n')

        # Buka file Excel
        self.workbook = openpyxl.load_workbook('data_pelanggan/Rekap_Bulanan.xlsx')

        # Pilih worksheet yang diinginkan (misalnya, worksheet pertama)
        self.sheet = self.workbook.active

        # Baca nilai pada sel A1
        # Makanan
        self.Makanan_Excel1 = self.sheet['A1'].value
        self.Makanan_Excel2 = self.sheet['A2'].value
        self.Makanan_Excel3 = self.sheet['A3'].value
        self.Makanan_Excel4 = self.sheet['A4'].value
        self.Makanan_Excel5 = self.sheet['A5'].value
        self.Makanan_Excel6 = self.sheet['A6'].value
        self.Makanan_Excel7 = self.sheet['A7'].value
        self.Makanan_Excel8 = self.sheet['A8'].value
        self.Makanan_Excel9 = self.sheet['A9'].value

        self.Minuman_Excel1 = self.sheet['B1'].value
        self.Minuman_Excel2 = self.sheet['B2'].value
        self.Minuman_Excel3 = self.sheet['B3'].value
        self.Minuman_Excel4 = self.sheet['B4'].value
        self.Minuman_Excel5 = self.sheet['B5'].value
        self.Minuman_Excel6 = self.sheet['B6'].value
        self.Minuman_Excel7 = self.sheet['B7'].value
        self.Minuman_Excel8 = self.sheet['B8'].value

        self.Jajan_Excel1 = self.sheet['C1'].value
        self.Jajan_Excel2 = self.sheet['C2'].value
        self.Jajan_Excel3 = self.sheet['C3'].value
        self.Jajan_Excel4 = self.sheet['C4'].value
        self.Jajan_Excel5 = self.sheet['C5'].value
        self.Jajan_Excel6 = self.sheet['C6'].value
        self.Jajan_Excel7 = self.sheet['C7'].value
        self.Jajan_Excel8 = self.sheet['C8'].value


        # Mengubah nilai pada kolom makanan
        # MAKANAN
        self.MakananBaru1 = self.Makanan_Excel1 + self.Makanan1
        self.MakananBaru2 = self.Makanan_Excel2 + self.Makanan2
        self.MakananBaru3 = self.Makanan_Excel3 + self.Makanan3
        self.MakananBaru4 = self.Makanan_Excel4 + self.Makanan4
        self.MakananBaru5 = self.Makanan_Excel5 + self.Makanan5
        self.MakananBaru6 = self.Makanan_Excel6 + self.Makanan6
        self.MakananBaru7 = self.Makanan_Excel7 + self.Makanan7
        self.MakananBaru8 = self.Makanan_Excel8 + self.Makanan8
        self.MakananBaru9 = self.Makanan_Excel9 + self.Makanan9

        # MINUMAN
        self.MinumanBaru1 = self.Minuman_Excel1 + self.Minuman1
        self.MinumanBaru2 = self.Minuman_Excel2 + self.Minuman2
        self.MinumanBaru3 = self.Minuman_Excel3 + self.Minuman3
        self.MinumanBaru4 = self.Minuman_Excel4 + self.Minuman4
        self.MinumanBaru5 = self.Minuman_Excel5 + self.Minuman5
        self.MinumanBaru6 = self.Minuman_Excel6 + self.Minuman6
        self.MinumanBaru7 = self.Minuman_Excel7 + self.Minuman7
        self.MinumanBaru8 = self.Minuman_Excel8 + self.Minuman8


        # JAJAN
        self.JajanBaru1 = self.Jajan_Excel1 + self.Jajan1
        self.JajanBaru2 = self.Jajan_Excel2 + self.Jajan2
        self.JajanBaru3 = self.Jajan_Excel3 + self.Jajan3
        self.JajanBaru4 = self.Jajan_Excel4 + self.Jajan4
        self.JajanBaru5 = self.Jajan_Excel5 + self.Jajan5
        self.JajanBaru6 = self.Jajan_Excel6 + self.Jajan6
        self.JajanBaru7 = self.Jajan_Excel7 + self.Jajan7
        self.JajanBaru8 = self.Jajan_Excel8 + self.Jajan8


        self.sheet['A1'] = self.MakananBaru1
        self.sheet['A2'] = self.MakananBaru2
        self.sheet['A3'] = self.MakananBaru3
        self.sheet['A4'] = self.MakananBaru4
        self.sheet['A5'] = self.MakananBaru5
        self.sheet['A6'] = self.MakananBaru6
        self.sheet['A7'] = self.MakananBaru7
        self.sheet['A8'] = self.MakananBaru8
        self.sheet['A9'] = self.MakananBaru9

        self.sheet['B1'] = self.MinumanBaru1
        self.sheet['B2'] = self.MinumanBaru2
        self.sheet['B3'] = self.MinumanBaru3
        self.sheet['B4'] = self.MinumanBaru4
        self.sheet['B5'] = self.MinumanBaru5
        self.sheet['B6'] = self.MinumanBaru6
        self.sheet['B7'] = self.MinumanBaru7
        self.sheet['B8'] = self.MinumanBaru8

        self.sheet['C1'] = self.JajanBaru1
        self.sheet['C2'] = self.JajanBaru2
        self.sheet['C3'] = self.JajanBaru3
        self.sheet['C4'] = self.JajanBaru4
        self.sheet['C5'] = self.JajanBaru5
        self.sheet['C6'] = self.JajanBaru6
        self.sheet['C7'] = self.JajanBaru7
        self.sheet['C8'] = self.JajanBaru8

        self.workbook.save('data_pelanggan/Rekap_Bulanan.xlsx')

        self.workbook = openpyxl.load_workbook('data_pelanggan/REKAP_HARIAN.xlsx')

        # Pilih worksheet yang diinginkan (misalnya, worksheet pertama)
        self.sheet = self.workbook.active

        # Baca nilai pada sel A1
        # Makanan
        self.Makanan_Excel1 = self.sheet['A1'].value
        self.Makanan_Excel2 = self.sheet['A2'].value
        self.Makanan_Excel3 = self.sheet['A3'].value
        self.Makanan_Excel4 = self.sheet['A4'].value
        self.Makanan_Excel5 = self.sheet['A5'].value
        self.Makanan_Excel6 = self.sheet['A6'].value
        self.Makanan_Excel7 = self.sheet['A7'].value
        self.Makanan_Excel8 = self.sheet['A8'].value
        self.Makanan_Excel9 = self.sheet['A9'].value

        self.Minuman_Excel1 = self.sheet['B1'].value
        self.Minuman_Excel2 = self.sheet['B2'].value
        self.Minuman_Excel3 = self.sheet['B3'].value
        self.Minuman_Excel4 = self.sheet['B4'].value
        self.Minuman_Excel5 = self.sheet['B5'].value
        self.Minuman_Excel6 = self.sheet['B6'].value
        self.Minuman_Excel7 = self.sheet['B7'].value
        self.Minuman_Excel8 = self.sheet['B8'].value

        self.Jajan_Excel1 = self.sheet['C1'].value
        self.Jajan_Excel2 = self.sheet['C2'].value
        self.Jajan_Excel3 = self.sheet['C3'].value
        self.Jajan_Excel4 = self.sheet['C4'].value
        self.Jajan_Excel5 = self.sheet['C5'].value
        self.Jajan_Excel6 = self.sheet['C6'].value
        self.Jajan_Excel7 = self.sheet['C7'].value
        self.Jajan_Excel8 = self.sheet['C8'].value


        # Mengubah nilai pada kolom makanan
        # MAKANAN
        self.MakananBaru1 = self.Makanan_Excel1 + self.Makanan1
        self.MakananBaru2 = self.Makanan_Excel2 + self.Makanan2
        self.MakananBaru3 = self.Makanan_Excel3 + self.Makanan3
        self.MakananBaru4 = self.Makanan_Excel4 + self.Makanan4
        self.MakananBaru5 = self.Makanan_Excel5 + self.Makanan5
        self.MakananBaru6 = self.Makanan_Excel6 + self.Makanan6
        self.MakananBaru7 = self.Makanan_Excel7 + self.Makanan7
        self.MakananBaru8 = self.Makanan_Excel8 + self.Makanan8
        self.MakananBaru9 = self.Makanan_Excel9 + self.Makanan9

        # MINUMAN
        self.MinumanBaru1 = self.Minuman_Excel1 + self.Minuman1
        self.MinumanBaru2 = self.Minuman_Excel2 + self.Minuman2
        self.MinumanBaru3 = self.Minuman_Excel3 + self.Minuman3
        self.MinumanBaru4 = self.Minuman_Excel4 + self.Minuman4
        self.MinumanBaru5 = self.Minuman_Excel5 + self.Minuman5
        self.MinumanBaru6 = self.Minuman_Excel6 + self.Minuman6
        self.MinumanBaru7 = self.Minuman_Excel7 + self.Minuman7
        self.MinumanBaru8 = self.Minuman_Excel8 + self.Minuman8


        # JAJAN
        self.JajanBaru1 = self.Jajan_Excel1 + self.Jajan1
        self.JajanBaru2 = self.Jajan_Excel2 + self.Jajan2
        self.JajanBaru3 = self.Jajan_Excel3 + self.Jajan3
        self.JajanBaru4 = self.Jajan_Excel4 + self.Jajan4
        self.JajanBaru5 = self.Jajan_Excel5 + self.Jajan5
        self.JajanBaru6 = self.Jajan_Excel6 + self.Jajan6
        self.JajanBaru7 = self.Jajan_Excel7 + self.Jajan7
        self.JajanBaru8 = self.Jajan_Excel8 + self.Jajan8


        self.sheet['A1'] = self.MakananBaru1
        self.sheet['A2'] = self.MakananBaru2
        self.sheet['A3'] = self.MakananBaru3
        self.sheet['A4'] = self.MakananBaru4
        self.sheet['A5'] = self.MakananBaru5
        self.sheet['A6'] = self.MakananBaru6
        self.sheet['A7'] = self.MakananBaru7
        self.sheet['A8'] = self.MakananBaru8
        self.sheet['A9'] = self.MakananBaru9

        self.sheet['B1'] = self.MinumanBaru1
        self.sheet['B2'] = self.MinumanBaru2
        self.sheet['B3'] = self.MinumanBaru3
        self.sheet['B4'] = self.MinumanBaru4
        self.sheet['B5'] = self.MinumanBaru5
        self.sheet['B6'] = self.MinumanBaru6
        self.sheet['B7'] = self.MinumanBaru7
        self.sheet['B8'] = self.MinumanBaru8

        self.sheet['C1'] = self.JajanBaru1
        self.sheet['C2'] = self.JajanBaru2
        self.sheet['C3'] = self.JajanBaru3
        self.sheet['C4'] = self.JajanBaru4
        self.sheet['C5'] = self.JajanBaru5
        self.sheet['C6'] = self.JajanBaru6
        self.sheet['C7'] = self.JajanBaru7
        self.sheet['C8'] = self.JajanBaru8

        self.workbook.save('data_pelanggan/REKAP_HARIAN.xlsx')

        # Simpan perubahan ke file Excel


        self.slide10.destroy()
    def Minuman(self):
        self.slide7.destroy()
        self.Slide6 = Tk()
        self.Slide6.title("Food")
        self.Slide6.geometry('1280x1080')
        self.Slide6.resizable(False,False)

        # Background
        background_image = Image.open("tampilan/6.jpg")
        bg_img = ImageTk.PhotoImage(background_image)
        
        bg_label = Label(self.Slide6, image=bg_img)
        bg_label.image = bg_img  
        bg_label.place(x=0, y=3) 
        
        # Inisiasi Hitungan (Baris 1)
        self.Jumlah_Minuman1 = Label(self.Slide6,text=self.Minuman1,bg='#fffdd0')
        self.Jumlah_Minuman1.place(x=575,y=167)
        self.Jumlah_Minuman2 = Label(self.Slide6,text=self.Minuman2,bg='#fffdd0')
        self.Jumlah_Minuman2.place(x=811,y=167)
        self.Jumlah_Minuman3 = Label(self.Slide6,text=self.Minuman3,bg='#fffdd0')
        self.Jumlah_Minuman3.place(x=1111,y=167)

        # Inisiasi Minuman (Baris 2)
        self.Jumlah_Minuman4 = Label(self.Slide6,text=self.Minuman4,bg='#fffdd0')
        self.Jumlah_Minuman4.place(x=130,y=392)
        self.Jumlah_Minuman5 = Label(self.Slide6,text=self.Minuman5,bg='#fffdd0')
        self.Jumlah_Minuman5.place(x=358,y=392)
        self.Jumlah_Minuman6 = Label(self.Slide6,text=self.Minuman6,bg='#fffdd0')
        self.Jumlah_Minuman6.place(x=575,y=392)
        self.Jumlah_Minuman7 = Label(self.Slide6,text=self.Minuman7,bg='#fffdd0')
        self.Jumlah_Minuman7.place(x=809,y=392)
        self.Jumlah_Minuman8 = Label(self.Slide6,text=self.Minuman8,bg='#fffdd0')
        self.Jumlah_Minuman8.place(x=1110,y=392)

        # Plus_Button (Baris 1)
        ButPlus1 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman1)
        ButPlus1.place(x=612,y=165)
        ButPlus2 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman2)
        ButPlus2.place(x=846,y=165)
        ButPlus3 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman3)
        ButPlus3.place(x=1146,y=165)

        # Plus_Button (Baris 2)
        ButPlus4 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman4)
        ButPlus4.place(x=165,y=390)
        ButPlus5 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman5)
        ButPlus5.place(x=400,y=390)
        ButPlus6 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman6)
        ButPlus6.place(x=608,y=390)
        ButPlus7 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman7)
        ButPlus7.place(x=846,y=390)
        ButPlus8 = Button(self.Slide6,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_Minuman8)
        ButPlus8.place(x=1146,y=390)
        
        # Minus_Button (Baris 1)
        ButMin1 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman1)
        ButMin1.place(x=530,y=165)
        ButMin2 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman2)
        ButMin2.place(x=765,y=165)
        ButMin3 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman3)
        ButMin3.place(x=1065,y=165)

        # Minus_Button (Baris 2)
        ButMin4 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman4)
        ButMin4.place(x=88,y=390)
        ButMin5 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman5)
        ButMin5.place(x=309,y=390)
        ButMin6 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman6)
        ButMin6.place(x=530,y=390)
        ButMin7 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman7)
        ButMin7.place(x=765,y=390)
        ButMin8 = Button(self.Slide6,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_Minuman8)
        ButMin8.place(x=1065,y=390)

        # Next Button
        ButNext = Button(self.Slide6,text='SELANJUTNYA',width=17,height=1,borderwidth=0,bg='#ff8e84',command=self.Menu_Jajan,cursor='hand2',activebackground='#ff8e84')
        ButNext.place(x=1077, y=616)

        # Previous Button
        ButPrev = Button(self.Slide6,text='KEMBALI',width=17,height=1,borderwidth=0,bg='#ff8e84',cursor='hand2',activebackground='#ff8e84',command=self.BackToMakanan)
        ButPrev.place(x=70, y=617)
        
    def BacktoJajan(self):
        self.slide8.destroy()
        self.slide7 = Tk()
        self.slide7.title('Additional Food')
        self.slide7.geometry('1280x1080')
        self.slide7.resizable(False,False)
        # Background

        background_image = Image.open("tampilan/7.jpg")
        bg_img = ImageTk.PhotoImage(background_image)
        bg_label = Label(self.slide7, image=bg_img)
        bg_label.image = bg_img  
        bg_label.place(x=0, y=3) 

    
        # Inisiasi Hitungan (Baris 1)
        # self.Jajan1 = IntVar().get()
        self.Jumlah_Jajan1 = Label(self.slide7,text=self.Jajan1,bg='#fffdd0')
        self.Jumlah_Jajan1.place(x=575,y=167)
        # self.Jajan2 = IntVar().get()
        self.Jumlah_Jajan2 = Label(self.slide7,text=self.Jajan2,bg='#fffdd0')
        self.Jumlah_Jajan2.place(x=820,y=167)
        # self.Jajan3 = IntVar().get()
        self.Jumlah_Jajan3 = Label(self.slide7,text=self.Jajan3,bg='#fffdd0')
        self.Jumlah_Jajan3.place(x=1111,y=167)

        # Inisiasi Jajan (Baris 2)
        # self.Jajan4 = IntVar().get()
        self.Jumlah_Jajan4 = Label(self.slide7,text=self.Jajan4,bg='#fffdd0')
        self.Jumlah_Jajan4.place(x=130,y=392)
        # self.Jajan5 = IntVar().get()
        self.Jumlah_Jajan5 = Label(self.slide7,text=self.Jajan5,bg='#fffdd0')
        self.Jumlah_Jajan5.place(x=358,y=392)
        # self.Jajan6 = IntVar().get()
        self.Jumlah_Jajan6 = Label(self.slide7,text=self.Jajan6,bg='#fffdd0')
        self.Jumlah_Jajan6.place(x=575,y=392)
        # self.Jajan7 = IntVar().get()
        self.Jumlah_Jajan7 = Label(self.slide7,text=self.Jajan7,bg='#fffdd0')
        self.Jumlah_Jajan7.place(x=822,y=392)
        # self.Jajan8 = IntVar().get()  
        self.Jumlah_Jajan8 = Label(self.slide7,text=self.Jajan8,bg='#fffdd0')
        self.Jumlah_Jajan8.place(x=1110,y=392)

        # Plus_Button (Baris 1)
        ButPlus1 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan1)
        ButPlus1.place(x=612,y=165)
        ButPlus2 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan2)
        ButPlus2.place(x=855,y=165)
        ButPlus3 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan3)
        ButPlus3.place(x=1146,y=165)

        # Plus_Button (Baris 2)
        ButPlus4 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan4)
        ButPlus4.place(x=165,y=390)
        ButPlus5 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan5)
        ButPlus5.place(x=400,y=390)
        ButPlus6 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan6)
        ButPlus6.place(x=608,y=390)
        ButPlus7 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan7)
        ButPlus7.place(x=860,y=390)
        ButPlus8 = Button(self.slide7,text="+",height=1,cursor='hand2',activebackground='yellow',command=self.tambah_jajan8)
        ButPlus8.place(x=1146,y=390)
        
        # Minus_Button (Baris 1)
        ButMin1 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan1)
        ButMin1.place(x=530,y=165)
        ButMin2 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan2)
        ButMin2.place(x=780,y=165)
        ButMin3 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan3)
        ButMin3.place(x=1065,y=165)

        # Minus_Button (Baris 2)
        ButMin4 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan4)
        ButMin4.place(x=88,y=390)
        ButMin5 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan5)
        ButMin5.place(x=309,y=390)
        ButMin6 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan6)
        ButMin6.place(x=530,y=390)
        ButMin7 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan7)
        ButMin7.place(x=775,y=390)
        ButMin8 = Button(self.slide7,text='-',height=1,cursor='hand2',activebackground='red',command=self.kurang_jajan8)
        ButMin8.place(x=1065,y=390)

        # Next Button
        ButNext = Button(self.slide7,text='SELANJUTNYA',width=17,height=1,borderwidth=0,bg='#ff8e84',command=self.Pembayaran,cursor='hand2',activebackground='#ff8e84')
        ButNext.place(x=1077, y=616)

        # Previous Button
        ButPrev = Button(self.slide7,text='KEMBALI',width=17,height=1,borderwidth=0,bg='#ff8e84',cursor='hand2',activebackground='#ff8e84',command=self.Minuman)
        ButPrev.place(x=70, y=617)

    def tambah_jajan1(self):
        self.Jajan1 += 1
        self.Jumlah_Jajan1['text'] = self.Jajan1
    def tambah_jajan2(self):
        self.Jajan2 += 1
        self.Jumlah_Jajan2['text'] = self.Jajan2
    def tambah_jajan3(self):
        self.Jajan3 += 1
        self.Jumlah_Jajan3['text'] = self.Jajan3
    def tambah_jajan4(self):
        self.Jajan4 += 1
        self.Jumlah_Jajan4['text'] = self.Jajan4
    def tambah_jajan5(self):
        self.Jajan5 += 1
        self.Jumlah_Jajan5['text'] = self.Jajan5
    def tambah_jajan6(self):
        self.Jajan6 += 1
        self.Jumlah_Jajan6['text'] = self.Jajan6
    def tambah_jajan7(self):
        self.Jajan7 += 1
        self.Jumlah_Jajan7['text'] = self.Jajan7
    def tambah_jajan8(self):
        self.Jajan8 += 1
        self.Jumlah_Jajan8['text'] = self.Jajan8

    def kurang_jajan1(self):
        self.Jajan1 -= 1
        self.Jumlah_Jajan1['text'] = self.Jajan1
    def kurang_jajan2(self):
        self.Jajan2 -= 1
        self.Jumlah_Jajan2['text'] = self.Jajan2
    def kurang_jajan3(self):
        self.Jajan3 -= 1
        self.Jumlah_Jajan3['text'] = self.Jajan3
    def kurang_jajan4(self):
        self.Jajan4 -= 1
        self.Jumlah_Jajan4['text'] = self.Jajan4
    def kurang_jajan5(self):
        self.Jajan5 -= 1
        self.Jumlah_Jajan5['text'] = self.Jajan5
    def kurang_jajan6(self):
        self.Jajan6 -= 1
        self.Jumlah_Jajan6['text'] = self.Jajan6
    def kurang_jajan7(self):
        self.Jajan7 -= 1
        self.Jumlah_Jajan7['text'] = self.Jajan7
    def kurang_jajan8(self):
        self.Jajan8 -= 1
        self.Jumlah_Jajan8['text'] = self.Jajan8

        


