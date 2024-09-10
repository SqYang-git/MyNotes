def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 'Y'
            else:
                return 'N'
        else:
            return 'Y'
    else:
        return 'N'


year = int(input())
result = is_leap_year(year)
print(result)
