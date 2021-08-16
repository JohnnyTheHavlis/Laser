from tkinter import *
import visual
from movement import movement
from Execute import *
from ISO import *

class Main:
	def __init__(self):
		self.file_name = ('G-code_test.tap')

		self.Z = False

		self.root = Tk()
		self.root.resizable(width=False, height=False)
		self.root.geometry("800x480")
		self.width = 480
		self.height = 480

		self.circle_pos = [240, 240]

		self.visual = visual

		self.canvas = Canvas(self.root, width = self.width, height = self.height)
		self.canvas.grid(row=0, rowspan=3, column=1, columnspan=3)

		self.line_x = visual.create_line_x(self.circle_pos, self.canvas, "gray30")
		self.line_y = visual.create_line_y(self.circle_pos, self.canvas, "gray30")
		self.circle = visual.create_circle(self.circle_pos, 5, self.canvas, "red2")
		self.m = movement(self.canvas, self.circle, self.line_x, self.line_y)

		self.pos_buttons()
		#self.pos_labels()

		self.IS = ISO(self.file_name)
		self.EXE = Execute(self.circle, self.canvas, self.visual, self.IS, self.m)

		self.root.bind("<KeyPress-Left>",lambda e: self.m.move_left())
		self.root.bind("<KeyPress-Right>",lambda e: self.m.move_right())
		self.root.bind("<KeyPress-Up>",lambda e: self.m.move_up())
		self.root.bind("<KeyPress-Down>",lambda e: self.m.move_down())
		self.root.bind("<KeyRelease>", lambda e: self.m.Stop())

		self.root.after(1, self.loop)
		#root.after(20, get_pos)
		self.root.mainloop()
		'''
		def laser_toggle():
			visual.draw(circle, canvas, "red2")
			root.after(20, laser_toggle)

		if Z == True:
			root.after(20, laser_toggle)
		'''

	def loop(self):
		self.update_pos_labels()
		self.simulate()
		self.root.after(1, self.loop)

	def simulate(self):
		pos = self.m.get_absolute_position()
		print(pos)
		self.EXE.Exe_ISO(self.IS.Process(self.IS.Input_Line()))

	def get_pos(self):
		idk = m.get_coords()
		pos = m.get_absolute_position()
		print(pos)
		#print(type(idk))
		root.after(20, get_pos)

	def pos_buttons(self):
		f = Frame(self.root, height = 300, width = 150)
		f.grid(row = 1, column = 5, columnspan = 3, rowspan = 4)

		Button_lUp = Button (f, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_lUp())
		Button_left = Button (f, text = "L", padx = 40, pady = 40, command=lambda: self.m.move_left())
		Button_lDown = Button (f, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_lDown())
		Button_Up = Button (f, text = "U", padx = 40, pady = 40, command=lambda: self.m.move_up())
		Button_ = Button (f, text = "*", padx = 40, pady = 40, command=lambda: self.m.move_up())
		Button_Down = Button (f, text = "D", padx = 40, pady = 40, command=lambda: self.m.move_down())
		Button_rUp = Button (f, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_rUp())
		Button_right = Button (f, text = "R", padx = 40, pady = 40, command=lambda: self.m.move_right())
		Button_rDown = Button (f, text = "*", padx = 40, pady = 40, command=lambda: self.m.Move_rDown())

		Button_lUp.grid(row = 0, column = 5)
		Button_left.grid(row = 1,column = 5)
		Button_lDown.grid(row = 2, column = 5)
		Button_Up.grid(row = 0, column = 6)
		Button_.grid(row = 1, column = 6)
		Button_Down.grid(row = 2, column = 6)
		Button_rUp.grid(row = 0, column = 7)
		Button_right.grid(row = 1, column = 7)
		Button_rDown.grid(row = 2, column = 7)

	def pos_labels(self):
		self.Label_X = Label(self.root, text = "X:", padx = 40, pady = 40)
		self.Label_Y = Label(self.root, text = "Y:", padx = 40, pady = 40)
		self.Label_Z = Label(self.root, text = "Z:", padx = 40, pady = 40)

		self.Label_X.grid(row = 0, column = 0)
		self.Label_Y.grid(row = 1, column = 0)
		self.Label_Z.grid(row = 2, column = 0)

	def update_pos_labels(self):
		pos = self.m.get_absolute_position()
		pos['X'] = round(pos['X'],3)
		pos['Y'] = round(pos['Y'],3)
		Z = self.EXE.get_Z()
		self.Label_X.configure(text = "X: {}".format(pos['X']))
		self.Label_Y.configure(text = "Y: {}".format(pos['Y']))
		self.Label_Z.configure(text = "Z: {}".format(Z))

app = Main()