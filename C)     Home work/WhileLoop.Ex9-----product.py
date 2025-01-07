#write a program to find the product of given n natural numbers
n=int(input('enter a number: '))
i=1
ct=1
if n<=0:
    print('Invalid input')
else:
    while(i<=n):
        print(i)
        ct=ct*i
        i=i+1
    print('--------')
    print(ct)
    print('--------')
