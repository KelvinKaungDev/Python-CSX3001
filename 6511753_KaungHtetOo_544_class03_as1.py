x1 = int(input('Enter X1:'))
x2 = int(input('Enter X2:'))
x3 = int(input('Enter X3:'))

x1_by_x3 = x1 % x3
x2_by_x3 = x2 % x3

if (x1_by_x3 == 0) and (x2_by_x3 == 0) :
    print('x3 is a factor of both x1 and x2.')
elif (x1_by_x3 == 0) and (x2_by_x3 != 0) :
    print('x3 is a factor of x1.')
elif (x1_by_x3 != 0) and (x2_by_x3 == 0) :
    print('x3 is a factor of x2.')
else :
    print('x3 is neither a factor of x1 nor x2.')
