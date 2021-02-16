from tkinter import messagebox


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