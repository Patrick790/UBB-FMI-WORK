class Person:
    def __init__(self, personID, name, adress):
        '''

        :param personID:
        :param nume:
        :param adresa:
        '''
        self.__personID = personID
        self.__name = name
        self.__adress = adress


    def get_personID(self):
        return self.__personID

    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    def set_personID(self, new_personID):
        self.__personID = new_personID

    def set_name(self, new_name):
        self.__name = new_name

    def set_adress(self, new_adress):
        self.__adress = new_adress


    def __str__(self):
        '''
        functie pentru pretty printing
        :return:
        '''
        return "Person " + str(self.get_personID()) + " : " + self.get_name() + " , " + self.get_adress()
