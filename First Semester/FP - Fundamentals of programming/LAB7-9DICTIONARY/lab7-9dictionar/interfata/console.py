from business.personService import PersonService

class Console:
    def __init__(self, personService: PersonService):
        self.personService = personService

    def add_person(self):
        try:
            personID = int(input("Enter the person id: "))
            name = input("Enter the name of the person: ")
            adress = input("Enter the adress of the person: ")
            self.personService.add_person(personID, name, adress)
        except ValueError:
            print("Invalid input, try again")
        except KeyError as ke:
            print(ke)

    def modify_person(self):
        try:
            personID = int(input("Enter the id of the person you want to modify: "))
            new_name = input("Enter the new name of the person: ")
            new_adress = input("Enter the new adress of the person: ")
            self.personService.modify_person(personID, new_name, new_adress)
        except KeyError as ke:
            print(ke)

    def delete_person(self):
        try:
            personID = int(input("Enter the id of the person you want to remove: "))
            self.personService.delete_person(personID)
        except KeyError as e:
            print(e)
    def print_persons(self):
        all_persons = self.personService.get_all_persons()
        if len(all_persons) == 0:
            print("List is empty")
        for person in all_persons:
            print(person)



    def print_meniu(self):
        print("1. Add person: ")
        print("2. Modifiy person: ")
        print("3. Delete person: ")
        print("a. Show all persons: ")
        print()



    def meniu(self):
        while True:
            self.print_meniu()
            option = input("Select an option:\n")
            if option == "1":
                self.add_person()
            elif option == "2":
                self.modify_person()
            elif option == "3":
                self.delete_person()
            elif option == "a":
                self.print_persons()
            elif option == "x":
                break
            else:
                print("Invalid option, try again")