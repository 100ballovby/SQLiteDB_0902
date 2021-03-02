from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from database import Database

db = Database('shop.db', tn='routers')


def populate_list(hostname=''):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in db.fetch(hostname):
        router_tree_view.insert('', 'end', values=row)


def populate_list2(query='SELECT * FROM routers'):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in db.fetch2(query):
        router_tree_view.insert('', 'end', values=row)


def clear_text():
    brand_entry.delete(0, END)
    hostname_entry.delete(0, END)
    ram_entry.delete(0, END)
    flash_entry.delete(0, END)


def add_router():
    if brand_text.get() == '' or hostname_text.get() == '' or ram_text.get() == '' or flash_text.get() == '':
        messagebox.showerror('Обязательные поля!', 'Пожалуйста, заполните все поля.')
        return
    db.insert(hostname_text.get(), brand_text.get(), ram_text.get(), flash_text.get())
    clear_text()
    populate_list()


def select_router(event):
    try:
        global selected_item
        index = router_tree_view.selection()[0]
        selected_item = router_tree_view.item(index)['values']
        hostname_entry.delete(0, END)
        hostname_entry.insert(END, selected_item[1])
        brand_entry.delete(0, END)
        brand_entry.insert(END, selected_item[2])
        ram_entry.delete(0, END)
        ram_entry.insert(END, selected_item[3])
        flash_entry.delete(0, END)
        flash_entry.insert(END, selected_item[4])
    except IndexError:
        messagebox.showwarning('Несуществующее значение!', 'Вы пытаетесь получить доступ к объекту, которого нет!')


def delete_router():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_router():
    db.update(selected_item[0], hostname_text.get(), brand_text.get(),
              ram_text.get(), flash_text.get())
    populate_list()


def search_hostname():
    hostname = hostname_search.get()
    populate_list(hostname)


def execute_query():
    query = query_search.get()
    populate_list2(query)

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

frame_router = Frame(app)
frame_router.grid(row=4, column=0, columnspan=4,
                  rowspan=6, pady=20, padx=20)
columns = ['id', 'hostname', 'Brand', 'RAM', 'Flash']
router_tree_view = Treeview(frame_router, columns=columns, show='headings')
router_tree_view.column('id', width=30)

for col in columns[1:]:
    router_tree_view.column(col, width=120)
    router_tree_view.heading(col, text=col)

router_tree_view.bind('<<TreeviewSelect>>', select_router)
router_tree_view.pack(side='left', fill='y')

# КНОПКИ
frame_btns = Frame(app)
frame_btns.grid(row=3, column=0, pady=30)

add_btn = Button(frame_btns, text="Add router",
                 width=12, command=add_router)
add_btn.grid(row=0, column=1)

remove_btn = Button(frame_btns, text="Remove router",
                    width=12, command=delete_router)
remove_btn.grid(row=0, column=2)

update_btn = Button(frame_btns, text="Update router",
                    width=12, command=update_router)
update_btn.grid(row=0, column=3)

clear_btn = Button(frame_btns, text="Clear Input",
                   width=12, command=clear_text)
clear_btn.grid(row=1, column=1)

search_btn = Button(frame_btns, text="Search",
                    width=12, command=search_hostname)
search_btn.grid(row=1, column=2)

search_query = Button(frame_btns, text="Search Query",
                      width=12, command=execute_query)
search_query.grid(row=1, column=3)

populate_list()
app.mainloop()
