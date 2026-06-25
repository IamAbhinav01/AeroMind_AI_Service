class ErrorHandler(Exception):

    def __init__(self, message:str,status_code:int,detail:str | None = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.detail = detail

    def to_dictionary(self)->dict:
        payload:dict = {
            "error":self.message,
            "status_code":self.status_code
        }
        if self.detail :
            payload["detail"] = self.detail
        return payload