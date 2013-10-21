import datetime
import time
class DS1820(adress):
	'''Class for working with a DS1820 temperature sensor
	'''
	def __init__(self):
		'''Some initialization		'''
		self.adress = adress
		self.temp = 0.0

	def ReadTemp(self):
		'''Read the file that stores temperature data, use the folder
		with the provided adress. Dont forget to run modprobe on the pi'''
	    with open(r'/sys/bus/w1/devices/'+self.adress+r'/w1_slave', 'r') as tempfile:
            data = tempfile.read() #Read the whole file
            temp_pos = data.find('t=') #Look for t, this is where the temperature is
            data = data[temp_pos+2:]#remove 't='
            data = int(data)/1000#insert comma, 
            self.temp = data
            return data

    def Write_temp(self, interval):
    	'''interval in seconds, dont update until interval is reached
    	Dont really know how the time stamp should work'''
    	timestamp = time.time()
    	if time.time() - interval > timestamp:
    		now = datetime.datetime.now()
    		if self.data_string == self.temp:*'''If temp is same as before, just insert a _'''
    			self.data_string = '_'
    		else:
    			self.data_string = self.temp
	        with open('sensors/'now.year + now.month + now.day + '/' + self.adress, 'a') as outfile:
	                outfile.write(self.data_string)
