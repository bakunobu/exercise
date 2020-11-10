def is_leap_year(year):
    IsLeapYear = (year % 4 == 0)
    IsLeapYear = IsLeapYear and ((year % 100) != 0)
    IsLeapYear = IsLeapYear or ((year % 400) == 0)
    return(IsLeapYear)

print(is_leap_year(2000))
print(is_leap_year(1987))
print(is_leap_year(2010))