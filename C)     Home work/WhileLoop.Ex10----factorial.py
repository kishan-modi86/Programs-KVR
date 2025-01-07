#program to find the factorial of a given number
number = int(input("Enter a number: "))
fac = 1
i = 1
while i <= number:
    fac =fac * i
    i =i+1
print(f"The factorial of {number} is {fac}.")
