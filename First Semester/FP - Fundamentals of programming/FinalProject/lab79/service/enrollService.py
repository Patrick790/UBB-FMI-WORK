from datetime import datetime
from domain.Enroll import Enroll

class EnrollService:

    def __init__(self, enroll_repository, person_repository, event_repository):
        self.__enroll_repository = enroll_repository
        self.__person_repository = person_repository
        self.__event_repository = event_repository

    def get_all(self): ##
        return self.__enroll_repository.get_all()

    def add(self, id, personID, evenId):
        enroll = Enroll(id, personID, evenId)
        self.__enroll_repository.add(enroll)

    def exist_enroll_event(self, evenId):
        return self.__enroll_repository.get_enroll_after_event(evenId)

    def person_enrolled_at_event(self, description):
        all_persons = []
        all_enrolls = self.__enroll_repository.get_all()
        for enroll in all_enrolls:
            id_event = enroll.get_evenId()
            event = self.__event_repository.get_event_after_id(id_event)
            if event.get_description() == description:
                person_id = enroll.get_personID()
                person = self.__person_repository.get_person_by_id(person_id)
                name = person.get_name()
                all_persons.append(person)
        return all_persons

    def get_event_description_date(self, personID):

        '''
        method that returns a dict which contins the events and their descriptions if a certain person is enrolled in them
        :param personID: id of the person
        :return: a dict that contains the event and the description if the person is enrolled
        '''
        dict_event_description = {}
        enrolls = self.get_all()
        for enroll in enrolls:
            if enroll.get_personID() == personID:  #found an event that is attended by the searched person
                event_id = enroll.get_evenId()
                event = self.__event_repository.get_event_by_id(event_id)
                description_event = event.get_description()
                event_date = event.get_date()
                dict_event_description[event_date] = description_event
        return dict_event_description

    def return_person_enrolled_at_event_after_date(self, name):
        '''
               method that returns the events for a certain person with the description ascending order after the date or description
               :param personID: id person
               :return:
               '''
        person = self.__person_repository.get_by_name(name)
        if person == -1:
            raise KeyError("Person with the given name does not exist")
        else:
            id_person = person.get_id()
            dict_event_date = self.get_event_description_date(id_person) #dict ex: {description event: date event}
            dict_sorted = sorted(dict_event_date.items(), key=lambda d:(d[1], d[0])) #(datetime.strptime(d, "%Y-%m-%d"), ))
            #dict_sorted = sorted(dict_event_date.items(), key=lambda d: (d[1] , d[0]))
            # sorting the input list by formatting each date using the strptime() function
            #inputDateList.sort(key=lambda date: datetime.strptime(date, "%m-%Y"))
            return dict_sorted


    def get_nr_enrolls(self, person_id):
        enrolls = self.get_all()
        nr_events = 0
        for enroll in enrolls:
            if enroll.get_personID() == person_id:
                nr_events += 1
        return nr_events

    def most_events(self):##
        max_nr_events = -1
        persons = self.__person_repository.get_all()
        for person in persons:
            if max_nr_events < self.get_nr_enrolls(person.get_id()):
                max_nr_events = self.get_nr_enrolls(person.get_id())
        return max_nr_events

    def person_most_events(self):
        all_persons = []
        persons = self.__person_repository.get_all()
        # return persons
        maxx = self.__person_repository.most_events()
        for person in persons:
            nr_enrolls = self.get_nr_enrolls(person.get_id())
            if nr_enrolls == maxx:
                all_persons.append(person)
        return all_persons

    def get_nr_events(self, event_id):
        enrolls = self.get_all()
        nr_persons = 0
        for enroll in enrolls:
            if enroll.get_evenId() == event_id:
                nr_persons += 1
        return nr_persons

    def get_person_nr_events(self):
        dict_person_nr_events = {}
        events = self.__event_repository.get_all()
        for event in events:
            event_id = event.get_id()
            dict_person_nr_events[event.get_description()] = self.get_nr_events(event_id)
        new_doc = dict(sorted(dict_person_nr_events.items(), key=lambda item: item[1], reverse=True))
        return new_doc

    # def first_20(self): ##
    #     dict = self.get_person_nr_events()
    #     l = int(0.2 * len(dict))
    #     new_dict = {}
    #     i = 0
    #     for el in dict:
    #         if i <= l:
    #             new_dict[el] = dict[el]
    #             i = i + 1
    #         else:
    #             break
    #     return new_dict
    #
    # def size(self):
    #     return self.__enroll_repository.__len__()


    # def get_client_nr_carti(self):
    #     '''Functia care afisaza lista de clienti sortata dupa numarul de carti imprumutate
    #     '''
    #     dictonar_client_nr_carti = {}
    #     clients = self.__client_repository.get_all()
    #     for client in clients:
    #         id_client = client.get_id()
    #         dictonar_client_nr_carti[client.getName()] = self.get_nr_carti(id_client)
    #     new_doc = dict(sorted(dictonar_client_nr_carti.items(), key=lambda item: item[1], reverse=True))
    #     return new_doc

    # def get_nr_carti(self, id_client):
    #     inchirieri = self.get_all()
    #     nr_books = 0
    #     for inchiriere in inchirieri:
    #         if inchiriere.get_id_client() == id_client:
    #             nr_books += 1
    #     return nr_books

    # def get_event_date(self, personID):
    #
    #     '''
    #     method that returns a dict which contins the events and their descriptions if a certain person is enrolled in them
    #     :param personID: id of the person
    #     :return: a dict that contains the event and the description if the person is enrolled
    #     '''
    #     dict_event_date = {}
    #     enrolls = self.get_all()
    #     for enroll in enrolls:
    #         if enroll.get_personID() == personID:  #found an event that is attended by the searched person
    #             event_id = enroll.get_evenId()
    #             event = self.__event_repository.get_event_by_id(event_id)
    #             description_event = event.get_description
    #             date = event.get_date
    #             dict_event_date[description_event] = date
    #     return dict_event_date




    # def get_person_nr_events(self):
    #     dict_person_nr_events = {}
    #     persons = self.__person_repository.get_all()
    #     for person in persons:
    #         person_id = person.get_id()
    #         dict_person_nr_events[person.get_name()] = self.get_person_nr_events(person_id)
    #     new_doc = dict(sorted(dict.items(), key=lambda item: item[1], reverse=True))
    #     return new_doc
    #
    #
    # def first_20(self):
    #     dict = self.get_person_nr_events()
    #     l = int(0.2 * len(dict))
    #     new_dict = {}
    #     i = 0
    #     for el in dict:
    #         if i < l:
    #             new_dict[el] = dict[el]
    #             i = i + 1
    #         else:
    #             break
    #     return new_dict

# events.sort(key=lambda event: (event.description, event.date.year, event.date.month, event.date.day))
      #  return events

# inputDateList.sort(key=lambda date: datetime.strptime(date, "%m-%Y"))
# print(sorted(inputDateList, key=sortDates))

#  Rapoarte:
#  Lista de evenimente la care participă o persoană ordonat alfabetic după descriere, după dată
#  Persoane participante la cele mai multe evenimente
#  Primele 20% evenimente cu cei mai mulți participanți (descriere, număr participanți)