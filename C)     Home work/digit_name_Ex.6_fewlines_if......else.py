digit=int(input('enter the digit from 0 to 9'))
res='zero' if digit==0 else 'one' if digit==1 else 'two' if digit==2 else 'three' if digit==3 else 'four' if digit==4 else 'five' if digit==5 else 'six' if digit==6 else 'seven' if digit==7 else 'eight' if digit==8 else 'nine' if digit==9 else 'it is a number' if digit>9 else 'negative digit' if 0>digit>=-9 else 'nothing'
print(f'{digit} is {res}')
