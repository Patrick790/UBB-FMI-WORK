from exeption.exeption import RepoError
from repository.Repository import Repository


class RepoErrorr:
    pass


class EnrollRepository(Repository):

    def __init__(self, person_repository, event_repository):
        super().__init__()
        self.__person_repository = person_repository
        self.__event_repository = event_repository

    def add(self, enroll):
        person_id = enroll.get_personID()
        event_id = enroll.get_evenId()
        if self.__person_repository.find_after_id(person_id) == -1 or self.__event_repository.find_after_id(event_id) == -1:
            raise RepoError("The person or the event does not exist!")
        elif self.find_enroll_after_person_id_and_event_id(person_id, event_id) != -1:
            raise RepoError("The person is already enrolled at the event")
        else:
            super().add(enroll)


    def find_enroll_after_person_id_and_event_id(self, person_id, event_id):
        for i in range(0, len(self._list)):
            current_enroll = self._list[i]
            if current_enroll.get_id() == person_id and current_enroll.get_event_id() == event_id:
                return i
        return -1

    def exist_enroll_event(self, event_id):
        for i in range(0, len(self._list)):
            current_enroll = self._list[i]
            if current_enroll.get_id() == event_id:
                return True
        return False

    def delete_enrolls_event(self, event_id):
        i = 0
        while i < len(self._list):
            current_enroll = self._list[i]
            if current_enroll.get_event_id() == event_id:
                event_id = current_enroll.get_id()
                super().delete(event_id)
                i = i - 1
            i = i + 1

    # def get_all(self):
    #     return self.__all_enrolls
    #
    # def add(self, enroll):
    #     id = enroll.get_id()
    #     if self.find_enroll_after_id(id) != -1:
    #         raise KeyError("This id has already been used for an enroll: ")
    #     else:
    #         personID = enroll.get_personID()
    #         evenId = enroll.get_evenId()
    #         if self.__person_repository.find_person_after_id(personID) == -1 or self.__event_repository.find_event_after_id_r(evenId) == -1:
    #             raise KeyError("The person or the event does not exist!")
    #         elif self.find_enroll_after_person_id_and_event_id(personID, evenId) != -1:
    #             raise KeyError("The person is already enrolled at the event")
    #         else:
    #             self.__all_enrolls.append(enroll)
    #
    # def find_enroll_after_id(self, id):
    #     for i in range(0, len(self.__all_enrolls)):
    #         current_enroll = self.__all_enrolls[i]
    #         if current_enroll.get_id() == id:
    #             return i
    #     return -1
    #
    # def find_enroll_after_person_id_and_event_id(self, personID, evenId):
    #     for i in range(0, len(self.__all_enrolls)):
    #         current_enroll = self.__all_enrolls[i]
    #         if current_enroll.get_personID() == personID and current_enroll.get_evenId() == evenId:
    #             return i
    #     return -1
    #
    # def exist_enroll_event(self, evenId):
    #     for i in range(0, len(self.__all_enrolls)):
    #         current_enroll = self.__all_enrolls[i]
    #         if current_enroll.get_evenId == evenId:
    #             return True
    #     return False
    #
    # def delete_enrolls_event(self, evenId):
    #     i = 0
    #     while i < len(self.__all_enrolls):
    #         current_enroll = self.__all_enrolls[i]
    #         if current_enroll.get_evenId() == evenId:
    #             self.__all_enrolls.remove(current_enroll)
    #             i = i - 1
    #         i = i + 1