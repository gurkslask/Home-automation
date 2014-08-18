import pickle as cPickle
 

'''
    CUR_GLO1 = 'valglo1'
    CUR_GLO2 = 'valglo2'
    CUR_GLO3 = 'valglo3'

    def saveGlobs():
        tempDict1 = globals().copy()
        tempDict2 = {}
        for key in tempDict1:
            if (key[:4]=='CUR_'):tempDict2[key] = tempDict1[key]
        pickle.dump(tempDict2,open('tempDict.p','wb'))

    def retrieveGlobs():
        tempDict = pickle.load(open('tempDict.p','rb'))
        globals().update(tempDict)





def Load(self):
    f = open(self.filename,'rb')
    tmp_dict = cPickle.load(f)
    f.close()          

    self.__dict__.update(tmp_dict) 


def Save(self):
    f = open(self.filename,'wb')
    cPickle.dump(self.__dict__,f,2)
    f.close()
'''


class mintestklass():
    def __init__(self):
        self.name='none'
        self.a_name = 'Bertil'
        self.filename = 'temp.p'
        self.testklass = mintestklass2()

    def Load(self):
        f = open(self.filename,'rb')
        tmp_dict = cPickle.load(f)
        f.close()           
        print(type(tmp_dict['testklass']))

        self.__dict__.update(tmp_dict)  
    

    def Save(self):
        f = open(self.filename,'wb')
        cPickle.dump(self.__dict__,f,2)
        f.close()

class mintestklass2():
    def  __init__(self):
        self.namn = 'none'
        self.a_namn = 'Berit'

def main():
    #klassen = pickle.load(open('temp.p', 'rb'))
    klassen = mintestklass()
    print(klassen.name)
    print(klassen.a_name)
    klassen.Load()



    print(klassen.name)
    print(klassen.a_name)
    klassen.name='Alex2'
    klassen.a_name='Berta'
    print(klassen.name)
    print(klassen.a_name)



    print(klassen.testklass.namn)
    print(klassen.testklass.a_namn)
    klassen.testklass.namn='Alex2'
    klassen.testklass.a_namn='Berta'
    print(klassen.testklass.namn)
    print(klassen.testklass.a_namn)
    print(klassen.__dict__)
    


    klassen.Save()
    #pickle.dump(klassen, open('temp.p', 'wb'))

if __name__ == '__main__':
        main()    