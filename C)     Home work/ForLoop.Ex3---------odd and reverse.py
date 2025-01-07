num=int(input('enter a number'))
for i in range(1,num+1):
    if i<=0:
        print('invalid input')
    if i%2!=0:
        print(i)
        i=i+1
print('------------Reverse--------------')
for i in range(num,2,-1):
    if i%2!=0:
        print(i)
        i=i-1
