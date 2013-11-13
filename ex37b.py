#
# listdir.py
#
# This script creates a listbox which enables the user
# to see files in any folder on the system
#
# First we need to import some modules
#
import os
from time import sleep
from Tkinter import *
#
# We create a DirList class
#
class DirList:
#
# This code creates the GUI
#
	def __init__(self,initdir=None):
		self.top = Tk()
		self.label = Label(self.top, text = 'Directory Lister' + ' v1.1')
		self.label.pack()
		
		self.cwd = StringVar(self.top)
		
		self.dir1 = Label(self.top, fg = 'green', font = ('Helvetica', 12, 'bold'))
		self.dir1.pack()
		
		self.dirfm = Frame(self.top)
		self.dirsb = Scrollbar(self.dirfm)
		self.dirsb.pack(side = RIGHT, fill = Y)
		self.dirs = Listbox(self.dirfm, height = 15, width = 50, yscrollcommand = self.dirsb.set)
		self.dirs.bind('<Double-1>',self.setDirAndGo)
		self.dirsb.config(command=self.dirs.yview)
		self.dirs.pack(side=LEFT, fill=BOTH)
		self.dirfm.pack()
		
		self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
		self.dirn.bind('<RETURN>', self.doLS())
		self.dirn.pack()
		
		self.bfm = Frame(self.top)
		self.clr = Button(self.bfm, text='Clear', command=self.clrDir, activeforeground='white',activebackground='blue')
		self.ls  = Button(self.bfm, text='List Directory', command=self.doLS, activeforeground='white', activebackground='green')
		self.quit= Button(self.bfm, text='Quit',command=self.top.quit,activeforeground='white',activebackground='red')
		self.clr.pack(side=LEFT)
		self.ls.pack(side=LEFT)
		self.quit.pack(side=LEFT)
		self.bfm.pack()
		
		if initdir:
			self.cwd.set(os.curdir)
			self.doLS()
#
# Now we create some functions that we have bound to some of the widgets described above.
#
# The clrDir function clears the directory information.
#
	def clrDir(self, ev=None):
		self.cwd.set('')
#
# This is a setup function.
#
	def setDirAndGo(self, ev=None):
		self.last = self.cwd.get()
		self.dirs.config(selectbackground='red')
		check = self.dirs.get(self.dirs.curselection())
		if not check:
			check = os.curdir
		self.cwd.set(check)
		self.doLS()
#
# This function gets the directory information.
#
	def doLS(self, ev=None):
		error = ''
		tdir = self.cwd.get()
		if not tdir: tdir = os.curdir
		
		if not os.path.exists(tdir):
			error = tdir + ': no such file'
		elif not os.path.isdir(tdir):
			error = tdir + ': no a directory'
			
		if error:
			self.cwd.set(error)
			self.top.update()
			sleep(2)
			if not (hasattr(self, 'last') and self.last):
				self.last = os.curdir
			self.cwd.set(self.last)
			self.dirs.config(\
				selectbackground = 'LightSkyBlue')
			self.top.update()
			return
			
		self.cwd.set('FETCHING DIRECTORY CONTENTS...')
		self.top.update()
		dirlist = os.listdir(tdir)
		dirlist.sort()
		os.chdir(tdir)
		self.dir1.config(text=os.getcwd())
		self.dirs.delete(0,END)
		self.dirs.insert(END,os.curdir)
		self.dirs.insert(END,os.pardir)
		for eachFile in dirlist:
			self.dirs.insert(END,eachFile)
		self.cwd.set(os.curdir)
		self.dirs.config(selectbackground='LightSkyBlue')
#
# This is the function that starts the program. Note mainloop(). A GUI is,
# essentially a loop that waits for the user to do something.
#
def main():
	d = DirList(os.curdir)
	mainloop()
		
if __name__ == '__main__':
	main()
		