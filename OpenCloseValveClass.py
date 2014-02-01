#!/usr/bin/python
# -*- coding: utf-8 -*-
from  ds1820class import Write_temp
import time

class OpenCloseValve(object):
	'A class that controls a valve with a close and a open signal'
	def __init__(self ):
		self.deadband = 2.0
		self.Time_Open = 1.0 #Seconds the valve shall open
		self.Time_Close = 0.5 #Seconds the valve shall close
		self.Man_Open = False
		self.Man_Close = False
		self.Man_Close_OUT = False
		self.Man_Open_OUT = False
		self.Write_Stat_Open = Write_temp(self.Man_Open, 'VS1_SV1_Open')
		self.Write_Stat_Close = Write_temp(self.Man_Close, 'VS1_SV1_Close')
		self.Control_Time = 0
		self.Control_Active = False

	def main(self, PV, SP):
		self.deltaT = SP - PV
		if self.deadband < self.deltaT:
			'If deltaT is bigger than the deadband, open valve and Heat'
			#Open 
			self.Man_Open = True
			self.Man_Close = False

		elif self.deltaT > 0 - self.deadband:
			'If deltaT is less than 0 minus deadband, close valve and Dont heat'
			#close
			self.Man_Close = True
			self.Man_Open = False

		else:
			'If none is true, do nothing'
			self.Man_Close = False 
			self.Man_Open = False

	def control(self):
		if not self.Control_Active:
			self.Control_Time = time.time() 
			self.Control_Active = True
		if self.Man_Close:
			if self.Control_Time + self.Time_Close < time.time():
				self.Man_Close_OUT = True
				#Close variable
			else:
				self.Man_Close_OUT = False
				self.Control_Active = False
		if self.Man_Open:
			if self.Control_Time + self.Time_Open < time.time():
				self.Man_Open_OUT = True
				#Open variable
			else:
				self.Man_Open_OUT = False
				self.Control_Active = False






