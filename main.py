from ds1820class import DS1820
import time

GT1 = DS1820('28-00000523a1cb')
#GT1.SetWriteInterval(60)
VS1_GT2 = DS1820('28-00000524056e')
VS1_GT3 = DS1820('28-0000052407e0')


#IO assignments should look like this
IO_Variables={1:{'Tagname': 'VS1_P1_DO', 'Value': 0, 'IOAddress':1, 'IOCard':2048, 'Type':'DO'},
			  2:{'Tagname': 'VS1_SV1_OPEN_DO', 'Value': 0, 'IOAddress':2, 'IOCard':2048, 'Type':'DO'},
			  3:{'Tagname': 'VS1_SV1_CLOSE_DO', 'Value': 0, 'IOAddress':3, 'IOCard':2048, 'Type':'DO'},

			  4:{'Tagname': 'VS1_SV1_CLOSE_DO', 'Value': 0, 'IOAddress':3, 'IOCard':2048, 'Type':'DO'},
			  }

GT1.SetWriteInterval(60)
VS1_GT2.SetWriteInterval(60)
VS1_GT3.SetWriteInterval(60)
while True:
	'''This is the main loop'''

	print(GT1.RunMainTemp())
	print(VS1_GT2.RunMainTemp())
	print(VS1_GT3.RunMainTemp())

	time.sleep(20)
