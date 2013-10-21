from ds1820class import DS1820
import time

GT1 = DS1820('28-00000523a1cb')
print(GT1.ReadTemp())
