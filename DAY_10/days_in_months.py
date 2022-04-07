leap_or_not = False


def is_leap(year):
    '''This function return a boolean value stating whether the year entered is leap year or not.'''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_or_not = True
            else:
                leap_or_not = False
        else:
            leap_or_not = True
    else:
        leap_or_not = False

    return leap_or_not


def days_in_month(yr, month):
    '''This function will return the number of days in a month. The parameters are year and month in numeric.'''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_or_not = is_leap(yr)
    if(leap_or_not and (month == 2)):
        return month_days[1]+1
    return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
