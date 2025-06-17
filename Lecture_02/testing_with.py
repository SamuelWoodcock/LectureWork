def format_date(day: object, month: object, year: object) -> str:
    return f'{day}/{month}/{year}'

date = (22,11,1988)
format_date(*date)

print(format_date(*date))


