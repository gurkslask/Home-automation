from ds1820class import DS1820
import time

GT1 = DS1820('28-00000523a1cb')
#GT1.SetWriteInterval(60)
VS1_GT2 = DS1820('28-00000524056e')
VS1_GT3 = DS1820('28-0000052407e0')


GT1.SetWriteInterval(60)
VS1_GT2.SetWriteInterval(60)
VS1_GT3.SetWriteInterval(60)
while True:
	'''This is the main loop'''

	print(GT1.RunMainTemp())
	print(VS1_GT2.RunMainTemp())
	print(VS1_GT3.RunMainTemp())

	time.sleep(20)
