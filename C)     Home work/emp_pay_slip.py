sal=float(input('enter the salary of employee: '))
print('*'*50)
emp_name=input('enter the name of employee: ')
emp_number=int(input('enter the employee number '))
print('*'*50)
if sal<=0:
    print('invalid salary')
if sal>=10000:
    da=(20/100)*(sal)
    ta=(10/100)*sal
    hra=(7/100)*sal
    cca=(0.5/100)*sal
    ma=(0.25/100)*sal
    lic=(2/100)*sal
    gpf=(1/100)*sal
if 0<sal<10000:
    da=(15/100)*(sal)
    ta=(7.5/100)*sal
    hra=(5/100)*sal
    cca=(0.25/100)*sal
    ma=(0.12/100)*sal
    lic=(1.5/100)*sal
    gpf=(1/100)*sal
print('                                            ')
print('                                            ')
print('employee name: ',emp_name)
print('employee number: ',emp_number)
print('                                            ')
print('*'*50)
print('                                            ')
print('                                            ')
print('net salary =', sal+da+ta+hra+cca+ma-(lic+gpf))
print('                                            ')
print('                                            ')
print('*'*50)
print('*'*50)
