
class PersonEventService:
    def __init__(self,PersonEventRepository, EventNrRepository):
        self.person_event_repository = PersonEventRepository
        self.event_nr_repository = EventNrRepository

    def get_all(self):
        return self.person_event_repository.save_p()

    def first_20(self):
        all_enrolls = self.person_event_repository.save_p()
        all_enrolls = sorted(all_enrolls, key=lambda x: x.nr_events, reverse = True)
        lenght = int(0.2 * len(all_enrolls)) + 1
        return all_enrolls[:lenght]

    # def most_events(self):
    #     all_events = self.event_nr_repository.save_e()
    #     all_events = sorted(all_events, key=lambda x: x.nr_enrolls, reverse= True)
    #     return all_events[:1]

    def return_person_enrolled_at_event_after_date(self):
        all_events = self.event_nr_repository
        all_events.sort(all_events, key=lambda x:(x.description, x.date))
        return all_events


# class ClientBookService:
#     def _init_(self, client_book_repository, book_nr_repository):
#         self.client_book_repository = client_book_repository
#         self.book_nr_repository = book_nr_repository
#
#     def get_all(self):
#         return self.client_book_repository.save_c()
#
#     def cele_mai_inchiriate_carti(self):
#         all_book_hire = self.book_nr_repository.save_b()
#         all_book_hire = sorted(all_book_hire, key=lambda x: x.nr_inchirieri, reverse=True)
#         return all_book_hire[:1]
#
#     def order_by_name(self):
#         all_client_book = self.client_book_repository.save_c()
#         all_client_book = sorted(all_client_book, key=lambda x: x.name, reverse=False)
#         return all_client_book
#
#     def order_by_nr_carti(self):
#         all_client_book = self.client_book_repository.save_c()
#         all_client_book = sorted(all_client_book, key=lambda x: x.nr_books, reverse=True)
#         return all_client_book
#
#     def first_20(self):
#         all_client_book = self.client_book_repository.save_c()
#         all_client_book = sorted(all_client_book, key=lambda x: x.nr_books, reverse=True)
#         lung = int(0.2 * len(all_client_book)) + 1
#         return all_client_book[:lung]