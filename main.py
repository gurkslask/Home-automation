from ds1820class import DS1820
from ds1820class import Write_temp
from Kompensering import Kompensering
from OpenCloseValveClass import OpenCloseValve
import time


#Declare temperaturecompensation
Komp = Kompensering()
Komp.SetVarden(20, 17)
Komp.SetVarden(-10, 60)
Komp.SetVarden(0, 55)
Komp.SetVarden(10, 30)
Komp.SetVarden(-20, 65)
Komp.SetMax(65)
Komp.SetMin(20)

#Loggin of the compensation
Setpoint_VS1 = 0.0
Setpoint_Log_VS1 = Write_temp(Setpoint_VS1,'VS1_Setpoint')

#Declare temperature sensors
#Framledning
GT1 = DS1820('28-00000523a1cb')
#Retur
VS1_GT2 = DS1820('28-00000524056e')
#Ute
VS1_GT3 = DS1820('28-0000052407e0')

#Declare logging interval
GT1.SetWriteInterval(60)
VS1_GT2.SetWriteInterval(60)
VS1_GT3.SetWriteInterval(60)

#Declare Heating valve
VS1_SV1_Class = OpenCloseValve()

ActTimeLoop1 = time.time()
ActTimeLoop2 = time.time()

while True:
	'''This is the main loop'''
	if ActTimeLoop1 < time.time() + 20:
		ActTimeLoop1 = time.time()

		print('GT1 {0:.1f}'.format(GT1.RunMainTemp()))
		print('GT2 {0:.1f}'.format(VS1_GT2.RunMainTemp()))
		print('GT3 {0:.1f}'.format(VS1_GT3.RunMainTemp()))
		
		Setpoint_VS1 = Komp.CountSP(VS1_GT3.temp)
		Setpoint_Log_VS1.value = Setpoint_VS1
		print('SP {0:.1f}'.format(Setpoint_VS1))
		Setpoint_Log_VS1.main()

	if ActTimeLoop2 < time.time() + 5:
		ActTimeLoop2 = time.time()

		VS1_SV1_Class.main(GT1.temp , Setpoint_VS1, b_SV_CLOSE_DO, b_SV_OPEN_DO)

	time.sleep(4)
