#write a program which will generate
num=int(input('enter the number'))
i=2
print('*'*50)
if num<=0:
    print('invalid input')
else:
    if num%2==0:
        while(num>=i):
            print(num)
            num=num-2
    if num%2!=0:
        num=num-1
        while(num>=i):
            print(num)
            num=num-2