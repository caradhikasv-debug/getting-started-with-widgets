from tkinter import *
window=Tk()
window.title("getting started with widgets")
window.geometry("400x300")
lbl=Label(window,text="hello",fg="white",bg="blue",height=1,width=300)
lbl.pack()
namelbl=Label(window,text="Full Name",fg="white",bg="blue")
namelbl.pack()
nameentry=Entry(window)
nameentry.pack()
def display():
    name=nameentry.get()
    global message
    message="welcome to the application\n"
    greet="hello "+name+"\n"
    textbox.insert(END,greet)
    textbox.insert(END,message)
Btn=Button(window,text="Begin",command=display)
Btn.pack()
textbox=Text(window,height=3)
textbox.pack()
window.mainloop()