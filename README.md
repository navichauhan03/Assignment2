#A program for test if a number is odd or even
a=int(input('Enter the Number: '))
if a % 2 == 0: #modulus operator used to check number divisible by 2 and no remainder
    print(a,"Number is Even")
else:
    print(a,'Number is Odd')
print('Thank You')

# a program sum all integers from 1 to 50 and prints its sum
list=range(1,50)
sum=0
for i in list:
    sum=sum+i
print('Sum of All values from 1 to 50 is: ',sum)
print('Thanks')


