def is_leap(y):
    return y % 400 == 0 or y % 4 == 0 and y % 100 != 0


def days_in_month(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m == 2 and is_leap(y):
        return 29
    return month_days[m - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












