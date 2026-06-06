from tkinter import *
from menu_utama import MenuUtamaMixin
from pemilik import PemilikMixin
from pelanggan import PelangganMixin
from pegawai import PegawaiMixin

class Starboy(MenuUtamaMixin, PemilikMixin, PelangganMixin, PegawaiMixin):
    Jajan1 = 0
    Jajan2 = 0
    Jajan3 = 0
    Jajan4 = 0
    Jajan5 = 0
    Jajan6 = 0
    Jajan7 = 0
    Jajan8 = 0
    Minuman1 = 0
    Minuman2 = 0
    Minuman3 = 0
    Minuman4 = 0
    Minuman5 = 0
    Minuman6 = 0
    Minuman7 = 0
    Minuman8 = 0
    Makanan1 = 0
    Makanan2 = 0
    Makanan3 = 0
    Makanan4 = 0
    Makanan5 = 0
    Makanan6 = 0
    Makanan7 = 0
    Makanan8 = 0
    Makanan9 = 0

    # __init__ akan dipanggil dari MenuUtamaMixin

if __name__ == "__main__":
    root = Tk()
    aplikasi = Starboy(root)
    root.mainloop()
