# WAP to find multiple of number

x  = int(input('enter the number:'))
y = int(input('enter the number to check multiple or not:'))

if(x % y == 0):
    print("The number is multiple of", y)
else:
    print('Not a multiple of', y)

