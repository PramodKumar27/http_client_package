class HTTPRequestException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
