n=int(input('enter a number'))
for i in range(1,n+1):
    if i%2==0:
        print(i)
        i=i+2
print('-------------------------------')
#reverse of even in for loop
for i in range(n,1,-1):
    if i%2==0:
        print(i)
        i=i-2
print('-------------------------------')