from tkinter import *

import copy



# Backend
def Main_Copy(app):
    app.clipboard_clear()
    app.clipboard_append(copy_value.get())
def GO_copy():
    read_able_data = open("GBD.txt",'r')
    data = read_able_data.read()
    data = data.replace(replce_namevar.get(),namevar.get())
    copy_value.set(data)
    read_able_data.close()
    chikit.set(1)


def resetx(app,nm,rn):
    app.clipboard_clear()
    nm.delete(0, END)
    rn.delete(0, END)
    rn.insert(0,"#")
    copy_value.set("")
    chikit.set(0)



def Add_edit_window(app,data):
    app.destroy()
    file = open("GBD.txt", 'w')
    file.write(data)
    file.close()

def clear_edit_window(app):
    app.destroy()
    file = open("GBD.txt", 'w')
    file.close()



def Open_edit(app):
    read_able_data = open("GBD.txt",'r')
    edit_window = Toplevel(app)
    edit_window.geometry("800x600")
    edit_window.title("Edit")
    textArea = Text(edit_window,height=30,width=80)
    textArea.insert(END,read_able_data.read())
    textArea.pack(pady=10)
    add = Button(edit_window,text="Add",width=20,command = lambda : Add_edit_window(edit_window,textArea.get(1.0, "end-1c")))
    add.pack(side=LEFT,padx=160)
    delete = Button(edit_window,text="Clear",width=20,command= lambda: clear_edit_window(edit_window))
    delete.pack(side=LEFT)
    read_able_data.close()



#Forntendt



app = Tk()
namevar = StringVar()
namevar.set("")
replce_namevar = StringVar()
replce_namevar.set("")
chikit = IntVar()
copy_value = StringVar()


app.geometry("500x250")

app.resizable(False,False)
p = PhotoImage(file='ico.png')
app.iconphoto(False,p)
app.title("Galorant")
frame1 = Frame(app,height=200,width=275)
frame1.config(bg="black")
frame2 = Frame(app,height=200,width=225)
frame2.config(bg="black")
frame1.pack(expand=True,fill=BOTH,side=LEFT)
name = Entry(frame1,background="white",width=17,textvariable=namevar,font=('Arial 18'))
name.place(x=40,y=50)
relace_name = Entry(frame1,background="white",text="#",width=7,textvariable=replce_namevar,justify=CENTER,font=('Arial 15 bold'))
relace_name.place(x=40,y=110)
relace_name.insert(0,"#")
chikit.set(0)
replace_button = Checkbutton(frame1,text=" '.'",variable=chikit,onvalue=1,offvalue=0,background="#9F9FA3",width=4,font=('Arial 10 bold'),state=DISABLED).place(x=128,y=110)
Add_button = Button(frame1,text="Edit",background="#9F9FA3",width=7,font=('Arial 10'),command=lambda: Open_edit(app)).place(x=200,y=110)
clear_button = Button(frame1,text="Reset",background="#9F9FA3",font=('Arial 10 bold'),width=13,command=lambda :resetx(app,name,relace_name)).place(x=40,y=170)
go_button = Button(frame1,text="GO",foreground="white",background="#7F1416",command=lambda : GO_copy(),font=('Arial 10 bold'),width=12).place(x=160,y=170)
frame2.pack(expand=True,fill=BOTH,side=RIGHT)
Cp_button = Button(frame2,text="Copy",font=('Arial 30 bold'),background="#7F1416",foreground="white",height=3,width=7,command=lambda:Main_Copy(app),highlightbackground="black",bd=3,highlightthickness=2)
Cp_button.place(x=10,y=30)

app.mainloop()
