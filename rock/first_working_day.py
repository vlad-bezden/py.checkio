"""The First Working Day

As the input you will get the date of the first day of the vacation in the format
'YYYY-MM-DD' and the number of days of the vacation.
Your task is to find out which day will be the first working day after the vacation.
If it will be Saturday or Sunday then it should be the next Monday.
In this mission you should ignore the national holidays and consider only Saturdays and Sundays.
Also don't forget about February 29th in the leap year and about
the situation when the start of the vacation is at the end of the
December of the one year and the end of it is at the beginning of the next year.

Input: First day of the vacation and number of days of it.

Output: Date of the first working day.

Precondition:
1900 <= year <= 2100
"""


def vacation(date: str, days: int) -> int:
    return 0


if __name__ == "__main__":
    assert vacation("2018-07-01", 14) == "2018-07-16"
    assert vacation("2018-02-19", 10) == "2018-03-01"
    assert vacation("2000-02-28", 5) == "2000-03-06"
    assert vacation("1999-12-20", 14) == "2000-01-03"
