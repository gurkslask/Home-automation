from ds1820class import DS1820
import time

GT1 = DS1820('28-00000523a1cb')
GT1.Set_Write_Interval(60)



while True:
	'''This is the main loop'''


	
	print(GT1.ReadTemp())
	GT1.Write_temp(60)



	time.sleep(20)
