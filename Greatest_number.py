# WAP to find the freatest of 3 numbers entered by the user.

a = int(input('Enter first number:'))
b = int(input('Enter Second number:'))
c = int(input('Enter third number:'))

if(a>=b and a>=c):
    print("first number is largest",a)
elif(b>=c):
    print('second number is largest',b)
else:
    print('third number is largest',c)