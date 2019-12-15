from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("C:\Games\store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]
class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Ürün Ekle", font=('arial 30 bold'))
        self.heading.place(x=200, y=0)

        self.name_l = Label(master, text="Ürün Adı", font=('arial 15 bold'))
        self.name_l.place(x=0, y=70)

        self.stock_l = Label(master, text="Ürün Stok", font=('arial 15 bold'))
        self.stock_l.place(x=0, y=120)

        self.sp_l = Label(master, text="Satış Fiyatı", font=('arial 15 bold'))
        self.sp_l.place(x=0, y=170)

        self.vendor_l = Label(master, text="Satıcı Adı", font=('arial 15 bold'))
        self.vendor_l.place(x=0, y=220)

        self.id_l = Label(master, text="ID", font=('arial 15 bold'))
        self.id_l.place(x=0, y=270)

        self.name_e = Entry(master, width=25, font=('arial 15 bold'))
        self.name_e.place(x=180, y=70)

        self.stock_e = Entry(master, width=25, font=('arial 15 bold'))
        self.stock_e.place(x=180, y=120)

        self.sp_e = Entry(master, width=25, font=('arial 15 bold'))
        self.sp_e.place(x=180, y=170)

        self.vendor_e = Entry(master, width=25, font=('arial 15 bold'))
        self.vendor_e.place(x=180, y=220)

        self.id_e = Entry(master, width=25, font=('arial 15 bold'))
        self.id_e.place(x=180, y=270)

        self.btn_add = Button(master, text="Ürün Ekle", width=25, height=2, command=self.get_items)
        self.btn_add.place(x=270, y=320)

        self.btn_clear = Button(master, text="Temizle", width=18, height=2, command=self.clear_all)
        self.btn_clear.place(x=100, y=320)

        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Up>', self.clear_all)
    def get_items(self, *args, **kwargs):
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()

        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("HATA", "Tüm Alanları Doldurunuz")
        else:
            sql = "INSERT INTO inventory (name, stock, sp, vendor,) VALUES(?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.sp, self.vendor,))
            conn.commit()
            tkinter.messagebox.showinfo("Başarılı", "Ürün Eklendi.")

    def clear_all(self, *args, **kwargs):
        num = id + 1
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)

root = Tk()
b = Database(root)
root.geometry("480x400+0+0")
root.title("Ürün Ekle")
root.mainloop()