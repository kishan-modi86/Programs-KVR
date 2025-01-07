n=int(input('enter the number: '))
i=0
sum=1

if n<0:
    print('invalid input')
else:
    while(i<n):
        sum=(n-i)*sum
        i=i+1
    print(sum)



