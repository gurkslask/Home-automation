from pymodbus.client.sync import ModbusTcpClient

class ModbusDigitalOutputIOCard():
    """docstring for ModbusDigitalOutput"""
    def __init__(self, adress):
        self.IOcard = 0
        self.IOadress = adress
        self.IOValue = 0
        self.IOVariables = {}

    def BinToDec(self):
        '''
        Here you gotta do data assignments as follows:
        ModbusDigitalOutputIOCard__CLASS.IOVariables[0] =  my_digitalout_variable_1
        ModbusDigitalOutputIOCard__CLASS.IOVariables[1] =  my_digitalout_variable_2

        '''

        BinData=''
        for i in self.IOVariables:
            Bindata = self.IOVariables[i]+Bindata
        DecData=int(BinData,2)
        return DecData

              
    def WriteStatus(self):
        client.write_registers(self.IOadress, self.BinToDec())

    def SetAddress(self, Address):
        self.IOadress = Address