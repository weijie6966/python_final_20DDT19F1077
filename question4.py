from tkinter import*

def changedtext():
    if(txt_lal.cget("text")=="Changed Text"):
        txt_lal.config(text="I have been changed")
    else:
        txt_lal.config(text="Changed Text")

window=Tk()
window.geometry('250x150')
window.title("GUI Example")

window.minsize(width=250,height=150)
window.maxsize(width=250,height=150) 

frame=Frame(window,bg="red")
frame.pack(padx=10,pady=50)
btn=Button(window,text="Changed Text" ,command=changedtext)
btn.pack()

txt_lal=Label(window,text="Changed Text")
txt_lal.pack()

window.mainloop()