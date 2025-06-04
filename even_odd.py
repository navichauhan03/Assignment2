#A program for test if a number is odd or even
a=int(input('Enter the Number: '))
if a % 2 == 0: #modulus operator used to check number divisible by 2 and no remainder
    print(a,"Number is Even")
else:
    print(a,'Number is Odd')
print('Thank You')