"""
序列示例
"""

# 1-12月的序列
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# 以 1-31 的数字作为结尾的列表
endings = ['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']

year = input('Year: ')
month = input('Month（1-12）：')
day = input('Day（1-31）：')

month_number = int(month)
day_number = int(day)

# 月份与天数减一，获取正确索引
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print(month_name + ' ' + ordinal + '，' + year)

