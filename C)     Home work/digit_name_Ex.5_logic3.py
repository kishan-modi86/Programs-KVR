digit=int(input('enter the digit'))
m={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
#print({1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}.get(digit,'enter digtit'))
#print({-1:'negative digit',-2:'negative digit',-3:'negative digit',-4:'negative digit',-5:'negative digit',-6:'negative digit','-7':'negative digit',-8:'negative digit',-9:'negative digit'}.get(digit,'number'))
if digit in m.keys():
    print(m.get(digit,'error'))

