# import tkinter
# print("Hello World! Tkinter")

# window = tkinter.Tk()
# window.title("GUI")
# tkinter.Label(window, text = "Hello World!").pack()
# window.mainloop()

import os
import sys
import subprocess

model = input("Enter your model name: ")

if os.path.exists(f"/usr/share/X11/xorg.conf.d/99-huion{model}.conf"):
	out = subprocess.run(['bash', './listButtons.sh'], stdout=subprocess.PIPE)
	activeButtons = out.stdout.decode('utf-8').strip().split('\n')

	newConfig = {}
	for button in activeButtons:
		temp = input(f'Enter the configuration for button {button}: ')
		newConfig[button] = temp
	
	args = ''
	for key, value in newConfig.items():
		args += f'"{key}:{value}" '
	
	print(args)
	subprocess.run(['bash', './setButtons.sh', args])
else:
	with open(f"/usr/share/X11/xorg.conf.d/99-huion{model}.conf", "w") as fh:
		fh.write(f'Section "InputClass"\n\tIdentifier "Huion tablets with Wacom driver"\n\tMatchUSBID "256c:006d*"\n\tMatchIsTablet "true"\n\tMatchDevicePath "/dev/input/event*"\n\tDriver "wacom"\nEndSection\n\t')
	
	os.system('sudo systemctl restart display-manager')