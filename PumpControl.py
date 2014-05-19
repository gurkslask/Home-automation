import time


class PumpControl(object):
	'''The default PumpControl class'''

	def __init__(self):
		self.LarmDelay = 15
		self.Man = False
		self.Out = False
	def main(self, DI):
		if self.Man:
			self.Out = True
		elif not self.Man:
			self.Out = False

		if DI != self.Out:
			self.Larm = True
		else:
			self.Larm = False