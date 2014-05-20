#!/usr/bin/python
# -*- coding: utf-8 -*-
from ds1820class import DS1820
from ds1820class import Write_temp
from Kompensering import Kompensering
from OpenCloseValveClass import OpenCloseValve
from IOdef import IOdef
from Flask.Flask import simple, hello, Flaskrun
from flask import Flask, make_response
from scraping import GetData

import time
import threading



class MainLoop():
	def __init__(self):

		#Declare IO Variables
		self.IOVariables = IOdef()

		#Declare temperaturecompensation
		self.Komp = Kompensering()
		self.Komp.SetVarden(20, 17)
		self.Komp.SetVarden(-10, 40)
		self.Komp.SetVarden(0, 35)
		self.Komp.SetVarden(10, 30)
		self.Komp.SetVarden(-20, 65)
		self.Komp.SetMax(65)
		self.Komp.SetMin(20)

		#Loggin of the compensation
		self.Setpoint_VS1 = 0.0
		self.Setpoint_Log_VS1 = Write_temp(self.Setpoint_VS1,'VS1_Setpoint')

		#Declare temperature sensors
		#Framledning
		self.GT1 = DS1820('28-00000523a1cb')
		#Retur
		self.VS1_GT2 = DS1820('28-00000524056e')
		#Ute
		self.VS1_GT3 = DS1820('28-0000052407e0')

		#Declare logging interval
		self.GT1.SetWriteInterval(60)
		self.VS1_GT2.SetWriteInterval(60)
		self.VS1_GT3.SetWriteInterval(60)

		#Declare Heating valve
		self.VS1_SV1_Class = OpenCloseValve()
		self.VS1_SV1_Open_Trend_Class = Write_temp(self.IOVariables['b_SV_OPEN_DO']['Value'] * 10, 'b_SV_OPEN_DO')
		self.VS1_SV1_Close_Trend_Class = Write_temp(self.IOVariables['b_SV_CLOSE_DO']['Value'] * 10, 'b_SV_CLOSE_DO')

		#Initialize the loops
		self.ActTimeLoop1 = time.time()
		self.ActTimeLoop2 = time.time()

		#Interaction menu
		self.choices = {
					"1" : self.ChangeSP, 
					"2" : self.ShowValues
				}

		self.Weather_State=''

	def ControlLoop(self):
			while True:
				'''This is the main loop'''
				if self.ActTimeLoop1 +20< time.time():
					#20 seconds loop
					self.ActTimeLoop1 = time.time()

					#print('GT1 {0:.1f}'.format(GT1.RunMainTemp()))
					#print('GT2 {0:.1f}'.format(VS1_GT2.RunMainTemp()))
					#print('GT3 {0:.1f}'.format(VS1_GT3.RunMainTemp()))
					self.GT1.RunMainTemp()
					self.VS1_GT2.RunMainTemp()
					self.VS1_GT3.RunMainTemp()
					
					self.Setpoint_VS1 = self.Komp.CountSP(self.VS1_GT3.temp)
					self.Setpoint_Log_VS1.value = self.Setpoint_VS1
					#print('SP {0:.1f}'.format(Setpoint_VS1))
					self.Setpoint_Log_VS1.main()

					#Run valve check
					self.VS1_SV1_Class.main(self.GT1.temp , self.Setpoint_VS1)
					self.VS1_SV1_Open_Trend_Class.main()
					self.VS1_SV1_Close_Trend_Class.main()

					#print('Loop 1')

				if self.ActTimeLoop2 +5< time.time():
					#5seconds loop
					self.ActTimeLoop2 = time.time()

					#Run control of the valve
					self.VS1_SV1_Class.control()
					self.IOVariables['b_SV_CLOSE_DO']['Value'] = self.VS1_SV1_Class.Man_Close_OUT
					self.IOVariables['b_SV_OPEN_DO']['Value'] = self.VS1_SV1_Class.Man_Open_OUT

					#print('Loop 2')

				if self.ActTimeLoop1 +14400< time.time():
					#4 hour loop
					self.Weather_State=GetData()

				time.sleep(4)



	def InteractionLoop(self):
		while True:
			
			print("""Home-automation menu:
				1. Change Setpoint
				2. Show values
				""")
			choice=raw_input('Enter an option: ')
			action = self.choices.get(choice)
			if action:
				action()
			else:
				print("{0} is not a valid choice".format(choice))
			
			#print('Fran klassen: Open - ' + str(self.VS1_SV1_Class.Man_Open_OUT))
			#print('Fran klassen: Close - ' + str(self.VS1_SV1_Class.Man_Close_OUT))
			#print('Fran databasen: Open - ' + str(self.IOVariables['b_SV_OPEN_DO']['Value']))
			#print('Fran databasen: Close - ' + str(self.IOVariables['b_SV_CLOSE_DO']['Value']))
			time.sleep(5)

	def ChangeSP(self):
		value1 = input('Enter outside temperature: ')
		value2 = input('Enter forward temperature: ')
		try:
			self.Komp.DictVarden[int(value1)] =int(value2)
		except:
			print('Invalid values entered')

	def ShowValues(self):
		print('GT1 {0:.1f}'.format(self.GT1.temp))
		print('GT2 {0:.1f}'.format(self.VS1_GT2.temp))
		print('GT3 {0:.1f}'.format(self.VS1_GT3.temp))
		print('SP {0:.1f}'.format(self.Setpoint_VS1))

	def FlaskLoop(self):
		Flaskrun()






def main():
	ML = MainLoop()
	threading.Thread(target=ML.FlaskLoop).start()
	threading.Thread(target=ML.ControlLoop).start()
	threading.Thread(target=ML.InteractionLoop).start()


if __name__ == '__main__':
	main()




