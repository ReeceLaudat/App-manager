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
		self.geometry("700x450")

		self.button = ttk.Button(self, text="Button")


		NotebookTabs(self)

class NotebookTabs(ttk.Notebook):
	def __init__(self, parent):
		super().__init__(parent)

		self.pack(fill=BOTH, expand=YES, padx=20, pady=20)


		MainFrame(self)
		SideFrame(self)


class MainFrame(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		
		self.pack(side=RIGHT, padx=10, pady=20, fill='both')


class SideFrame(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		
		self.pack(side=LEFT, padx=20, pady=20)

		self.buttonA = ttk.Button(self, text='Button A')
		self.buttonB = ttk.Button(self, text='Button B')

		self.buttonA.grid(row=0, column=0, padx=10)
		self.buttonB.grid(row=1, column=0, padx=10)

		parent.add(self, text='Selection')



if __name__ == '__main__':
	app = MainApp()
	app.mainloop()

 