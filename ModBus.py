from pymodbus.client.sync import ModbusTcpClient
import time, os


#---------------------------------------------------------------------------#
# configure the client logging
#---------------------------------------------------------------------------#
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


#---------------------------------------------------------------------------#
# configure io card
#---------------------------------------------------------------------------#
Digital_In_1 = ModbusDigitalIOCard():
Digital_In_1.SetAddress(1)
#---------------------------------------------------------------------------#
# choose the client you want
#---------------------------------------------------------------------------#
# make sure to start an implementation to hit against. For this
# you can use an existing device, the reference implementation in the tools
# directory, or start a pymodbus server.
#---------------------------------------------------------------------------#
client = ModbusTcpClient('192.168.1.9')
rq = client.write_registers(2048, [0])
rr = client.read_input_registers(000, 1)
print rr.registers



#---------------------------------------------------------------------------#
# Run io card
#---------------------------------------------------------------------------#
Digital_In_1.ReadStatus()


#---------------------------------------------------------------------------#
# configure io card variables
#---------------------------------------------------------------------------#

Test_Variabel = Digital_In_1.IOVariables[14]








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
class ModbusDigitalIOCard():
    """docstring for ModbusDigitalInput"""
    def __init__(self, arg):
        self.IOcard = 0
        self.IOadress = 0
        self.IOValue = 0
        self.IOVariables = {}

    def ReadStatus(self):
        self.Value = client.read_input_registers(self.IOadress, 1)
        self.DecToBin(self.Value.registers)

    def DecToBin(DecVal, self):
        '''
        Here you gotta do data assignments as follows:
        my_digitalin_variable_1 = ModbusDigitalIOCard__CLASS.IOVariables[0]
        my_digitalin_variable_2 = ModbusDigitalIOCard__CLASS.IOVariables[1]

        '''
        BinVal = bin(DecVal)
        for i in range(len(BinVal) - 2):
           bitVal = BinVal[len(BinVal)-1-i]
           if self.IOVariables[i]:
              self.IOVariables[i] = bitVal

    def SetAddress(Address):
        self.IOadress = Address






