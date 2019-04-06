"""
Time Converter (12h to 24h)

You are the modern man who prefers the 24-hour time format.
But the 12-hour format is used in some places.
Your task is to convert the time from the 12-h format into 24-h by
following the next rules:
- the output format should be 'hh:mm'
- if the output hour is less than 10 - write '0' before it. For example: '09:05'
Here you can find some useful information about the 12-hour format.

Input: Time in a 12-hour format (as a string).
Output: Time in a 24-hour format (as a string).
Example:

time_converter('12:30 p.m.') == '12:30'
time_converter('9:00 a.m.') == '09:00'
time_converter('11:15 p.m.') == '23:15'

Precondition:
'00:00' <= time <= '23:59'
"""


def time_converter(time: str) -> str:
    hours, minutes = map(int, time[:-5].split(":"))
    hours = hours % 12 + 12 * ("p" in time)
    return f"{hours:02}:{minutes:02}"


if __name__ == "__main__":
    assert time_converter("12:30 p.m.") == "12:30"
    assert time_converter("9:00 a.m.") == "09:00"
    assert time_converter("11:15 p.m.") == "23:15"
    assert time_converter("12:00 a.m.") == "00:00"
    print("DONE!")
