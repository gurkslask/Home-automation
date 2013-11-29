from pymodbus.client.sync import ModbusTcpClient

class ModbusDigitalInputIOCard():
    """docstring for ModbusDigitalInput
    This is a class for CREVIS Digital input card
    that communicates via Modbus.
    When assigning the class, the Modbus adress
    must be specified. The modbus client must be 
    included as well, as this is where the connection 
    will happen
    """
    def __init__(self, adress, client):
        self.IOcard = 0
        self.IOadress = adress
        self.IOValue = 0
        self.IOVariables = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0}
        self.client = client

    def ReadStatus(self):
        """
        This method will read the input values from the IO card
        and convert from decimal to bin

        Here you gotta do data assignments as follows:
        my_digitalin_variable_1  =  ModbusDigitalInputIOCard__CLASS.IOVariables[0]
        my_digitalin_variable_2  =  ModbusDigitalInputIOCard__CLASS.IOVariables[1]
        """
        self.Value = self.client.read_input_registers(self.IOadress, 1)
        self.DecToBin(int(self.Value.registers[0]))

    def DecToBin(self, DecVal):
        BinVal = bin(DecVal)
        for i in range(len(BinVal) - 2):
           bitVal = BinVal[len(BinVal)-1-i]
           self.IOVariables[i] = bitVal

    def SetAddress(self, Address):
        #Use this method to set the address
        self.IOadress = Address

