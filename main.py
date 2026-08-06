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
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs, style='long.TNotebook')

		self.pack(fill='both', expand=True, padx=20, pady=20, ipadx=20, ipady=20)


		PasswordGen(self)
		ProductFinder(self)


class PasswordGen(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		parent.add(self, text='Password \nGenarator')




		#Layout
		#self.grid(ipadx=20, ipady=40)
		self.columnconfigure((0,1,2,3,4,5), weight=1, uniform='a')


		self.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')



		#widgets
		self.gen_label = ttk.Label(self, width=20, text='Word for \npassword generation', relief='flat'
			).grid(row=0, column=1, padx=10, pady=10)

		self.passwordEntry = ttk.Entry(self
			).grid(row=0, column=2)

		self.generate_button = ttk.Button(self, text='Generate'
			).grid(row=0, column=3)

		self.output_text = ttk.Text(self
			).grid(row=2, column=1)

class ProductFinder(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		
		self.grid(padx=20, pady=40)

		parent.add(self, text='Product \nFinder')

		self.buttonA = ttk.Button(self, text='Button A')
		self.buttonB = ttk.Button(self, text='Button B')

		self.buttonA.grid(row=0, column=0, padx=10, pady=10)
		self.buttonB.grid(row=1, column=0, padx=10, pady=10)

	



if __name__ == '__main__':
	app = MainApp()
	app.mainloop()

 