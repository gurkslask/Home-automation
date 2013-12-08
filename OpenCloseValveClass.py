import time

class OpenCloseValve(object):
	'A class that controls a valve with a close and a open signal'
	def __init__(self, PV, SP, IOClose, IOOpen ):
		self.PV = PV
		self.SP = SP
		self.deadband = 2.0
		self.Time_Open = 1.0 #Seconds the valve shall open
		self.Time_Close = 0.5 #Seconds the valve shall close

	def main(self):
		self.deltaT = self.SP - self.PV
		if self.deadband < self.deltaT:
			#Open 
			self.Man_Open = 1
		elif self.deltaT > 0 - self.deadband:
			#close
			self.Man_Close = 1

		while self.Man_Close == 1:
			self.acttime = time.time()
			if self.acttime < time.time() + self.Time_Close:
				#set Close IO
				pass
			else:
				self.Man_Close=0


		while self.Man_Open == 1:
			self.acttime = time.time()
			if self.acttime < time.time() + self.Time_Close:
				#set Open IO
				pass
			else:
				self.Man_Open=0




