from tkinter import *
root = Tk()
miFrame = Frame(root, width=500, height= 400)
miFrame.pack()
#miImagen = PhotoImage(file="")
miLabel= Label(miFrame, text="Hola hijueputas", fg= "red", font=("Comic Sans MS", 18))
miLabel.place(x= 100, y= 200)
root.mainloop()