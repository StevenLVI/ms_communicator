class NotImplementedError(Exception):
    def __init__(self, message, status=None):
        self.status = status
        return super().__init__(message)


class BadRequestError(Exception):
    def __init__(self, message, status=None):
        self.status = status
        return super().__init__(message)
