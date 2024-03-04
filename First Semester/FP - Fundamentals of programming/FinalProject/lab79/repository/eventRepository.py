from repository.Repository import Repository

class EventRepository(Repository):

    def __init__(self):
        super().__init__()

    def get_event_by_id(self, id):
        for i in range(0, len(self._list)):
            current_event = self._list[i]
            if current_event.get_id() == id:
                return current_event
        return -1

    # def get_all_r(self):
    #     '''
    #     :return: function that returns the whole list of events
    #     '''
    #     return self.__all_events
    #
    # def find_event_after_id_r(self, evenid):
    #     '''
    #     :param evenid: the id that we search for in the whole list of ids
    #     :return: the event with the given id if we find it, or -1 if the id is not in the list
    #     '''
    #     for i in range(0, len(self.__all_events)):
    #         current_event = self.__all_events[i]
    #         if current_event.get_evenid() == evenid:
    #             return i
    #     return -1


    # def add(self, event):
    #     '''
    #     :param event: the event that we want to add to the list
    #     :return:
    #     '''
    #     if self.find_event_after_id_r(event.get_evenid()) != -1:
    #         raise KeyError("There already is an event with the given id")
    #     else:
    #         self.__all_events.append(event)
    #
    # def delete(self, evenid):
    #     '''
    #     :param evenid: the id of the event that we want to delete
    #     :return:
    #     '''
    #     if self.find_event_after_id_r(evenid) == -1:
    #         raise KeyError("The event with the given id does not exist")
    #     else:
    #         i =  self.find_event_after_id_r(evenid)
    #         current_event = self.__all_events[i]
    #         self.__all_events.remove(current_event)
    #
    # def modify(self, new_event):
    #     '''
    #     :param new_event: the new event
    #     :return:
    #     '''
    #     if self.find_event_after_id_r(new_event.get_evenid()) == -1:
    #         raise KeyError("The event with the given id does not exist")
    #     else:
    #         i =  self.find_event_after_id_r(new_event.get_evenid)
    #         self.__all_events[i] = new_event