from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import customtkinter
import os

customtkinter.set_appearance_mode("dark")

class MainApp(ttk.App):
	def __init__(self):
		super().__init__()
		self.theme_use('catppuccin-dark')
		self.title("App Manager")
		self.geometry("1000x650")
		self.style.configure('long.TNotebook', tabposition='wn')

		self.button = ttk.Button(self, text="Button")


		NotebookTabs(self)

class NotebookTabs(ttk.Notebook):
	def __init__(self, parent):
		super().__init__(parent, style='long.TNotebook')

		self.pack(fill=BOTH, expand=YES, padx=20, pady=20)


		PasswordGen(self)
		ProductFinder(self)


class PasswordGen(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		parent.add(self, text='Password Genarator')

		#Styling of frame in tabe
		self['padding'] = (5,10,5,10)
		self['borderwidth'] = 5
		self['relief'] = 'flat'

		#Layout
		self.columnconfigure(0, weight=1)
		self.columnconfigure(0, weight=3)

		#self.grid(padx=20, pady=20)
		ttk.Label(parent, text='Word to use for \npassword generation').grid(row=1, column=2, padx=50, pady=20)
		self.PasswordEntry = ttk.Entry(parent)

		self.PasswordEntry.grid(row=1, column=3, padx=10)

class ProductFinder(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		
		#self.pack(side=LEFT, padx=20, pady=20)

		parent.add(self, text='Product Finder')

		self.buttonA = ttk.Button(self, text='Button A')
		self.buttonB = ttk.Button(self, text='Button B')

		self.buttonA.grid(row=0, column=0, padx=10)
		self.buttonB.grid(row=1, column=0, padx=10)

	



if __name__ == '__main__':
	app = MainApp()
	app.mainloop()

 