from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import os

#customtkinter.set_appearance_mode("dark")

class MainApp(ttk.App):
	def __init__(self):
		super(MainApp, self).__init__()
		self.theme_use('catppuccin-dark')
		self.title("App Manager")
		self.geometry("1250x650")
		self.style.configure('long.TNotebook', tabposition='wn')


		NotebookTabs(self)

class NotebookTabs(ttk.Notebook):
	def __init__(self, parent, **kwargs):
		super(NotebookTabs, self).__init__(parent, **kwargs, style='long.TNotebook')

		self.pack(fill='both', expand=True, padx=20, pady=20, ipadx=20, ipady=20)

		ProductFinder(self)
		PasswordGen(self)



class ProductFinder(ttk.Frame):
	def __init__(self, parent):
		super(ProductFinder, self).__init__(parent)
		
		self.grid(padx=20, pady=40)

		parent.add(self, text='Product \nFinder')

		#Layout
		self.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)


		self.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)

		#Widgets

		self.searchentry = ttk.Entry(self
			).grid(row=1, column=0, sticky='we', padx=5)

		self.searchbutton = ttk.Button(self, text='Search'
			).grid(row=1, column=1, sticky='w')

		self.searchfb = ttk.Checkbutton(self, text='Fb marketplace'
			).grid(row=2, column=0, sticky='w', padx=5)

		self.searchEbay = ttk.Checkbutton(self, text='Ebay'
			).grid(row=2, column=0, sticky='e', padx=5)

		self.importbutton = ttk.Button(self, text='Import', command=self.plot,
			).grid(row=1, column=1, sticky='e')

	def plot(self):
		#Appearance
		
	    # the figure that will contain the plot
		fig = Figure(figsize = (5, 5),
	                 dpi = 100)

	    # list of squares
		y = [i**2 for i in range(101)]

	    # adding the subplot
		plot1 = fig.add_subplot(111)

	    # plotting the graph
		plot1.plot(y)

	    # creating the Tkinter canvas
	    # containing the Matplotlib figure
		canvas = FigureCanvasTkAgg(fig, self)  
		canvas.draw()

	    # placing the canvas on the Tkinter window
		canvas.get_tk_widget().grid(row=5, column=5)

	    # creating the Matplotlib toolbar
		toolbar = NavigationToolbar2Tk(canvas, self)
		toolbar.update()

	    # placing the toolbar on the Tkinter window
		toolbar.get_tk_widget().grid(row=6,column=6)





class PasswordGen(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		parent.add(self, text='Password \nGenarator')


		#Layout
		self.columnconfigure((0,1,2,3), weight=1, uniform='a')


		self.rowconfigure((0,1,2,3), weight=1, uniform='a')


		#widgets
		self.gen_label = ttk.Label(self, width=20, text='Word for \npassword generation', relief='flat'
			).grid(row=0, column=1, padx=10, pady=10)

		self.passwordEntry = ttk.Entry(self
			).grid(row=0, column=2)

		self.generate_button = ttk.Button(self, text='Generate'
			).grid(row=0, column=3)

		self.output_text = ttk.Text(self
			).grid(row=1, column=1)





	



if __name__ == '__main__':
	app = MainApp()
	app.mainloop()

 