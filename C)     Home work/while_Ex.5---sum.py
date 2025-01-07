#write a program to find the sum of n natural numbers
n=int(input('enter the n0.'))
i=1
x=0
if n<0:
    print('inv')
else:
    while(i<=n):
        print(i)
        x=x+i
        i=i+1
    print('------------------')
    print(x)
    print('------------------')