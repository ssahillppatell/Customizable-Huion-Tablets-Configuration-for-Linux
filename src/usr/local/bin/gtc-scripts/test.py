from tkinter import Tk, Frame, Label, ttk, Button

def w2(root):
	frame1.destroy()
	frame2 = Frame(root)
	frame2.grid(row = 0, column = 0)
	Label(frame2, text = 'Hello W2').grid(row = 0, column = 0)
	Button(frame2, text = 'Change', command = lambda:w1(root)).grid(row = 1, column = 0)
	# Label(root, text = 'Hello W2').grid(row = 0, column = 0)


def w1(root):
	global frame1
	frame1 = Frame(root)
	frame1.grid(row = 0, column = 0)
	Label(frame1, text = 'Hello W1').grid(row = 0, column = 0)
	Button(frame1, text = 'Change', command = lambda:w2(root)).grid(row = 1, column = 0)

root = Tk()
root.title('Test')

w1(root)

root.mainloop()