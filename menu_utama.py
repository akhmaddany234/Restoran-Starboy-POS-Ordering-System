from tkinter import *
from PIL import ImageTk, Image

class MenuUtamaMixin:
#----------------------------------------------------------------------------------KODE UNTUK BERANDA--------------------------------------------------------------------------------------------------------------------
    def __init__(self, tampilan):
        self.tampilan = tampilan
        tampilan.title("Selamat datang di Restoran Starboy")
        tampilan.geometry('1280x680')

        # Buka gambar dengan PIL
        img = Image.open("tampilan/tampilan pertama.jpg")  
        self.gambar = ImageTk.PhotoImage(img)

        # Tampilkan gambar di label
        label_gambar = Label(tampilan, image=self.gambar)
        label_gambar.pack(pady=0)

        # Tombol button pemilik
        self.pemilik_button = Button(tampilan,text= 'PEMILIK', command=self.loginpemilik,font = ("Clear Sans", 20, 'bold') ,width=18,height=0 , bg="#FF8E84",bd=0,cursor='hand2',activebackground='#FF8E84')
        self.pemilik_button.place(x=88-15,y=428-24)

        # Tombol button pelanggan
        self.pelanggan_button = Button(tampilan,text= 'PELANGGAN', command=self.loginpelanggan,font = ("Clear Sans", 20, 'bold') ,width=18,height=0 , bg="#FF8E84", bd=0,cursor='hand2',activebackground='#FF8E84')
        self.pelanggan_button.place(x=530-20-17,y=428-24)

        # Tombol button pegawai
        self.pegawai_button = Button(tampilan,text= 'PEGAWAI', command=self.loginpegawai,font = ("Clear Sans", 20, 'bold') ,width=18,height=0 , bg="#FF8E84", bd=0,cursor='hand2',activebackground='#FF8E84')
        self.pegawai_button.place(x=980-50-25,y=428-24)
