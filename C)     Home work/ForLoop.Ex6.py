lst=[]
n=int(input('enter a number'))
for x in range(1,n+1):
    lst.insert(x,float(input(f'enter value{x} : ')))
print(lst)
print('--------OR-----------')
m=[1,2,3,4,5]
sum=0
for x in range(len(m)):
    sum=sum+m[x]
print(sum)

