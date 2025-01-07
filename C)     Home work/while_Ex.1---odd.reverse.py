#write a program which will generate odd numbers in reverse order
n=int(input())
i=1
if n<=0:
    print('invalid input')
else:
    if n%2!=0:
        while(n>=i):
            print(n)
            n=n-2
    if n % 2 == 0:
        n = n - 1
        while (n >= i):
            print(n)
            n = n - 2

