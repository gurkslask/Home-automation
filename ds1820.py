import time
def Read_temp():
	with open('/sys/bus/w1/devices/28-00000523a1cb/w1_slave', 'r') as tempfile:
		data = tempfile.read()
		print(data.find('t='))
		temp_pos = data.find('t=')
		print(data[temp_pos+2:])

def Write_temp(in)
	with open('test') as infile:
		data = infile.read()
	with open('test', 'w') as outfile:
        a_file.write(data + '\n' + in)