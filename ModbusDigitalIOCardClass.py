class ModbusDigitalIOCard():
    """docstring for ModbusDigitalInput"""
    def __init__(self, adress):
        self.IOcard = 0
        self.IOadress = adress
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

    def SetAddress(self, Address):
        self.IOadress = Address