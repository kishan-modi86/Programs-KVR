#by creating list
digit=int(input('enter the digit from 0 to 9: '))
lst=['zero','one','two','three','four','five','six','seven','eight','nine']
if digit==0:
    print(lst[0])
if digit==1:
    print(lst[1])
if digit==2:
    print(lst[2])
if digit==3:
    print(lst[3])
if digit==4:
    print(lst[4])
if digit==5:
    print(lst[5])
if digit==6:
    print(lst[6])
if digit==7:
    print(lst[7])
if digit==8:
    print(lst[8])
if digit==9:
    print(lst[9])
if -9<=digit<0:
    print('negative digit')
if digit>9 or digit<-9:
    print('it is a number : please enter a digit')
