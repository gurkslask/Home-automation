from pymodbus.client.sync import ModbusTcpClient
import time, os
from ModbusDigitalInputIOCardClass import ModbusDigitalInputIOCard
from ModbusDigitalOutputIOCardClass import ModbusDigitalOutputIOCard

#---------------------------------------------------------------------------#
# configure the client logging
#---------------------------------------------------------------------------#
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


#---------------------------------------------------------------------------#
# choose the client you want
#---------------------------------------------------------------------------#
# make sure to start an implementation to hit against. For this
# you can use an existing device, the reference implementation in the tools
# directory, or start a pymodbus server.
#---------------------------------------------------------------------------#
client = ModbusTcpClient('192.168.1.9')
#rq = client.write_registers(2048, [0])
#rr = client.read_input_registers(000, 1)
#print (rr.registers)

#---------------------------------------------------------------------------#
# configure io card
#---------------------------------------------------------------------------#
Digital_In_1 = ModbusDigitalInputIOCard(0, client)

Digital_Out_1 = ModbusDigitalOutputIOCard(2048, client)

#---------------------------------------------------------------------------#
# Define io card Variables
#---------------------------------------------------------------------------#
Digital_In_1_Variable0 = Digital_In_1.IOVariables[0]
Digital_In_1_Variable1 = Digital_In_1.IOVariables[1]
Digital_In_1_Variable2 = Digital_In_1.IOVariables[2]
Digital_In_1_Variable3 = Digital_In_1.IOVariables[3]
Digital_In_1_Variable4 = Digital_In_1.IOVariables[4]
Digital_In_1_Variable5 = Digital_In_1.IOVariables[5]
Digital_In_1_Variable6 = Digital_In_1.IOVariables[6]
Digital_In_1_Variable7 = Digital_In_1.IOVariables[7]
Digital_In_1_Variable8 = Digital_In_1.IOVariables[8]
Digital_In_1_Variable9 = Digital_In_1.IOVariables[9]
Digital_In_1_Variable10 = Digital_In_1.IOVariables[10]
Digital_In_1_Variable11 = Digital_In_1.IOVariables[11]
Digital_In_1_Variable12 = Digital_In_1.IOVariables[12]
Digital_In_1_Variable13 = Digital_In_1.IOVariables[13]
Digital_In_1_Variable14 = Digital_In_1.IOVariables[14]
Digital_In_1_Variable15 = Digital_In_1.IOVariables[15]
#---------------------------------------------------------------------------#
# Run io card
#---------------------------------------------------------------------------#
Digital_In_1.ReadStatus()
#---------------------------------------------------------------------------#
# Define io card Variables
#---------------------------------------------------------------------------#
Digital_In_1_Variable0 = Digital_In_1.IOVariables[0]
Digital_In_1_Variable1 = Digital_In_1.IOVariables[1]
Digital_In_1_Variable2 = Digital_In_1.IOVariables[2]
Digital_In_1_Variable3 = Digital_In_1.IOVariables[3]
Digital_In_1_Variable4 = Digital_In_1.IOVariables[4]
Digital_In_1_Variable5 = Digital_In_1.IOVariables[5]
Digital_In_1_Variable6 = Digital_In_1.IOVariables[6]
Digital_In_1_Variable7 = Digital_In_1.IOVariables[7]
Digital_In_1_Variable8 = Digital_In_1.IOVariables[8]
Digital_In_1_Variable9 = Digital_In_1.IOVariables[9]
Digital_In_1_Variable10 = Digital_In_1.IOVariables[10]
Digital_In_1_Variable11 = Digital_In_1.IOVariables[11]
Digital_In_1_Variable12 = Digital_In_1.IOVariables[12]
Digital_In_1_Variable13 = Digital_In_1.IOVariables[13]
Digital_In_1_Variable14 = Digital_In_1.IOVariables[14]
Digital_In_1_Variable15 = Digital_In_1.IOVariables[15]

#---------------------------------------------------------------------------#
# Define io card Variables
#---------------------------------------------------------------------------#
Digital_Out_1_Variable0 = 0
Digital_Out_1_Variable1 = 0
Digital_Out_1_Variable2 = 1#<---
Digital_Out_1_Variable3 = 0
Digital_Out_1_Variable4 = 0
Digital_Out_1_Variable5 = 0
Digital_Out_1_Variable6 = 0
Digital_Out_1_Variable7 = 0
Digital_Out_1.IOVariables[0] = Digital_Out_1_Variable0
Digital_Out_1.IOVariables[1] = Digital_Out_1_Variable1
Digital_Out_1.IOVariables[2] = Digital_Out_1_Variable2
Digital_Out_1.IOVariables[3] = Digital_Out_1_Variable3
Digital_Out_1.IOVariables[4] = Digital_Out_1_Variable4
Digital_Out_1.IOVariables[5] = Digital_Out_1_Variable5
Digital_Out_1.IOVariables[6] = Digital_Out_1_Variable6
Digital_Out_1.IOVariables[7] = Digital_Out_1_Variable7
#---------------------------------------------------------------------------#
# Run io card
#---------------------------------------------------------------------------#
Digital_Out_1.WriteStatus()
print(Digital_In_1_Variable0)
print(Digital_In_1_Variable1)
print(Digital_In_1_Variable2)
print(Digital_In_1_Variable3)
print(Digital_In_1_Variable4)
print(Digital_In_1_Variable5)
print(Digital_In_1_Variable6)
print(Digital_In_1_Variable7)
print(Digital_In_1_Variable8)
print(Digital_In_1_Variable9)
print(Digital_In_1_Variable10)
print(Digital_In_1_Variable11)
print(Digital_In_1_Variable12)
print(Digital_In_1_Variable13)
print(Digital_In_1_Variable14)
print(Digital_In_1_Variable15)
#---------------------------------------------------------------------------#
# configure io card variables
#---------------------------------------------------------------------------#

#Test_Variabel = Digital_In_1.IOVariables[14]








'''
#rq = client.write_registers(8009, [2]*4)
rr = client.read_input_registers(0000,1)
print rr
#assert(rr.registers == [10]*8)

'''
'''
rr = client.read_holding_registers(8001, 1)
print rr.registers

i=1
uptime = time.time()
while True:
    rq = client.write_registers(800, [i]*1)
    print i
    rr = client.read_input_registers(000, 1)
    print rr.registers
    if i < 7:
        i = i * 2
        print time.time() - uptime
    else:
        i=1
        os.system("cls")
    time.sleep(1)
'''

#---------------------------------------------------------------------------#
# close the client
#---------------------------------------------------------------------------#
client.close()

'''IOcardDict = {}

def InitModbusCards():
    
'''







