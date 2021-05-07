import os
import subprocess
from tkinter import Tk, Label, PhotoImage, ttk, Frame, Entry, Button

root = Tk()
root.title("Graphic-Tab-Config")
root.geometry('600x600')

myIcon = PhotoImage(file = '/usr/local/bin/gtc-scripts/images/icon.png')
root.iconphoto(False, myIcon)

myNotebook = ttk.Notebook(root)
myNotebook.pack(fill = 'both')

PadTab = Frame(myNotebook)
StylusTab = Frame(myNotebook)

myNotebook.add(PadTab, text = "Pad")
myNotebook.add(StylusTab, text = "Stylus")

PadTabFrame = Frame(PadTab)
PadTabFrame.grid(row = 0, column = 0)


Label(PadTabFrame, text = "Enter the model name:").grid(row = 0, column = 0)

modelName = Entry(PadTabFrame, width = 30)
modelName.grid(row = 0, column = 1)

activeButtons = []

def confFile(model):
	if os.path.exists(f"/usr/share/X11/xorg.conf.d/99-huion{model}.conf"):
		out = subprocess.run(['bash', '/usr/local/bin/gtc-scripts/listButtons.sh'], stdout=subprocess.PIPE)
		activeButtons = out.stdout.decode('utf-8').strip().split('\n')

		args = []
		# userName = subprocess.run(['whoami'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
		
		if os.path.exists(f'/home/pagal/.graphic-tab-config'):
			with open(f"/home/pagal/.graphic-tab-config", "r") as fh:
				args = fh.readline().strip().replace('"', '').split(' ')

			count = 0	
			config = []
			for i in args:
				num = int(i.split(':')[0])
				conf = i.split(':')[1]
				Label(PadTabFrame, text = f'Button {num}').grid(row = count + 2, column = 0)
				temp = Entry(PadTabFrame)
				temp.grid(row = count + 2, column = 1)
				temp.insert(0, f'{conf}')
				config.append(temp)
				count += 1
			
			def updateConfig():
				x = 0
				dotfile = ''
				for i in activeButtons:
					dotfile += f'"{i}:{config[x].get()}" '
					x += 1

				with open(f'/home/pagal/.graphic-tab-config', "w") as fh:
					fh.write(dotfile)
				
				subprocess.run(['bash', '/usr/local/bin/gtc-scripts/setButtons.sh', dotfile])
			
			saveBtn = Button(PadTabFrame, text = 'Save', command = lambda: updateConfig() )
			saveBtn.grid(row = count + 2, column = 0)

	else:
		with open(f"/usr/share/X11/xorg.conf.d/99-huion{model}.conf", "w") as fh:
			fh.write(f'Section "InputClass"\n\tIdentifier "Huion tablets with Wacom driver"\n\tMatchUSBID "256c:006d*"\n\tMatchIsTablet "true"\n\tMatchDevicePath "/dev/input/event*"\n\tDriver "wacom"\nEndSection\n\t')
	
		with open(f'/etc/init.d/gtc-onboot.sh', "w") as fh:
			fh.write('bash /usr/local/bin/gtc-scripts/setButtons.sh "$(cat /home/pagal/.graphic-tab-config)"')
		os.chmod('/home/pagal/.graphic-tab-config', 0o777)
		
		os.system('sudo chmod +x /etc/init.d/gtc-onboot.sh')
		os.system('sudo systemctl restart display-manager')

Button(PadTabFrame, text = "Proceed", command = lambda:confFile(modelName.get())).grid(row = 1, column = 0, columnspan = 2)


root.mainloop()