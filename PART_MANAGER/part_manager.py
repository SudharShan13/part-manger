from tkinter import *

from db import Database

from tkinter import messagebox



db = Database('store.db')



def populate_list():

    patrs_list.delete(0,END);

    for row in db.fetch():

        patrs_list.insert(END,row);



def add_item():

    if part_text.get()== '' or customer_text.get()== '' or retailer_text.get()=='' or price_text.get()=='' :

        messagebox.showerror('Required Fields','Please include all fields')

        return

    db.insert(part_text.get(),customer_text.get(),retailer_text.get(),price_text.get())

    patrs_list.delete(0,END);

    patrs_list.insert(END,(part_text.get(),customer_text.get(),retailer_text.get(),price_text.get()))

    clear_text();

    populate_list();



def remove_item():

    select_item()

    db.remove(selected_item[0])

    clear_text()

    populate_list()



def update_item():

    part = part_text.get()

    cust = customer_text.get()

    retailer = retailer_text.get()

    price = price_text.get()

    select_item()

    db.update(selected_item[0], part, cust, retailer, price)

    populate_list()



def clear_text():

    part_entry.delete(0,END)

    customer_entry.delete(0,END)

    retailer_entry.delete(0,END)

    price_entry.delete(0,END)



def select_item():

    global selected_item;

    index = patrs_list.curselection()[0]

    selected_item = patrs_list.get(index)

    

    part_entry.delete(0,END)

    part_entry.insert(END,selected_item[1])

    customer_entry.delete(0,END)

    customer_entry.insert(END,selected_item[2])

    retailer_entry.delete(0,END)

    retailer_entry.insert(END,selected_item[3])

    price_entry.delete(0,END)

    price_entry.insert(END,selected_item[4])













app = Tk();











part_text=StringVar()

part_label=Label(app,text='Part Name:',font=('bold',14),pady=20)

part_label.grid(row=0,column=0,sticky=W);

part_entry=Entry(app,textvariable=part_text)

part_entry.grid(row=0,column=1)





customer_text=StringVar()

customer_label=Label(app,text='Customer Name:',font=('bold',14),padx=20)

customer_label.grid(row=0,column=2,sticky=E);

customer_entry=Entry(app,textvariable=customer_text)

customer_entry.grid(row=0,column=3)





retailer_text=StringVar()

retailer_label=Label(app,text='Retailer:',font=('bold',14))

retailer_label.grid(row=1,column=0,sticky=W);

retailer_entry=Entry(app,textvariable=retailer_text)

retailer_entry.grid(row=1,column=1)





price_text=StringVar()

price_label=Label(app,text='Price:',font=('bold',14),padx=20)

price_label.grid(row=1,column=2,sticky=W);

price_entry=Entry(app,textvariable=price_text)

price_entry.grid(row=1,column=3)





patrs_list=Listbox(app,height=8,width=50,border=0)

patrs_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20,padx=20)



scrollbar=Scrollbar(app)

scrollbar.grid(row=3,column=3)



patrs_list.configure(yscrollcommand=scrollbar.set)

scrollbar.configure(command=patrs_list.yview)







patrs_list.bind('<<ListBoxSelect>>',select_item);











add_btn=Button(app,text='addpart',width=12,command=add_item)

add_btn.grid(row=2,column=0,pady=20)



remove_btn=Button(app,text='Remove part',width=12,command=remove_item)

remove_btn.grid(row=2,column=1)



update_btn=Button(app,text='Update part',width=12,command=update_item)

update_btn.grid(row=2,column=2)



clear_btn=Button(app,text='Clear part',width=12,command=clear_text)

clear_btn.grid(row=2,column=3,pady=20)







app.title('part Manager');

app.geometry('700x350');





populate_list();





app.mainloop();