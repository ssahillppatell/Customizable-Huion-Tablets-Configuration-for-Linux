import tkinter
print("Hello World! Tkinter")

window = tkinter.Tk()
window.title("GUI")
tkinter.Label(window, text = "Hello World!").pack()
window.mainloop()