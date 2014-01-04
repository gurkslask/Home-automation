from  ds1820class import Write_temp
import time

class OpenCloseValve(object):
	'A class that controls a valve with a close and a open signal'
	def __init__(self ):
		self.deadband = 2.0
		self.Time_Open = 1.0 #Seconds the valve shall open
		self.Time_Close = 0.5 #Seconds the valve shall close
		self.Man_Open = 0
		self.Man_Close = 0
		self.Write_Stat_Open = Write_temp(self.Man_Open, 'VS1_SV1_Open')
		self.Write_Stat_Close = Write_temp(self.Man_Close, 'VS1_SV1_Close')

	def main(self, PV, SP, IOClose, IOOpen, IOVariables):
		self.deltaT = SP - PV
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
				IOVariables[IOClose]['Value'] = 1
				self.Write_Stat_Close.main()
			else:
				self.Man_Close=0
				IOVariables[IOClose]['Value'] = 0
				self.Write_Stat_Close.main()



		while self.Man_Open == 1:
			self.acttime = time.time()
			if self.acttime < time.time() + self.Time_Close:
				#set Open IO
				IOVariables[IOOpen]['Value'] = 1
				self.Write_Stat_Open.main()
			else:
				self.Man_Open=0
				IOVariables[IOOpen]['Value'] = 0
				self.Write_Stat_Open.main()

		return IOVariables









