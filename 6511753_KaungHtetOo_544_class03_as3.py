import math

shoppng_amount           = int(input('Enter shopping amount (in baht):'))
shopping_hour            = int(input('Enter shopping hours:'))
shopping_minute          = int(input('Enter shopping minutes:'))
shopping_parking_fee     = 30
shopping_total_in_hour   = shopping_hour + (shopping_minute / 60)
shopping_total_in_minute = shopping_hour * 60 + shopping_minute

if (shoppng_amount >= 1500) and (shopping_total_in_minute > 120) :
    print(f'The parking fee is {shopping_parking_fee} baht.')
elif (shoppng_amount < 500) and (shopping_total_in_minute > 60) :
    time_to_pay_parking_fee = shopping_total_in_minute - 60
    pay_for_parking_fee     = 30 * ( math.ceil(time_to_pay_parking_fee / 30) )
    print(f'The parking fee for the first hour is free. You have to pay {pay_for_parking_fee} baht for the parking fee.')
elif (shoppng_amount >= 500) and (shopping_total_in_minute > 120) :
    time_to_pay_parking_fee = shopping_total_in_minute - 120
    pay_for_parking_fee     = 30 * ( math.ceil(time_to_pay_parking_fee / 30) )
    print(f'The parking fee for the first 2 hours is free. You have to pay {pay_for_parking_fee} Baht for the parking fee.')
