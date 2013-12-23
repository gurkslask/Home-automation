from ds1820class import DS1820
from ds1820class import Write_temp
import Kompensering
import time


Komp = Kompensering()
Komp.SetVarden(20, 17)
Komp.SetVarden(-10, 60)
Komp.SetVarden(0, 55)
Komp.SetVarden(10, 30)
Komp.SetVarden(-20, 65)
Komp.SetMax(65)
Komp.SetMin(20)

#Framledning
GT1 = DS1820('28-00000523a1cb')
#Retur
VS1_GT2 = DS1820('28-00000524056e')
#Ute
VS1_GT3 = DS1820('28-0000052407e0')


GT1.SetWriteInterval(60)
VS1_GT2.SetWriteInterval(60)
VS1_GT3.SetWriteInterval(60)
while True:
	'''This is the main loop'''

	print(GT1.RunMainTemp())
	print(VS1_GT2.RunMainTemp())
	print(VS1_GT3.RunMainTemp())
	
	Setpoint_VS1 = Komp.CountSP(VS1_GT3.temp)
	Setpoint_Log_VS1 = Write_temp(Setpoint_VS1,'VS1_Setpoint')

	time.sleep(20)
