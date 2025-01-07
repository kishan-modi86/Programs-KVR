i=int(input('enter values in list'))
lst=[]
sum=0
if i>0:
    for x in range(1,i+1):
        lst.append(float(input(f'enter lst value{x}',)))
    print(lst)
    for m in range(len(lst)):
        sum=sum+lst[m]
    print('sum=',sum)
    print(f'average = {sum/i}')
else:
    print('invalid input')
