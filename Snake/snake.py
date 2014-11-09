from config import *


class Snake:
	def __init__(self, COLOR=GREEN, Y_CORD=100, RIGHT_BUTTON=None, DOWN_BUTTON=None, LEFT_BUTTON=None, UP_BUTTON=None, _queue=None):
		self.color, self.right_button, self.down_button, self.left_button, self.up_button = COLOR, RIGHT_BUTTON, DOWN_BUTTON, LEFT_BUTTON, UP_BUTTON
		self.keys = (RIGHT_BUTTON, DOWN_BUTTON, LEFT_BUTTON, UP_BUTTON)
		self.ax, self.ay = dx, 0
		self.score = 0

		if _queue is not None:
			self.queue = _queue
		else:
			self.queue = tuple((START_X + DIAMETER * (N - i), Y_CORD) for i in range(N))

	def __repr__(self):
		return repr(self.queue) + ' ' + repr(self.ax) + ' ' + repr(self.ay) + '\n'

	def setSpeed(self, _ax, _ay):
		self.ax, self.ay = _ax, _ay

	def getHead(self):
		return self.queue[0]
		
	def isAlive(self, enemy):
		head = self.getHead()
		return not isOutside(head) and head not in self.queue[1:] + enemy.queue

	def foundPrize(self, prize):
		head = self.getHead()
		return pygame.Rect((head[0] - RADIUS, head[1] - RADIUS), (DIAMETER, DIAMETER)).colliderect(prize)

	def grow(self, enemy):
		self.score += 1
		last = self.queue[-1]
		add = None

		for i, j in directions:
			tail = last[0] + i * DIAMETER, last[1] + j * DIAMETER
			if tail not in self.queue + enemy.queue:
				add = tail

		#if add is None:
		#	print "can't grow"
		#	pygame.time.delay(20000)
		#	assert 0

		self.queue += (add,)

	def changeDirection(self, key):
		if key == self.right_button and self.ay != 0:
			self.ax = dx
			self.ay = 0

		elif key == self.down_button and self.ax != 0:
			self.ay = dy
			self.ax = 0

		elif key == self.left_button and self.ay != 0:	
			self.ax = -dx
			self.ay = 0

		elif key == self.up_button and self.ax != 0:	
			self.ay = -dy
			self.ax = 0

	def changesState(self, key):
		if key == self.right_button and self.ay != 0:
			return 1
		elif key == self.down_button and self.ax != 0:
			return 1
		elif key == self.left_button and self.ay != 0:	
			return 1
		elif key == self.up_button and self.ax != 0:	
			return 1
		return 0

	def move(self):
		head = self.getHead()
		nhead = head[0] + self.ax, head[1] + self.ay
		self.queue = (nhead,) + self.queue[:-1]

	def draw(self, screen):
		#if self.ax == 0 and self.ay == 0:
		#	print 'delayed ', self.__repr__()
		#	pygame.time.delay(20000)

		pygame.draw.circle(screen, (100, 0, 0), self.getHead(), RADIUS, 0)
		for item in self.queue[1:]:
			pygame.draw.circle(screen, self.color, item, RADIUS, 0)
