#LoginValidation.py<--File Name and Module Name
from LoginException import LoginUserError, LoginPasswardError
def welcome(uname):
    print("Hi {}, Good Morning-Good Remberence about user name and Pwd".format(uname))
def validation(uname,pwd):
    usernames=["python","java","c"]
    passwords=["rossum","james","ritche"]
    if uname not in usernames:
        raise LoginUserError
    else:
        if pwd not in passwords:
            raise LoginPasswardError
        else:
            welcome(uname) # Function Call
