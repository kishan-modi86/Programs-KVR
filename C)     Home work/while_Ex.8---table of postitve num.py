n=int(input('enter a number of your choice: '))
i=1
if n<=0:
    print('invalid input {}'.format(n))
else:
    while i<=10:

        print(f'{n}    x     {i}    =  {n*i}')
        i=i+1