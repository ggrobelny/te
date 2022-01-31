#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.colorchooser, tkinter.messagebox
from tkinter.filedialog import *
import tkinter.scrolledtext as sc
from tkfontchooser import askfont
import re
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import ttk

root = Tk()
#root.geometry('1920x1080')
f=tk.Frame(root)
tv=ttk.Treeview(f,show='tree')
xbar=tk.Scrollbar(f,orient=tk.VERTICAL, command=tv.yview)
tv.configure(yscroll=xbar.set)
directory='/home/'
tv.heading('#0',text='Dir：'+directory)
path=os.path.abspath(directory)
node=tv.insert('','end',text=path,open=True)
def traverse_dir(parent,path):
    for d in os.listdir(path):
        full_path=os.path.join(path,d)
        isdir = os.path.isdir(full_path)
        id=tv.insert(parent,'end',text=d,open=False)
        if isdir:
            traverse_dir(id,full_path)
traverse_dir(node,path)
xbar.pack(side=tk.RIGHT,fill=tk.Y)
tv.pack()
f.pack(ipadx=3, ipady=3, side="left", expand=True, fill="both")

class main:
	def __init__(self,master):
		self.master = master
		self.filename = 'y4ns.y4'
		self.updateTitle()
		self.widgets()
		self.menubar()
#		self.Treeview()

	def updateTitle(self):
		print(self.filename)
		self.master.title(self.filename+": "+'custom editor')

