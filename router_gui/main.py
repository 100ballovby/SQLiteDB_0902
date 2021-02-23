from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview


def populate_list(tree_view, db, hostname=''):
    for i in tree_view.get_children():
        tree_view.delete(i)
    for row in db.fetch(hostname):
        tree_view.insert('', 'end', values=row)


def populate_list2(tree_view, db, query='SELECT * FROM routers'):
    for i in tree_view.get_children():
        tree_view.delete(i)
    for row in db.fetch2(query):
        tree_view.insert('', 'end', values=row)


def clear_text():
    pass


def add_router(brand, host, ram, flash, db):
    if brand.get() == '' or host.get() == '' or ram.get() == '' or flash.get() == '':
        messagebox.showerror('Обязательные поля!', 'Пожалуйста, заполните все поля.')
        return
    db.insert(host.get(), brand.get(), ram.get(), flash.get())
    clear_text()
    populate_list()

app = Tk()
frame_search = Frame(app)
frame_search.grid(row=0, column=0)

lbl_search = Label(frame_search, text='Искать по названию',
                   font=('bold', 14), pady=20)
lbl_search.grid(row=0, column=0, sticky=W)

hostname_search = StringVar()
hostname_search_entry = Entry(frame_search, textvariable=hostname_search)
hostname_search_entry.grid(row=0, column=1, sticky=W)

query_search = StringVar()
query_search.set("SELECT * FROM routers WHERE ram > 1024")
query_search_entry = Entry(frame_search,
                           textvariable=query_search,
                           width=40)
query_search_entry.grid(row=1, column=1)

# FRAME for db
frame_fields = Frame(app)
frame_fields.grid(row=1, column=0)

# hostname
hostname_text = StringVar(value='Cisco')
hostname_label = Label(frame_fields, text='Имя Хоста', font=('bold', 14))
hostname_label.grid(row=0, column=0)
hostname_entry = Entry(frame_fields, textvariable=hostname_text)
hostname_entry.grid(row=0, column=1)

# brand
brand_text = StringVar(value='Cisco')
brand_label = Label(frame_fields, text='Бренд', font=('bold', 14))
brand_label.grid(row=0, column=2)
brand_entry = Entry(frame_fields, textvariable=brand_text)
brand_entry.grid(row=0, column=3)

# RAM
ram_text = IntVar(value=1024)
ram_label = Label(frame_fields, text='Оперативная память', font=('bold', 14))
ram_label.grid(row=1, column=0)
ram_entry = Entry(frame_fields, textvariable=ram_text)
ram_entry.grid(row=1, column=1)

# FLASH
flash_text = IntVar(value=256)
flash_label = Label(frame_fields, text='Flash память', font=('bold', 14))
flash_label.grid(row=1, column=2)
flash_entry = Entry(frame_fields, textvariable=flash_text)
flash_entry.grid(row=1, column=3)

app.mainloop()
