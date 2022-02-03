from tkinter import *
import numpy as np

number_of_xdots = 7
number_of_ydots = 8
number_of_dots = min(number_of_ydots,number_of_xdots)
history = []
# grid = [[[0 for k in range(4)] for j in range(number_of_ydots)] for i in range(number_of_xdots)]
size_of_board = 500
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 5
dot_color = '#7BC043'
point_color = '#03fbff'
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
		self.game_point = [int((number_of_xdots-1)/2),int(((number_of_xdots-1)/2)+1)]
		self.history = []
		self.window = Tk()
		self.window.title('StructuraL')
		self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board+100)
		self.grid = [[[0 for k in range(4)] for j in range(number_of_ydots)] for i in range(number_of_xdots)]
		self.canvas.pack()
		self.window.bind('<Button-1>', self.click)
		self.player = 1
		self.refresh_board()
		self.play_again()

	def play_again(self):
		self.refresh_board()
		self.game_point = [int((number_of_xdots-1)/2),int(((number_of_xdots-1)/2)+1)]
		self.grid = [[[0 for k in range(4)] for j in range(number_of_ydots)] for i in range(number_of_xdots)]
		self.history = []
		# Input from user in form of clicks
		self.player = 1
		self.reset_board = False
		self.turntext_handle = []

		self.already_marked_boxes = []
		self.display_turn_text()
		return
	def mainloop(self):
		self.window.mainloop()

	# ------------------------------------------------------------------
	# Logical Functions:
	# The modules required to carry out game logic
	# ------------------------------------------------------------------
	def is_edge_occupied(self, logical_position, type):
		if (logical_position>=0):
			if (self.grid[self.game_point[0]][self.game_point[1]][logical_position] == 0):
				return(0)
		else:
			if(logical_position == -1 and (self.grid[self.game_point[0]-1][self.game_point[1]][1]) == 0):
				return(0)
			elif(logical_position == -2 and (self.grid[self.game_point[0]-1][self.game_point[1]+1][2]) == 0):
				return(0)
			elif(logical_position == -3 and (self.grid[self.game_point[0]][self.game_point[1]+1][3]) == 0):
				return(0)
			elif(logical_position == -4 and (self.grid[self.game_point[0]-1][self.game_point[1]-1][0]) == 0):
				return(0)
		return(1)



	def game_point_position(self):
		return [(self.game_point[0]+0.5)*distance_between_dots,(self.game_point[1]+0.5)*distance_between_dots]

	def draw_dash(self,a,b,c,d,e,f):
		self.canvas.create_line((a+0.5)*distance_between_dots,
								(b+0.5)*distance_between_dots,
								(c+0.5)*distance_between_dots,
								(d+0.5)*distance_between_dots,
								fill = e, 
								dash = f)
		return
	def draw_line(self,a,b,c,d,player):
		if player==1:
			self.canvas.create_line((a+0.5)*distance_between_dots,
									(b+0.5)*distance_between_dots,
									(c+0.5)*distance_between_dots,
									(d+0.5)*distance_between_dots,
									fill = 'blue',width = 5)
		else:
			self.canvas.create_line((a+0.5)*distance_between_dots,
									(b+0.5)*distance_between_dots,
									(c+0.5)*distance_between_dots,
									(d+0.5)*distance_between_dots,
									fill = 'red',width = 5)
		return
	def draw_dot(self,a,b,c,d):
		start_x = a*distance_between_dots+distance_between_dots/2
		end_x = b*distance_between_dots+distance_between_dots/2
		self.canvas.create_oval(start_x-dot_width/2, 
								end_x-dot_width/2, 
								start_x+dot_width/2,
								end_x+dot_width/2, 
								fill=c,
								outline=d)
	def display_turn_text(self):
		text = 'Next turn: '
		if self.player==1:
			text += 'Player1'
			color = player1_color
		else:
			text += 'Player2'
			color = player2_color

		self.canvas.delete(self.turntext_handle)
		self.turntext_handle = self.canvas.create_text(size_of_board - 5*len(text),
													   size_of_board-distance_between_dots/8,
													   font="cmr 15 bold", text=text, fill=color)

		return
	def convert_grid_to_logical_position(self, grid_position):
		success = 1
		# clickx = (grid_position[0]+0.5)*distance_between_dots
		# clicky = (grid_position[1]+0.5)*distance_between_dots
		[clickx,clicky] = grid_position
		pointx = (self.game_point[0]+0.5)*distance_between_dots
		pointy = (self.game_point[1]+0.5)*distance_between_dots
		#-(1/2)pi ~ (1/2)pi
		if (clickx == pointx):
			return 0, 0
		pivot = np.arctan(((clicky-pointy)/(clickx-pointx)))
		pivot = round(pivot/((1/4)*(3.14159)),0)
		# print(pivot)
		if (pivot == 2 or pivot == -2):
			if((clicky - pointy)>0):
				logical_position = -3;
			else:
				logical_position = 3;
		if (pivot == 1):
			if((clickx - pointx)>0):
				logical_position = 0;
			else:
				logical_position = -4;
		if (pivot == 0):
			if((clickx - pointx)>0):
				logical_position = 1;
			else:
				logical_position = -1;
		if (pivot == -1):
			if((clickx - pointx)>0):
				logical_position = 2;
			else:
				logical_position = -2;
		if (abs(clickx-pointx)>distance_between_dots or abs(clicky-pointy)>distance_between_dots):
			success = 0
		print(logical_position)
		return logical_position, success
	def make_edges(self):#draw all lines
		i = 0;
		while i<number_of_xdots:
			j = 0;
			while j<number_of_ydots:
				if self.grid[i][j][0]!=0:
					self.draw_line(i,j,i+1,j+1,self.grid[i][j][0])
				if self.grid[i][j][1]!=0:
					self.draw_line(i,j,i+1,j,self.grid[i][j][1])
				if self.grid[i][j][2]!=0:
					self.draw_line(i,j,i+1,j-1,self.grid[i][j][2])
				if self.grid[i][j][3]!=0:
					self.draw_line(i,j,i,j-1,self.grid[i][j][3])
				j+=1
			i+=1
		return
	def refresh_board(self):
		# [x,y] = self.game_point_position()
		[x,y] = self.game_point################################if edge occupied
		if (x<number_of_xdots-1 and y<number_of_ydots-1) :
			if self.grid[x][y][0] == 0:
				self.draw_dash(x,y,x+1,y+1,'gray',(2,2))
		if (x<number_of_xdots-1) :
			if self.grid[x][y][1] == 0:
				self.draw_dash(x,y,x+1,y,'gray',(2,2))
		if (x<number_of_xdots-1 and y>0) :
			if self.grid[x][y][2] == 0:
				self.draw_dash(x,y,x+1,y-1,'gray',(2,2))
		if (y>0) :
			if self.grid[x][y][3] == 0:
				self.draw_dash(x,y,x,y-1,'gray',(2,2))
		if (y<number_of_ydots-1) :
			if self.grid[x][y+1][3] == 0:
				self.draw_dash(x,y,x,y+1,'gray',(2,2))
		if (x>0 and y<number_of_ydots-1) :
			if self.grid[x-1][y+1][2] == 0:
				self.draw_dash(x,y,x-1,y+1,'gray',(2,2))
		if (x>0) :
			if self.grid[x-1][y][1] == 0:
				self.draw_dash(x,y,x-1,y,'gray',(2,2))
		if (x>0 and y>0) :
			if self.grid[x-1][y-1][0] == 0:
				self.draw_dash(x,y,x-1,y-1,'gray',(2,2))

		for i in range(number_of_xdots):
			for j in range(number_of_ydots):
				self.draw_dot(i,j,dot_color,dot_color)
		self.draw_dot(x,y,point_color,point_color)
	def game_point_full(self):
		[x,y] = self.game_point
		if (x<number_of_xdots-1 and y<number_of_ydots-1):
			if self.grid[x][y][0] == 0:
				return(0)
		if (x<number_of_xdots-1):
			if self.grid[x][y][1] == 0:
				return(0)
		if (x<number_of_xdots-1 and y>0):
			if self.grid[x][y][2] == 0:
				return(0)
		if (y>0):
			if self.grid[x][y][3] == 0:
				return(0)
		if(y<number_of_ydots-1):
			if self.grid[x][y+1][3] == 0:
				return(0)
		if(x>0 and y<number_of_ydots-1):
			if self.grid[x-1][y+1][2] == 0:
				return(0)
		if(x>0):
			if self.grid[x-1][y][1] == 0:
				return(0)
		if(x>0 and y>0):
			if self.grid[x-1][y-1][0] == 0:
				return(0)
		return(1)

	def update_board(self, new_edge,player):
		if (new_edge>=0):
			# print("haga")
			self.grid[self.game_point[0]][self.game_point[1]][new_edge] = player
			if new_edge == 0:
				print("gaga")
				self.game_point[0] = self.game_point[0]+1
				self.game_point[1] = self.game_point[1]+1
			elif new_edge == 1:
				self.game_point[0] = self.game_point[0]+1
			elif new_edge == 2:
				self.game_point[0] = self.game_point[0]+1
				self.game_point[1] = self.game_point[1]-1
			elif new_edge == 3:
				self.game_point[1] = self.game_point[1]-1
		else:
			if(new_edge == -1):
				self.grid[self.game_point[0]-1][self.game_point[1]][1] = player
				self.game_point[0] = self.game_point[0]-1
			elif(new_edge == -2):
				self.grid[self.game_point[0]-1][self.game_point[1]+1][2] = player
				self.game_point[0] = self.game_point[0]-1
				self.game_point[1] = self.game_point[1]+1
			elif(new_edge == -3):
				self.grid[self.game_point[0]][self.game_point[1]+1][3] = player
				self.game_point[1] = self.game_point[1]+1
			elif(new_edge == -4):
				self.grid[self.game_point[0]-1][self.game_point[1]-1][0] = player
				self.game_point[0] = self.game_point[0]-1
				self.game_point[1] = self.game_point[1]-1
		if self.game_point[0] >= number_of_xdots:
			self.game_point[0]-=1;
		if self.game_point[1] >= number_of_ydots:
			self.game_point[1]-=1;
		if not(self.game_point_full()):
			self.history.append(self.game_point)
		else:
			i = len(self.history)
			while(self.game_point_full()):
				i-=1
				self.game_point = self.history[i]
		return

	def click(self, event):
		if not self.reset_board:
			grid_position = [event.x, event.y]
			new_edge, valid_input = self.convert_grid_to_logical_position(grid_position)
			# print("ha:"+str(valid_input)+" :ba:"+ str(self.is_edge_occupied(new_edge, valid_input)))
			if valid_input and (self.is_edge_occupied(new_edge, valid_input)==0):
				# print("tra")
				self.update_board(new_edge,self.player)#calculations and savings
				self.canvas.delete("all")
				self.make_edges()#draw all lines
				self.refresh_board()#draw choices
				self.player= (self.player % 2) + 1
				print("player:" + str(self.player))
				# if self.is_gameover():
				# 	# self.canvas.delete("all")
				# 	self.display_gameover()
				# else:
				# 	self.display_turn_text()
		else:
			self.canvas.delete("all")
			self.play_again()
			self.reset_board = False


game_instance = StructuraL()
game_instance.mainloop()