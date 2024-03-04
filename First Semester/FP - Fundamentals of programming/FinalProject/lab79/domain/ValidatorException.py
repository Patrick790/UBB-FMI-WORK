
class ValidatorException(Exception):

    def __init__(self, list_msg_error):
        self.__list_msg_error = list_msg_error

    def __str__(self):
        msg = ""
        for error in self.__list_msg_error:
            msg = msg + error + "\n"
        return msg