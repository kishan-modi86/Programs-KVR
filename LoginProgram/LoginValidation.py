#LoginValidation.py<--File Name and Module Name
from LoginException import LoginUserError, LoginPasswardError
def welcome(uname):
    print("Hi {}, Good Morning-Good Remberence about user name and Pwd".format(uname))
def validation(uname,pwd):
    dct={'python':'rossum','java':'james','c':'ritche'}
    usernames=["python","java","c"]
    if uname not in usernames:
        raise LoginUserError
    else:
        if pwd!=dct[uname]:
            raise LoginPasswardError
        else:
            welcome(uname) # Function Call
