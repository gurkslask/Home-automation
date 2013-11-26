from pymodbus.client.sync import ModbusTcpClient

class ModbusDigitalInputIOCard():
    """docstring for ModbusDigitalInput"""
    def __init__(self, adress, client):
        self.IOcard = 0
        self.IOadress = adress
        self.IOValue = 0
        self.IOVariables = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0}
        self.client = client

    def ReadStatus(self):
        self.Value = self.client.read_input_registers(self.IOadress, 1)
        self.DecToBin(int(self.Value.registers[0]))
        #print('---------------------------------------------')
        #print(self.Value.registers[0])
        #type(self.Value.registers[0])
    def DecToBin(self, DecVal):
        BinVal = bin(DecVal)
        for i in range(len(BinVal) - 2):
           bitVal = BinVal[len(BinVal)-1-i]
           self.IOVariables[i] = bitVal

    def SetAddress(self, Address):
        self.IOadress = Address

if __name__ == '__main__':
    x=ModbusDigitalInputIOCard(1)
    print(x.DecToBin(100))
    print(x.IOVariables)