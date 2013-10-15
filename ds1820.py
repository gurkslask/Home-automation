
with open('/sys/bus/w1/devices/28-00000523a1cb/w1_slave', 'r') as tempfile:
	data = tempfile.read()
	print(data.find('t='))
	temp_pos = data.find('t=')
	print(data[temp_pos:])