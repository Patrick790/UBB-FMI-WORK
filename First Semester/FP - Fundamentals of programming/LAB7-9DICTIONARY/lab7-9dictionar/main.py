from domain import person
from infrastructura.personRepository import PersonRepository
from business.personService import PersonService
from interfata.console import Console


def main():
    personRepository = PersonRepository()
    personService = PersonService(personRepository)
    console = Console(personService)
    console.meniu()


main()