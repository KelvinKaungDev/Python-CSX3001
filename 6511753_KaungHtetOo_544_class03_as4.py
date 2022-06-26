input_five_digits = int(input('Enter 5 digits numbers:'))
first_digit = input_five_digits // 10000
second_digit = ( input_five_digits // 1000 ) % 10
third_digit = ( input_five_digits // 100 ) % 10
fourth_digit = ( input_five_digits // 10 ) % 10
fifth_digit = input_five_digits % 10

swap_last_and_first_digit = fifth_digit * 10000 + second_digit * 1000 + third_digit * 100 + fourth_digit * 10 + first_digit;
swap_fourth_and_second_digit = first_digit * 10000 + fourth_digit * 1000 + third_digit * 100 + second_digit * 10 + fifth_digit;

if len(str(input_five_digits)) < 5 or len(str(input_five_digits)) > 5 :
    print('Wrong Input. Try Again.')
elif len(str(input_five_digits)) == 5 and third_digit > (first_digit + second_digit + fourth_digit + fifth_digit) :
    print(f'The output is {swap_last_and_first_digit}')
elif len(str(input_five_digits)) == 5 and third_digit < (first_digit + second_digit + fourth_digit + fifth_digit) :
    print(f'The output is {swap_fourth_and_second_digit}')
elif len(str(input_five_digits)) == 5 and third_digit == (first_digit + second_digit + fourth_digit + fifth_digit) :
    print(f'The output is {input_five_digits}')

