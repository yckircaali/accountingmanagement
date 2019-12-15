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
        self.heading = Label(master, text="Stok", font=('arial 30 bold'))
        self.heading.place(x=400, y=0)

        self.id_le = Label(master, text="ID", font=('arial 15 bold'))
        self.id_le.place(x=0, y=70)

        self.id_leb = Entry(master, font=('arial 15 bold') ,width=10)
        self.id_leb.place(x=380, y=70)

        self.btn_search = Button(master, text="Ara", width=15, height=2, command=self.search)
        self.btn_search.place(x=550, y=70)

        self.name_l = Label(master, text="Ürün ismi", font=('arial 15 bold'))
        self.name_l.place(x=0, y=120)

        self.stock_l = Label(master, text="Ürün Adeti", font=('arial 15 bold'))
        self.stock_l.place(x=0, y=170)

        self.sp_l = Label(master, text="Satış Fiyatını Girin", font=('arial 15 bold'))
        self.sp_l.place(x=0, y=220)

        self.vendor_l = Label(master, text="Satıcı Adını Girin", font=('arial 15 bold'))
        self.vendor_l.place(x=0, y=270)

        self.name_e = Entry(master, width=25, font=('arial 15 bold'))
        self.name_e.place(x=380, y=120)

        self.stock_e = Entry(master, width=25, font=('arial 15 bold'))
        self.stock_e.place(x=380, y=170)

        self.sp_e = Entry(master, width=25, font=('arial 15 bold'))
        self.sp_e.place(x=380, y=220)

        self.vendor_e = Entry(master, width=25, font=('arial 15 bold'))
        self.vendor_e.place(x=380, y=270)

        self.btn_add = Button(master, text="Güncelle", width=25, height=2, command=self.update)
        self.btn_add.place(x=470, y=320)
    
    def search(self, *args, **kwargs):
        sql = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(), ))
        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
            self.n4 = r[4]
            self.n8 = r[8]
        conn.commit()

        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.n1))

        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n2))

        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n4))

        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n8))

    def update(self, *args, **kwargs):
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u4 = self.sp_e.get()
        self.u7 = self.vendor_e.get()
        query = "UPDATE inventory SET name=?, stock=?, sp=?, vendor=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u4, self.u7, self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Başarılı", "Stoklar güncellendi.")

root = Tk()
b = Database(root)
root.geometry("730x400+0+0")
root.title("Stokları güncelle")
root.mainloop()