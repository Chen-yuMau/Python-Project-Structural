from tkinter import *
import numpy as np

size_of_board = 600
number_of_xdots = 6
number_of_ydots = 7
number_of_dots = min(number_of_ydots,number_of_xdots)
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
dot_color = '#7BC043'
player1_color = '#0492CF'
player1_color_light = '#67B0CF'
player2_color = '#EE4035'
player2_color_light = '#EE7E77'
Green_color = '#7BC043'
dot_width = 0.25*size_of_board/number_of_dots
edge_width = 0.1*size_of_board/number_of_dots
distance_between_dots = size_of_board / (number_of_dots)

class StructuraL():
	# ------------------------------------------------------------------
	# Initialization functions
	# ------------------------------------------------------------------
	def __init__(self):
		self.window = Tk()
		self.window.title('StructuraL')
		self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
		self.canvas.pack()
		self.window.bind('<Button-1>', self.click)
		self.player1_starts = True
		self.refresh_board()
		self.play_again()

	def play_again(self):

	def mainloop(self):
		self.window.mainloop()

	# ------------------------------------------------------------------
	# Logical Functions:
	# The modules required to carry out game logic
	# ------------------------------------------------------------------

	def click(self, event):
		if not self.reset_board:
			grid_position = [event.x, event.y]
			logical_positon, valid_input = self.convert_grid_to_logical_position(grid_position)
		else:
			self.canvas.delete("all")
			self.play_again()
			self.reset_board = False


game_instance = StructuraL()
game_instance.mainloop()