class NotValidInput(Exception):
    """
    Raise when input number is lower than 5, or greater than 20
    """
    pass


class ResponseError(Exception):
    """
    Raise when response is not 200 OK
    """
    pass
