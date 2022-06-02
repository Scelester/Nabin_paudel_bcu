#-------------------------------------------------------------------------#
#   scripted on Jun 2, 2022                                               |
#   by, Nabin Paudel                                                      |
#-------------------------------------------------------------------------#


def is_leap(year):
    """identifies if year is leap or not"""
    if year % 4 != 0:
        return False
    else:
        # when the year is not a century
        if year % 100 != 0:
            return True
        else:
            # can the given century can be divided by 400
            if year % 400 == 0:
                # yes! it is a leap year
                return True
            else:
                # no! it is no a leap year
                return False


def days_in_month(month, year):
    """returns the number of days in month of a particular year"""
    leap_yd = 0
    if is_leap(year):
        leap_yd = 1

    month_list = ["January", "February", "March", "April", "May",
                  "June", "July", "August", "September", "October",
                  "November", "December"]

    # incase year is invalid
    if type(year) != int:
        return 0
    elif year > 10000 or year < 1:
        return 0

    # try except block incase invalid month is given
    # inwhich case list.index() will give ValueError
    try:
        month_index = month_list.index(month) + 1
    except ValueError:
        return 0

    month_with_31 = [1, 3, 5, 7, 8, 10, 12]

    # for february and leap year
    if month_index == 2:
        return 28 + leap_yd
    elif month_index in month_with_31:
        return 31
    else:
        return 30


def day_of_date(month, day):
    """of year 2021 only"""
    total_days = 0
    month_with_31 = [1, 3, 5, 7, 8, 10, 12]
    for n in range(1, month):
        if n == 2:
            total_days += 28
        elif n in month_with_31:
            total_days += 31
        else:
            total_days += 30

    total_days += day

    # since 2021 started with friday listing it that way
    weekdays = ['Friday', 'Saturday', 'Sunday', 'Monday',
                'Tuesday', 'Wednesday',
                'Thursday', ]

    # dividing by 7 for each day in week
    day = total_days % 7

    return weekdays[day - 1]


# tesing results/code
if __name__ == '__main__':
    print(is_leap(2000))
    print(is_leap(2021))
    print()
    print(days_in_month("March", 1999))
    print(days_in_month("Haha", 2004))
    print()
    print(day_of_date(11, 1))
    print(day_of_date(8, 21))
