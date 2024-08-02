# If any error occurs (model not responsing..etc) then these errors are raised,,wherever we mention these class
#ie;we  created object of this customexception() class,,in QAWithPDF ->.....,,thus any exception happen in this file,,
#then exception is raised,,so ,,developer come to know where the exception lies,,thus they can fix it.........
#happens then above code is executed and tells what is exception and in what file it is occuring
#If we have 1000's of files in our project,,then simly create object of this exception class,,thus any error occurs in those file then,,we come to know where the exception lies easily,,and fix it

import sys


class customexception(Exception):

    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        print(exc_tb)

        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))


#Demo of,,how above exception works...abs#ie; we are not going to run this file,,,so  this below main fuction never executes,,,,,we are just accessing customexception class to crete object,a dn raise exception
if __name__=="__main__":
    try:
        a=1/0

    except Exception as e:
        #print(e)
        raise customexception(e,sys)
