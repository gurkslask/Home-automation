#!/usr/bin/python
# -*- coding: utf-8 -*-
#from pymodbus.client.sync import ModbusTcpClient


class ModbusDigitalOutputIOCard():
    """docstring for ModbusDigitalOutput
    This is a class for CREVIS Digital Output card
    that communicates via Modbus.
    When assigning the class, the Modbus adress
    must be specified. The modbus client must be 
    included as well, as this is where the connection 
    will happen
    """
    def __init__(self, adress, client, IOdict):
        self.IOdict = IOdict
        self.IOcard = 0
        self.IOadress = adress
        self.IOValue = 0
        self.IOVariables = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
        self.client = client
        self.IOlist = [i for i in self.IOdict if self.IOdict[i]['IOdevice']==self.IOadress]


    def BinToDec(self):
        '''
        This method will read the input values from the IO card
        and convert from decimal to bin
        
        Here you gotta do data assignments as follows:
        ModbusDigitalOutputIOCard__CLASS.IOVariables[0] =  my_digitalout_variable_1
        ModbusDigitalOutputIOCard__CLASS.IOVariables[1] =  my_digitalout_variable_2

        '''
        for i in self.IOlist:
            self.IOVariables[self.IOdict[i]['IOadress']] =  self.IOdict[i]['Value']

        Bindata=''
        for i in self.IOVariables:
            Bindata = str(self.IOVariables[i])+Bindata
        DecData=int(Bindata,2)
        DecData=[DecData]
        return DecData

              
    def WriteStatus(self):
        self.client.write_registers(self.IOadress, self.BinToDec())

    def SetAddress(self, Address):
        self.IOadress = Address

def IOdef():
    IOVariables={
    'b_P1_DO': {'Value': 0, 'IOdevice': 2, 'IOadress': 1, 'Comment': 'Radiator cirk pumpen'},
    'b_SV_OPEN_DO': {'Value': 1, 'IOdevice': 2, 'IOadress': 2, 'Comment': 'Open heating valve'}, 
    'b_SV_CLOSE_DO': {'Value': 1, 'IOdevice': 2, 'IOadress': 3, 'Comment': 'Close heating valve'},
    'b_P2_DO': {'Value': 0, 'IOdevice': 2, 'IOadress': 4, 'Comment': 'Sunwarming cirk pump'},
    'b_Test': {'Value': 0, 'IOdevice': 2, 'IOadress': 5, 'Comment': 'Test var'},
    }
    return IOVariables

if __name__ == '__main__':

    a = ModbusDigitalOutputIOCard(2, 0, IOdef())
    print(a.IOVariables)
    print(a.BinToDec())
    print(a.IOlist)
    print(a.IOVariables)