from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random

conn = sqlite3.connect("C:\Games\store.db")
c = conn.cursor()

date = datetime.datetime.now().date()

products_list = []
product_price = []
product_quantity = []
product_id = []

labels_list = []
class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.left = Frame(master, width=700, height=768)
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=768)
        self.right.pack(side=RIGHT) 

        self.heading = Label(self.left, text="Muhasebe Programı", font=('arial 30 bold'))
        self.heading.place(x=0, y=0)

        self.date_l = Label(self.right, text="Tarih " + str(date), font=('arial 16 bold'))
        self.date_l.place(x=0, y=0)

        self.tproduct = Label(self.right, text="Urunler", font=('arial 18 bold'))
        self.tproduct.place(x=0, y=60)

        self.tquantity = Label(self.right, text="Miktar", font=('arial 18 bold'))
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text="Tutar", font=('arial 18 bold'))
        self.tamount.place(x=500, y=60)

        self.enterid = Label(self.left, text="Ürünün ID'si ", font=('arial 18 bold'))
        self.enterid.place(x=0, y=80)

        self.enteride = Entry(self.left, width=25, font=('arial 18 bold'))
        self.enteride.place(x=190, y=80)
        self.enteride.focus()

        self.search_btn = Button(self.left, text="Ara", width=22, height=2, command=self.ajax)
        self.search_btn.place(x=350, y=120)

        self.productname = Label(self.left, text="", font=('arial 27 bold'))
        self.productname.place(x=0, y=250)

        self.pprice = Label(self.left, text="", font=('arial 27 bold'))
        self.pprice.place(x=0, y=290)

        self.total_l = Label(self.right, text="", font=('arial 40 bold'))
        self.total_l.place(x=0, y=550)

    def ajax(self, *args, **kwargs):
        self.get_id = self.enteride.get()

        query = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id, ))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_price = self.r[4]
            self.get_stock = self.r[2]
        self.productname.configure(text="Ürün isimleri : " + str(self.get_name))
        self.pprice.configure(text="Tutar : " + str(self.get_price))

        self.quantity_l = Label(self.left, text="Adet Giriniz", font=('arial 15 bold'))
        self.quantity_l.place(x=0, y=370)

        self.quantity_e = Entry(self.left, width=25, font=('arial 15 bold'))
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()

        self.discount_l = Label(self.left, text="İndirim Giriniz", font=('arial 15 bold'))
        self.discount_l.place(x=0, y=410)

        self.discount_e = Entry(self.left, width=25, font=('arial 15 bold'))
        self.discount_e.place(x=190, y=410)
        self.discount_e.insert(END, 0)

        self.add_to_cart_btn = Button(self.left, text="Ekle", width=22, height=2, command=self.add_to_cart)
        self.add_to_cart_btn.place(x=350, y=450)

        self.change_l = Label(self.left, text="Ödenen Tutar", font=('arial 15 bold'))
        self.change_l.place(x=0, y=550)

        self.change_e = Entry(self.left, width=25, font=('arial 15 bold'))
        self.change_e.place(x=190, y=550)

        self.change_btn = Button(self.left, text="Paraüstü Hesapla", width=22, height=2, command=self.change_func)
        self.change_btn.place(x=350, y=590)

        self.bill_btn = Button(self.left, text="Satın Al", width=100, height=2, command=self.generate_bill)
        self.bill_btn.place(x=0, y=640)

    def add_to_cart(self, *args, **kwargs):
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Hata", "Envanterinizde eşya yoktur.")
        else:
            self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))
            
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index = 0
            self.y_index = 100
            self.counter = 0
            for self.p in products_list:
                self.tempname = Label(self.right, text=str(products_list[self.counter]), font=('arial 15 bold'))
                self.tempname.place(x=0, y=self.y_index)
                labels_list.append(self.tempname)

                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 15 bold'))
                self.tempqt.place(x=300, y=self.y_index)
                labels_list.append(self.tempqt)

                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 15 bold'))
                self.tempprice.place(x=500, y=self.y_index)
                labels_list.append(self.tempprice)

                self.y_index += 40
                self.counter += 1

                self.total_l.configure(text="Tutar : " + str(sum(product_price)))

                self.quantity_l.place_forget()
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.destroy()

                self.enteride.focus()
                self.enteride.delete(0, END)

    def change_func(self, *args, **kwargs):
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(product_price))

        self.to_give = self.amount_given - self.our_total

        self.c_amount = Label(self.left, text="-" + str(self.to_give), font=('arial 15 bold'))
        self.c_amount.place(x=0 , y=600)

    def generate_bill(self, *args, **kwargs):
        self.x = 0

        initial = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(initial, (product_id[self.x], ))

        for i in products_list:
            for r in result:
                self.old_stock = r[2]
            self.new_stock = int(self.old_stock) - int(product_quantity[self.x])

            sql = "UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql, (self.new_stock, product_id[self.x]))
            conn.commit()

            sql2 = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES (?, ?, ?, ?)"
            c.execute(sql2, (products_list[self.x], product_quantity[self.x], product_price[self.x], date))
            conn.commit()

            self.x += 1

        for a in labels_list:
            a.destroy()

        del(products_list[:])
        del(product_id[:])
        del(product_quantity[:])
        del(product_price[:])

        self.total_l.configure(text="")
        self.c_amount.configure(text="")
        self.change_e.delete(0, END)
        self.enteride.focus()
        tkinter.messagebox.showinfo("Basarili", "Satin alim tamamlanmistir.")

root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.title("Muhasebe Programı")
root.mainloop()