#Menu

	def menubar(self):
		self.menu = Menu(root, bd=2, background="#34596b", activebackground='#091b3a', activeforeground='#d6bf33')
		self.master.config(menu=self.menu)
		filemenu = Menu(self.menu, background="#a52a2a", activebackground='#091b3a', activeforeground='#d6bf33')
		self.menu.add_cascade(label="File", menu=filemenu, font=("Ubuntu", 10, "bold"), background="#34596b", foreground="#d6bf33")
		filemenu.add_command(label="New", command=self.NewFile, font=("Ubuntu", 10, "bold"), background="#34596b",
							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		filemenu.add_command(label="Open", command=self.opn,font=("Ubuntu", 10, "bold"), background="#34596b",
							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		filemenu.add_command(label="Save", command=self.save,font=("Ubuntu", 10, "bold"), background="#34596b",
							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		filemenu.add_command(label="Save As..", command=self.saveas,font=("Ubuntu", 10, "bold"), background="#34596b",
							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		filemenu.add_separator(background="#34596b")
		filemenu.add_command(label="Exit", command=self.quit, font=("Ubuntu", 10, "bold"), background="#a52a2a",
							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		filemenu.add_separator(background="#34596b")

# Config

		Config = Menu(self.menu, background="#a52a2a", activebackground='#091b3a', activeforeground='#d6bf33')

		self.menu.add_cascade(label="Config", menu=Config, font=("Ubuntu", 10, "bold"), background="#34596b",
							  foreground="#d6bf33")

		Config.add_command(label="Font",command=self.chfont, font=("Ubuntu", 10, "bold"), background="#34596b",
						   foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		Config.add_command(label="Text Color", command=self.txtcolor, font=("Ubuntu", 10, "bold"), background="#34596b",
						   foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		bt = Menu(Config, background="#34596b", activebackground='#091b3a', activeforeground='#d6bf33')

		bt.add_command(label='Classic', command=self.linux, font=("Ubuntu", 10, "bold"), background="#34596b",
					   foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		bt.add_command(label='Peru Yellow', command=self.peru, font=("Ubuntu", 10, "bold"), background="#34596b",
					   foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		bt.add_command(label='Granat', command=self.granat, font=("Ubuntu", 10, "bold"), background="#34596b",
					   foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		bt.add_command(label='Simple', command=self.simple, font=("Ubuntu", 10, "bold"), background="#34596b",
					   foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		bt.add_command(label='Windows Error', command=self.werror, font=("Ubuntu", 10, "bold"), background="#34596b",
					   foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')

		Config.add_cascade(label="Background Theme",menu=bt, font=("Ubuntu", 10, "bold"), background="#a52a2a",
						   foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')


#Edit

		editmenu = Menu(self.menu, background="#a52a2a", activebackground='#091b3a', activeforeground='#d6bf33')
		self.menu.add_cascade(label="Edit", menu=editmenu, font=("Ubuntu", 10, "bold"),
							  background="#34596b", foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		editmenu.add_command(label="Copy", command=self.copy, font=("Ubuntu", 10, "bold"),
							 background="#34596b", foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		editmenu.add_command(label="Cut", command=self.cut, font=("Ubuntu", 10, "bold"),
							 background="#34596b", foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		editmenu.add_command(label="Paste", command=self.paste, font=("Ubuntu", 10, "bold"),
							 background="#34596b", foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		editmenu.add_command(label="Undo", command=self.undo, font=("Ubuntu", 10, "bold"),
							 background="#34596b", foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		editmenu.add_command(label="Redo", command=self.redo, font=("Ubuntu", 10, "bold"),
							 background="#34596b", foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
#

#Help Menu & About

		helpmenu = Menu(self.menu, background="#a52a2a", activebackground='#091b3a', activeforeground='#d6bf33')
		self.menu.add_cascade(label="Help", menu=helpmenu, font=("Ubuntu", 10, "bold"), background="#34596b",
							  foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
		helpmenu.add_command(label="About...", command=self.about, font=("Ubuntu", 10, "bold"), background="#34596b",
							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')

	def linux(self):
		self.ta['insertbackground'] = '#a52a2a'
#		self.ta['insertwidth'] = '5'
#		self.ta['insertborderwidth'] = '5'
		self.ta['bd'] = '5'
		self.ta['bg'] = 'black'
		self.ta['fg'] = 'chartreuse'

	def peru(self):
		self.ta['insertbackground'] = '#FFFF00'
#		self.ta['insertwidth'] = '5'
#		self.ta['insertborderwidth'] = '5'
		self.ta['bg'] = '#CD853F'
		self.ta['fg'] = '#FFFF00'

	def granat(self):
		self.ta['insertbackground'] = '#dd0c39'
#		self.ta['insertwidth'] = '5'
#		self.ta['insertborderwidth'] = '5'
		self.ta['bg'] = '#34596b'
		self.ta['fg'] = 'white'

	def simple(self):
		self.ta['insertbackground'] = '#7baed5'
#		self.ta['insertborderwidth'] = '5'
		self.ta['bg'] = '#838383'
		self.ta['fg'] = '#fff'

	def werror(self):
		self.ta['insertbackground'] = 'white'
#		self.ta['insertwidth'] = '5'
#		self.ta['insertborderwidth'] = '5'
		self.ta['bg'] = 'blue'
		self.ta['fg'] = 'white'


	def quit(self):
		if tkinter.messagebox.askyesno("Save", "Do you want to save the file before closing?"):
			self.save()
		quit()

	def about(self):


		window = Tk()
		window.geometry("600x375")
		window.configure(bg="#838383")

		window.title('text@editor:~$')
		label_1 = Label(window, text="File  Edit  View  Search Terminal  Help",bg="black", fg="white", width="120", height="1", anchor="nw", cursor="circle")
		label_2 = Label(window, text='text@editor:~$', bg="#838383", fg="#7FFF00", font="Ubuntu", width="84", height="1", anchor="nw", cursor="circle")
		label_pad = Label(window, text=" ", bg="#838383", width="84", height="5", anchor="nw", cursor="arrow")
		label_3 = Label(window,pady=(8), text='My name is \nGrzegorz Grobelny\nand i\'m Python \nDeveloper.', bg="#091b3a", fg="#7FFF00",
						font="Ubuntu 20", width="20", height="4", justify="center", bd=3, relief="raised", cursor="plus")

		label_1.pack()
		label_2.pack()
		label_pad.pack()
		label_3.pack()
		window.resizable(False, False)
		window.mainloop()

	def txtcolor(self):
		color = tkinter.colorchooser.askcolor('black')
		if color:
			self.ta['fg'] = color[1]

	def chfont(self):
		font = askfont(self.master)
		if font:
			font['family'] = font['family'].replace(' ', '\ ')
			font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
			if font['underline']:
				font_str += ' underline'
			if font['overstrike']:
				font_str += ' overstrike'
			self.ta['font'] = font_str
			self.ta['cursor'] = 'plus'
			self.ta['height'] = self.ta['height']-font['size']
			self.ta['width'] =  self.ta['width']-font['size']

	def widgets(self):
		self.master.protocol("WM_DELETE_WINDOW",self.quit)
		self.ta = sc.ScrolledText(self.master, height=40,width=100, foreground="#FFDEAD",
			font=("Ubuntu", 20, "normal"), bd=3, relief="sunken", background="#838383", cursor="plus",
			insertbackground = 'white', insertwidth = '5', insertborderwidth = '5', padx = '5', pady = '15')


		self.ta.pack(expand=True, fill=BOTH)

		self.ta.bind('<Control-o>', self.opn)
		self.ta.bind('<Control-n>', self.NewFile)
		self.ta.bind('<Control-s>', self.save)
		self.ta.bind('<Control-a>', self.select_all)
		self.ta.bind('<Control-A>', self.select_all)
		self.ta.bind("<Control-z>", self.undo)
		self.ta.bind("<Control-y>", self.redo)

	def NewFile(self, event=None):
		if tkinter.messagebox.askyesno("New", "Do you want to save the file?"):
			self.save()

		self.ta.delete(0.0, END)
		self.filename = "Untitled"
		self.updateTitle()

	def select_all(self, event=None):
		self.ta.tag_add(SEL, "1.0", END)
		self.ta.focus_set()

	def opn(self, event=None):
		File = str(askopenfilename(title="Open File",filetypes=[("all files", "*.*"),
			('CSS','.css'), ('HTML', '.html'), ('PYTHON', '.py'), ('JS', '.js'), ('PHP', '.php'), ('CSV', '.csv'), ('ASM', '.asm'),
			('SQL', '.sql'), ('TXT', '.txt'), ('BASH', '.bash'), ('SH', '.sh'), ('JSON', '.json'), ('MARKDOWN', 'md')]))

		if len(File) > 0:
			self.ta.delete("1.0", END)
			try:
				f = open(File)
				for line in f:
					self.ta.insert(END, line)
				f.close()
				self.filename = str(File)
				self.updateTitle()
			except IOError:
				tkinter.messagebox.showwarning("Open file", "Cannot open this file...")

	def save(self, event=None):
		if self.filename == 'Untitled':
			self.saveas()
		else:
			f = open(self.filename,"wb")
			text = self.ta.get("1.0", END).encode("utf-8")
			f.write(text)
			f.close()
			self.updateTitle()

	def saveas(self, event=None):
		file=str(asksaveasfilename(title="Save as File",defaultextension=".txt",filetypes=[("all files", "*.*"),
			('CSS', '.css'), ('HTML', '.html'), ('PYTHON', '.py'), ('JS', '.js'), ('PHP', '.php'), ('CSV', '.csv'), ('SH', '.sh'),
			('ASM', '.asm'), ('SQL', '.sql'), ('TXT', '.txt'), ('BASH', '.bash'), ('JSON', '.json'), ('MARKDOWN', 'md')]))
		if len(file)>0:
			f = open(file,'wb')
			text = self.ta.get("1.0", END).encode("utf-8")
			f.write(text)
			f.close()
			self.filename = file
			self.updateTitle()


	def copy(self, event=None):
		self.text.event_generate("&lt;&lt;Copy>>")
		return


	def paste(self, event=None):
		self.text.event_generate("&lt;&lt;Paste>>")
		return


	def cut(self, event=None):
		self.text.event_generate("&lt;&lt;Cut>>")
		return

	def undo(self, event=None):
		if self.steps != 0:
			self.steps -= 1
			self.delete(0, END)
			self.insert(END, self.changes[self.steps])

	def redo(self, event=None):
		if self.steps < len(self.changes):
			self.delete(0, END)
			self.insert(END, self.changes[self.steps])
			self.steps += 1

	def add_changes(self, event=None):
		if self.get() != self.changes[-1]:
			self.changes.append(self.get())
			self.steps += 1



canvas = Canvas(root, width=1920, height=1080, background='white')
frame = Frame(root, bd=2, relief="sunken")
main(root)
root.mainloop()
