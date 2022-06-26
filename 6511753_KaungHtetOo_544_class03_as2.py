x1 = int(input('Enter first number:'))
x2 = int(input('Enter second number:'))
x3 = int(input('Enter third number:'))
x4 = int(input('Enter fourth number:'))

sum_all           = x1 + x2 + x3 + x4;
check_even_or_odd = sum_all % 2

if (sum_all > 0) and (check_even_or_odd == 0) :
    print(f'{sum_all} is Positive Even')
elif (sum_all > 0) and (check_even_or_odd != 0) :
    print(f'{sum_all} is Positive Odd')
elif (sum_all < 0) and (check_even_or_odd == 0) :
    print(f'{sum_all} is Negative Even')
elif (sum_all < 0) and (check_even_or_odd != 0) :
    print(f'{sum_all} is Negative Odd')
elif (sum_all == 0) :
    print(f'{sum_all} is zero')
