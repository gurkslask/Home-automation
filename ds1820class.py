class DS1820(adress):
	'''Class for working with a DS1820 temperature sensor
	'''
	def __init__(self):
		'''Some initialization		'''
		self.adress = adress

	def ReadTemp(self):
		'''Read the file that stores temperature data, use the folder
		with the provided adress. Dont forget to run modprobe on the pi'''
	    with open(r'/sys/bus/w1/devices/'+self.adress+r'/w1_slave', 'r') as tempfile:
            data = tempfile.read() #Read the whole file
            temp_pos = data.find('t=') #Look for t, this is where the temperature is
            data = data[temp_pos+2:]#remove 't='
            data = int(data)/1000#insert comma, 
            return data
