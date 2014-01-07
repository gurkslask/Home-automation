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

	def main(self, PV, SP):
		self.deltaT = SP - PV
		if self.deadband < self.deltaT:
			'If deltaT is bigger than the deadband, open valve and Heat'
			#Open 
			self.Man_Open = 1
			self.Man_Close = 0

		elif self.deltaT > 0 - self.deadband:
			'If deltaT is less than 0 minus deadband, close valve and Dont heat'
			#close
			self.Man_Close = 1
			self.Man_Open = 0

		else:
			'If none is true, do nothing'
			self.Man_Close = 0 
			self.Man_Open = 0


