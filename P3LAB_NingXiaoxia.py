# Xiaoxia Ning
# 3/15/2024
# P3LAB
# This is a program that takes in a year and determines whether that year is a leap year.
is_leap_year = False

input_year = int(input("Which year do you want to check?"))

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
           is_leap_year = True
    else:
        is_leap_year = True
if is_leap_year:
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")