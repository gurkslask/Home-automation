import datetime
import time


timestamp_minute = time.time()

def Read_temp():
        with open('/sys/bus/w1/devices/28-00000523a1cb/w1_slave', 'r') as tempfile:
                data = tempfile.read()
                print(data.find('t='))
                temp_pos = data.find('t=')
                print(data[temp_pos+2:])

def Write_temp(indata):
        with open(r'C:/Projects/Home-automation/test.txt', 'a') as outfile:
                outfile.write(indata)

while True:
	if time.time() - 60 > timestamp_minute :
		now = datetime.datetime.now()
		stringen = str(now.day) + str(now.month) + str(now.minute) + ' - 5555\n'
		print( stringen)
		Write_temp( stringen)
		timestamp_minute = time.time()


