from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
import openpyxl
from datetime import datetime
import time
from tkinter import ttk

class PegawaiMixin:
#--------------------------------------------------------------------program untuk login pegawai----------------------------------------------------------------------------------------------------------------------------------
    def loginpegawai(self):
        self.tampilan.destroy()
        self.window_pegawai = Tk()
        self.window_pegawai.geometry('1280x680')

        img3 = Image.open("tampilan/loginpegawai.jpg")
        self.pegawailogin = ImageTk.PhotoImage(img3)
        label_gambarpegawai = Label(self.window_pegawai, image=self.pegawailogin)
        label_gambarpegawai.pack(pady=0)

        #pemasukan username 
        Label(self.window_pegawai,text="NAMA:",font=("Times New Roman",25,"bold"),bg="#FCF6D8").place(x=585,y=190)
        self.Nama_pegawai = StringVar()
        Entry(self.window_pegawai,textvariable=self.Nama_pegawai,font=("Times New Roman",25),borderwidth=0,width=17,justify="center").place(x=495,y=242)

        #pemasukkan kata sandi
        Label(self.window_pegawai,text="SANDI:",font=("Times New Roman",25,"bold"),bg="#FCF6D8").place(x=585,y=300)
        self.Sandi_pegawai = StringVar()
        Entry(self.window_pegawai,textvariable=self.Sandi_pegawai,font=("Times New Roman",25),borderwidth=0,width=17,justify="center").place(x=495,y=350)
        
        #membuat tombol login                                                                                                                                                
        Button(self.window_pegawai,text="LOGIN",font=("Times New Roman",20,"bold"),command=self.Cek_Akun_Pegawai,bg="#7D0B00",fg="white",width=10,cursor='hand2').place(x=552,y=425)
    
    #pengecekkan akun apakah yang di masukkan itu benar sesuai dengan ctt akun pegawai
    def Cek_Akun_Pegawai(self):
        nama = self.Nama_pegawai.get().upper()
        sandi = self.Sandi_pegawai.get()

        #membuka file txt untuk membaca
        with open("akun/akun_pegawai.txt", "r") as file:
            akunpegawai = file.read().splitlines()

        if f"{nama}:{sandi}" in akunpegawai:
            showinfo("Berhasil", "Login berhasil!")
            self.histori_penjualan()
        else:
            showerror("Gagal", "Nama atau sandi salah. Coba lagi.")

    #tampilan setelah memasukkan akun pegawai
    def histori_penjualan(self):
        self.window_pegawai.destroy()
        self.window_histori_penjualan = Tk()
        self.window_histori_penjualan.geometry('1280x680')

        img3 = Image.open("tampilan/12.jpg")
        self.tampilan_histori = ImageTk.PhotoImage(img3)
        label_gambarhistori = Label(self.window_histori_penjualan, image=self.tampilan_histori)
        label_gambarhistori.pack(pady=0)

        Button(self.window_histori_penjualan,text="CETAK STRUK",bg="#7d0b00",fg="white",bd=0,activebackground="#7d0b00",font=('times new roman',15,'bold'),width=23,cursor='hand2',command=self.CetakStruk).place(x=508,y=330)
        Button(self.window_histori_penjualan,text="   RIWAYAT   ",bg="#7d0b00",fg="white",bd=0,activebackground="#7d0b00",font=('times new roman',15,'bold'),width=23,cursor='hand2',command=self.RiwayatStrukPembeli).place(x=508,y=415)

    def CetakStruk(self):
        self.window_histori_penjualan.withdraw()
        self.window_PembayaranPembeli = Toplevel(self.window_histori_penjualan)
        self.window_PembayaranPembeli.geometry('1280x680')

        # Memuat dan menampilkan gambar latar belakang  
        img11 = Image.open("tampilan/Search Bar Struk.jpg")
        self.PembayaranPembeli = ImageTk.PhotoImage(img11)
        label_gambar = Label(self.window_PembayaranPembeli, image=self.PembayaranPembeli)
        label_gambar.pack(pady=0)

        self.kodestruk = StringVar()
        Entry(self.window_PembayaranPembeli,textvariable=self.kodestruk,font=("Times New Roman",25),borderwidth=0,width=18,justify="center").place(x=55, y=170)
        Button(self.window_PembayaranPembeli,text='Cari Struk',width=22,height=1,borderwidth=0,bg='#ff8e84',command=self.TampilkanStruk,cursor='hand2',activebackground='#ff8e84').place(x=130,y=240)


    def TampilkanStruk(self):
        # Periksa apakah file ada
        file_struk = f'data_pelanggan/{self.kodestruk.get()}.txt'

        # Membuat canvas
        canvas = Canvas(self.window_PembayaranPembeli, width=390, height=450, bg='white', borderwidth=0, highlightthickness=0)
        canvas.place(x=440, y=180)

        # Memuat teks untuk ditampilkan di atas canvas
        with open(file_struk, 'r') as file:
            isi_teks = file.read()
            canvas.create_text(10, 10, anchor=NW, text=isi_teks)


        ButPrint = Button(self.window_PembayaranPembeli,text='PRINT',width=17,height=1,borderwidth=0,bg='#ff8e84',command=self.loadingpage,cursor='hand2',activebackground='#ff8e84')
        ButPrint.place(x=1077, y=612)
    def loadingpage(self):
        
        self.progress_var =IntVar()
        self.progress_bar =ttk.Progressbar(self.window_PembayaranPembeli, variable=self.progress_var, maximum=100)
        self.progress_bar.place(x=10,y=10)
        self.hancurkan()
        

    def hancurkan(self):
        for i in range(101):
            self.progress_var.set(i)
            self.window_PembayaranPembeli.update_idletasks()
            time.sleep(0.05)


        showinfo(message='PRINTED')
        self.window_PembayaranPembeli.destroy()
        self.window_histori_penjualan.deiconify()

    def RiwayatStrukPembeli(self):
        self.window_histori_penjualan.withdraw()
        self.window_RiwayatStrukPembeli = Toplevel(self.window_histori_penjualan)
        self.window_RiwayatStrukPembeli.geometry('1280x680')

        # Memuat dan menampilkan gambar latar belakang
        img14 = Image.open("tampilan/riwayat struk.png")
        self.RiwayatStrukPembeli = ImageTk.PhotoImage(img14)
        label_gambar = Label(self.window_RiwayatStrukPembeli, image=self.RiwayatStrukPembeli)
        label_gambar.pack(pady=0)

        # Membuat widget Text untuk mengedit teks
        self.text_widget = Text(self.window_RiwayatStrukPembeli, wrap='word', height=26, width=97,bd=0)
        self.text_widget.place(x=250, y=180)

        # Memuat teks untuk ditampilkan di dalam widget Text
        with open('data_pelanggan/riwayat_pembeli.txt', 'r') as file:
            isi_teks = file.read()
            self.text_widget.insert('5.0', isi_teks)

        # Menambahkan scrollbar vertikal
        scrollbar = Scrollbar(self.window_RiwayatStrukPembeli, orient=VERTICAL, command=self.text_widget.xview)
        scrollbar.place(x=1265, y=141, height=436, width=15)
        self.text_widget.config(yscrollcommand=scrollbar.set)

        # Menambahkan tombol "SUBMIT"
        tombol_SUBMIT = Button(self.window_RiwayatStrukPembeli, text="SIMPAN", command=self.simpan_teks,font=("Clear Sans", 15, 'bold'),fg='white',bg='#7D0B00',bd=0,activebackground="#7D0B00",width=18,cursor='hand2')
        tombol_SUBMIT.place(x=530, y=630)

    def simpan_teks(self):
        # Mendapatkan isi teks dari widget Text
        isi_teks = self.text_widget.get('1.0', 'end-1c')

        # Menyimpan isi teks ke dalam file
        with open('data_pelanggan/riwayat_pembeli.txt', 'w') as file:
            file.write(isi_teks)
            showinfo('Pesanan Diterima','Berhasil di simpan')

        self.window_RiwayatStrukPembeli.destroy()
        self.window_histori_penjualan.deiconify()


    def RekapBulanan(self):
        self.window_akunpemilik.withdraw()
        self.window_RiwayatBulanan = Toplevel(self.window_akunpemilik)
        self.window_RiwayatBulanan.geometry('1280x680')

        # Memuat dan menampilkan gambar latar belakang
        img14 = Image.open("tampilan/Rekap Bulanan.png")
        self.FotoRiwayatBulanan = ImageTk.PhotoImage(img14)
        label_gambar = Label(self.window_RiwayatBulanan, image=self.FotoRiwayatBulanan)
        label_gambar.pack(pady=0)

        Kembali = Button(self.window_RiwayatBulanan,text='KEMBALI',bg='#7d0b00', fg="white",borderwidth=0,activebackground='#7d0b00',font=('times new roman',18,'bold'),width=22,cursor='hand2',command=self.DestroyBulanan)
        Kembali.place(x=480, y=615)

        self.workbook = openpyxl.load_workbook('data_rekap_bulanan/Rekap Bulanan.xlsx')
        self.sheet = self.workbook.active

        # Makanan
        Label(self.window_RiwayatBulanan,text=self.sheet['A1'].value,bg='white',font=('Times new roman',18,'bold')).place(x=400,y=207)
        Label(self.window_RiwayatBulanan,text=self.sheet['A2'].value,bg='white',font=('Times new roman',18,'bold')).place(x=400,y=235)
        Label(self.window_RiwayatBulanan,text=self.sheet['A3'].value,bg='white',font=('Times new roman',18,'bold')).place(x=400,y=235+28)
        Label(self.window_RiwayatBulanan,text=self.sheet['A4'].value,bg='white',font=('Times new roman',18,'bold')).place(x=400,y=235+28*2)
        Label(self.window_RiwayatBulanan,text=self.sheet['A5'].value,bg='white',font=('Times new roman',18,'bold')).place(x=400,y=235+28*3)
        Label(self.window_RiwayatBulanan,text=self.sheet['A6'].value,bg='white',font=('Times new roman',18,'bold')).place(x=400,y=235+28*4)
        Label(self.window_RiwayatBulanan,text=self.sheet['A7'].value,bg='white',font=('Times new roman',18,'bold')).place(x=400,y=235+28*5)
        Label(self.window_RiwayatBulanan,text=self.sheet['A8'].value,bg='white',font=('Times new roman',18,'bold')).place(x=400,y=235+28*6)
        Label(self.window_RiwayatBulanan,text=self.sheet['A9'].value,bg='white',font=('Times new roman',18,'bold')).place(x=400,y=235+28*7)

        # Minuman
        Label(self.window_RiwayatBulanan,text=self.sheet['B1'].value,bg='white',font=('Times new roman',18,'bold')).place(x=800,y=207)
        Label(self.window_RiwayatBulanan,text=self.sheet['B2'].value,bg='white',font=('Times new roman',18,'bold')).place(x=800,y=235)
        Label(self.window_RiwayatBulanan,text=self.sheet['B3'].value,bg='white',font=('Times new roman',18,'bold')).place(x=800,y=235+28*1)
        Label(self.window_RiwayatBulanan,text=self.sheet['B4'].value,bg='white',font=('Times new roman',18,'bold')).place(x=800,y=235+28*2)
        Label(self.window_RiwayatBulanan,text=self.sheet['B5'].value,bg='white',font=('Times new roman',18,'bold')).place(x=800,y=235+28*3)
        Label(self.window_RiwayatBulanan,text=self.sheet['B6'].value,bg='white',font=('Times new roman',18,'bold')).place(x=800,y=235+28*4)
        Label(self.window_RiwayatBulanan,text=self.sheet['B7'].value,bg='white',font=('Times new roman',18,'bold')).place(x=800,y=235+28*5)
        Label(self.window_RiwayatBulanan,text=self.sheet['B8'].value,bg='white',font=('Times new roman',18,'bold')).place(x=800,y=235+28*6)

        # Jajan
        Label(self.window_RiwayatBulanan,text=self.sheet['C1'].value,bg='white',font=('Times new roman',18,'bold')).place(x=1150,y=207)
        Label(self.window_RiwayatBulanan,text=self.sheet['C2'].value,bg='white',font=('Times new roman',18,'bold')).place(x=1150,y=235)
        Label(self.window_RiwayatBulanan,text=self.sheet['C3'].value,bg='white',font=('Times new roman',18,'bold')).place(x=1150,y=235+28*1)
        Label(self.window_RiwayatBulanan,text=self.sheet['C4'].value,bg='white',font=('Times new roman',18,'bold')).place(x=1150,y=235+28*2)
        Label(self.window_RiwayatBulanan,text=self.sheet['C5'].value,bg='white',font=('Times new roman',18,'bold')).place(x=1150,y=235+28*3)
        Label(self.window_RiwayatBulanan,text=self.sheet['C6'].value,bg='white',font=('Times new roman',18,'bold')).place(x=1150,y=235+28*4)
        Label(self.window_RiwayatBulanan,text=self.sheet['C7'].value,bg='white',font=('Times new roman',18,'bold')).place(x=1150,y=235+28*5)
        Label(self.window_RiwayatBulanan,text=self.sheet['C8'].value,bg='white',font=('Times new roman',18,'bold')).place(x=1150,y=235+28*6)

        self.current_month = self.get_current_month()

        # Membuat label untuk menampilkan nama bulan
        label_month = ttk.Label(self.window_RiwayatBulanan, text=self.current_month,background='#ffb4ae',font=('times new roman',20,'bold')).place(x=701, y=92)

    def get_current_month(self):
        self.now = datetime.now()
        return self.now.strftime("%B").upper()
    def DestroyBulanan(self):
        self.window_RiwayatBulanan.destroy()
        self.window_akunpemilik.deiconify()





