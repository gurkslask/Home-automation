from pymodbus.client.sync import ModbusTcpClient

class ModbusDigitalOutputIOCard():
    """docstring for ModbusDigitalOutput"""
    def __init__(self, adress, client):
        self.IOcard = 0
        self.IOadress = adress
        self.IOValue = 0
        self.IOVariables = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
        self.client = client

    def BinToDec(self):
        '''
        Here you gotta do data assignments as follows:
        ModbusDigitalOutputIOCard__CLASS.IOVariables[0] =  my_digitalout_variable_1
        ModbusDigitalOutputIOCard__CLASS.IOVariables[1] =  my_digitalout_variable_2

        '''

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