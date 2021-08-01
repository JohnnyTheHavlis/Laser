class movement:
    def __init__(self, canvasName, circle_object, line_x, line_y):
    	self.absolute_position = {}
    	self.x = 0
    	self.y = 0
    	self.F = 1000 #mm/min
    	self.canvasName = canvasName
    	self.circle = circle_object
    	self.line_x = line_x
    	self.line_y = line_y
    	self.last_move = 0
    	self.motion()		#calling move class to move objects
    	print(self.get_coords())

    def motion(self):
    	pos = self.get_coords()
    	if (self.last_move == 1 and pos[1] < 0):
    		self.Stop()
    	if (self.last_move == 2 and pos[3] > 300):
    		self.Stop()
    	if (self.last_move == 3 and pos[0] < 0):
    		self.Stop()
    	if (self.last_move == 4 and pos[2] > 300):
    		self.Stop()
    	
    	self.canvasName.move(self.circle, self.x, self.y)
    	self.canvasName.move(self.line_x, self.x, self.y)
    	self.canvasName.move(self.line_y, self.x, self.y)

    	self.canvasName.after(100, self.motion)

    def Move_lUp(self):
    	if (self.pos[0] == -5 or self.pos[1] == -5):
    		self.x = 0
    		self.y = 0
    	else:
    		self.x = -5
    		self.y = -5

    def Move_rUp(self):
    	self.x = 5
    	self.y = -5
    	
    def Move_lDown(self):
    	self.x = -5
    	self.y = 5

    def Move_rDown(self):
    	self.x = 5
    	self.y = 5

    def move_up(self):
    	pos = self.get_coords()
    	if (pos[1] < 0):
    		self.x = 0
    		self.y = 0
    	else:
    		self.x = 0
    		self.y = -5
    		self.last_move = 1

    def move_down(self):
    	pos = self.get_coords()
    	if (pos[3] > 300):
    		self.x = 0
    		self.y = 0
    	else:
    		self.x = 0
    		self.y = 5
    		self.last_move = 2

    def move_left(self):
    	pos = self.get_coords()
    	if (pos[0] < 0):
    		self.x = 0
    		self.y = 0
    	else:
    		self.x = -5
    		self.y = 0
    		self.last_move = 3

    def move_right(self):
    	pos = self.get_coords()
    	if (pos[2] > 300):
    		self.x = 0
    		self.y = 0
    	else:
    		self.x = 5
    		self.y = 0
    		self.last_move = 4

    def Stop(self):
    	self.x = 0
    	self.y = 0

    def get_coords(self):
    	return (self.canvasName.coords(self.circle))

    def Coords_chech(self):
    	pos = self.get_coords()
    	if (pos[0] < 0.0 and self.x != 0):
    		self.x = 0
    		self.y = 0
    		print ("1")
    	else:
    		pass

    def get_absolute_position(self):
    	pos = self.get_coords()
    	self.absolute_position['X'] = pos[0] + 5
    	self.absolute_position['Y'] = pos[1] + 5
    	return self.absolute_position
    	
    def change_feedrate(self, feedrate):	#insert F from canvas to change feedrate when change occurs, loop it to catch change
    	self.F = feedrate