class ApiError(Exception):

    """
        Exception for errors with api, getting data from api

        Attributes:
            error_code -- code of error, type int
        Properties:
            error_code -- returns code of error, type int
    """

    def __init__(self, error_code):
        super().__init__()
        self.__error_code = error_code

    @property
    def error_code(self):
        return self.__error_code
