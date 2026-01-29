import sys

class CustomException(Exception):
    def __init__(self,exception_message,exception_details:sys):
        super().__init__(exception_message) #best pratice without it also it works 
        self.exception_details=exception_details
        self.exception_message=exception_message
        #extracting traceback information
        _,_,exc_tb=self.exception_details.exc_info()
        if exc_tb is not None:
            self.lineno=exc_tb.tb_lineno
            self.filename=exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno="Unknow"
            self.filename="Unknown"

    def __str__(self):
        return f'Error occurred in python script name {self.filename} in the line number {self.lineno} and error message {self.exception_message}'
    


