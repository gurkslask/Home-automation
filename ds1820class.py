import datetime
import time
import os
class DS1820():
	'''Class for woking with a DS1820 temperature sensor
	'''
	def __init__(self, adress):
		'''Some initialization		'''
		self.adress = adress
		self.temp = 0.0
		self.interval = 0.0
		self.HighAlarmActivated = False
		self.LowAlarmActivated = False
		self.timestamp = 0
		self.data_string = ''

	def SetWriteInterval(self, interval):
		self.interval = interval
		return self.interval

	def SetHighThreshold(self, HighThreshold):
		self.HighAlarmActivated = True
		self.HighAlarmTreshold = HighThreshold
		return self.HighAlarmTreshold

	def SetLowThreshold(self, LowThreshold):
		self.LowAlarmActivated = True
		self.LowAlarmTreshold = LowThreshold
		return self.LowAlarmTreshold

	def CheckTemperatureAlarm(self):
		'''Checks whether any alarm are activated, if they are
		Check if they are higher/lower than the threshold, if they are
		set the alarm'''
		if self.LowAlarmActivated:
			if self.temp < self.LowAlarmTreshold:
				self.LowAlarm = True
		else:
			self.LowAlarm = False

		if self.HighAlarmActivated:
			if self.temp > self.HighAlarmTreshold:
				self.HighAlarm = True
		else:
			self.HighAlarm = False		

	def ReadTemp(self):
		'''Read the file that stores temperature data, use the folder
		with the provided adress. Dont forget to run modprobe on the pi'''
		with open(r'/sys/bus/w1/devices/'+self.adress+r'/w1_slave', 'r') as tempfile:
			data = tempfile.read() #Read the whole file
			temp_pos = data.find('t=') #Look for t, this is where the temperature is
			data = data[temp_pos+2:]#remove 't='
			data = float(data)/1000#insert comma, 
			self.temp = data
			return data

	def RunMainTemp(self):
		'''This is where the magic happens'''
		self.ReadTemp()

		self.CheckTemperatureAlarm()

		self.Write_temp2()

		return self.temp



	def Write_temp(self):
		'''interval in seconds, dont update until interval is reached
		Dont really know how the time stamp should work'''
		assert self.interval != 0.0, 'Interval not set!'
		if time.time() - self.interval > self.timestamp:
			self.timestamp = time.time()
			now = datetime.datetime.now()
			if self.data_string == self.temp: 
				self.data_string = '_'
			else:
				self.data_string = self.temp
			path = 'sensors/' + self.adress + '/'
			if not os.path.exists(path):
				os.makedirs(path)
			with open(path + str(now.year) + str(now.month) + str(now.day), 'a+') as outfile:
			        outfile.write(str(self.data_string) + '\n')

	def Write_temp2(self):
		'''interval in seconds, dont update until interval is reached
		Dont really know how the time stamp should work'''
		assert self.interval != 0.0, 'Interval not set!'
		if time.time() - self.interval > self.timestamp:
			self.timestamp = time.time()
			now = datetime.datetime.now()
			#Remove all of this shit, seems "unnecessary"
			if self.data_string == self.temp: 
				self.data_string = self.temp
			else:
				self.data_string = self.temp
			path = 'sensors/' + self.adress + '/'
			if not os.path.exists(path):
				os.makedirs(path)
			with open(path+'trend', 'a+') as outfile:
			        outfile.write(str(int(time.time())) + '|' + str(self.data_string) + '\n')			        
