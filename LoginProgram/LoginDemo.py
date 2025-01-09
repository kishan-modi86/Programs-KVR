#LoginDemo.py<---Main Program
from LoginValidation import validation
from LoginException import LoginUserError,LoginPasswardError
while(True):
    try:
        user=input("Enter User Name:")
        password=input("Enter Ur PassWord:")
        validation(user,password)
    except LoginUserError:
        print("{} Invalid User Name:".format(user))
    except LoginPasswardError:
        print("{} Invalid Passward".format(password))
    else:
        ch=input("\nDo u want to Login with another Details(yes/no):")
        if(ch.lower()=="no"):
            print("Thx for this Program")
            break
