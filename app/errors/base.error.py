class ErrorHandler(Exception):
    def __init__(self, message:str,status_code:int,detail:str | None = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.detail = detail
        