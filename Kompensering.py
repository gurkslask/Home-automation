class Kompensering:
    '''Kompensering är en klass som används
    för utekompensering. Man får sätta lite olika
    brytpunkter med SetVarden metoden, sätta MinMax
    och sen kör CountSP med utetemperaturen för att få
    tillbaka ett börvärde
    '''
    def __init__(self):
        self.DictVarden = {}
        self.SortedDictVarden = {}
        self.IterValue = 0

    def SetVarden(self, GraderUte, GraderFram):
        if isinstance(GraderUte, (int, float, complex)) and isinstance(GraderFram, (int, float, complex)):
            self.DictVarden[GraderUte] = GraderFram
        else:
            print('Fel vÃ¤rde')

    def SetMin(self, Min):
        self.Min = Min

    def SetMax(self, Max):
        self.Max = Max

    def MinMax(self, Value):
        return max(self.Min, min(self.Max, Value))
    
    def CountSP(self, PV):
        self.SortedList = sorted(self.DictVarden.keys())#Sortera värden
        for i in sorted(self.DictVarden.keys()):#Loopa igenom alla utetemp-värden
            if i > PV:#Hitta ett värde som är större än nuvarande utetemp
                self.UpperValueKomp = i#sätt det värdet
                self.LowValueKomp = self.SortedList[self.IterValue-1]#och ta värdet under det
                break#avbryt loopen4
            self.IterValue += 1
            if self.IterValue == len(self.DictVarden):
                return self.MinMax(self.DictVarden[self.SortedList[-1]])
        if self.UpperValueKomp == self.LowValueKomp:
            return self.MinMax(self.DictVarden[self.UpperValueKomp])#Om dessa är lika anta att nedre skalan nåddes
        self.y2 = self.DictVarden[self.UpperValueKomp]#sätt lite variabler
        self.y1 = self.DictVarden[self.LowValueKomp]
        self.x2 = self.UpperValueKomp
        self.x1 = self.LowValueKomp
        self.k =  (self.y2 - self.y1) / (self.x2 - self.x1)#utför räta linjens ekvation
        self.m =  self.y1 - (self.x1 * self.k)
        self.SP = (PV * self.k) + self.m
        return self.MinMax(self.SP), self.x2, self.x1
    



Komp = Kompensering()
Komp.SetVarden(20, 17)
Komp.SetVarden(-10, 60)
Komp.SetVarden(0, 55)
Komp.SetVarden(10, 30)
Komp.SetVarden(-20, 65)
Komp.SetMax(65)
Komp.SetMin(20)
print(Komp.CountSP(-52))
print(Komp.CountSP(152))


