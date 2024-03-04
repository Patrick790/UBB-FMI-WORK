from exeption.exeption import RepoError


class Repository:
    def __init__(self):
        self._list = []

    def get_all(self):
        return self._list

    def add(self, entity):
        if self.find_after_id(entity.get_id()) != -1:
            raise RepoError("There already is an entity with this id!")
           # raise DuplicateIDException("There already is an entity with this id")
        else:
            self._list.append(entity)

    def modify(self, new_entity):
        id_new_entity = new_entity.get_id()
        if self.find_after_id(id_new_entity) == -1:
            raise RepoError("Entity does not exist!")
            # raise InexistentIDException("The entity with this id does not exist")
        else:
            index = self.find_after_id(id_new_entity)
            self._list[index] = new_entity

    def delete(self, id):
        if self.find_after_id(id) == -1:
            raise RepoError("There is not an entity with this id!")
            #raise InexistentIDException("The entity with this id does not exist")
        else:
            index = self.find_after_id(id)
            self._list.pop(index)

    def find_after_id(self, id):
        for i in range(0, len(self._list)):
            current_entity = self._list[i]
            if current_entity.get_id() == id:
                return i
        return -1

    def get_by_id(self, id):
        for i in range(0, len(self._list)):
            current_entity = self._list[i]
            if current_entity.get_id() == id:
                return current_entity
        return -1

    def __len__(self):
        return len(self._list)
