"""
You prefer a good old 12-hour time format.
But the modern world we live in would rather use the 24-hour format and you see
it everywhere. Your task is to convert the time from the 24-h format into
12-h format by following the next rules:
- the output format should be 'hh:mm a.m.'
(for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'

Input: Time in a 24-hour format (as a string).
Output: Time in a 12-hour format (as a string).

Precondition:
'00:00' <= time <= '23:59'
"""


def time_converter(time: str) -> str:
    hours, minutes = map(int, time.split(":"))
    return f"{(hours - 1) % 12 + 1}:{minutes:02d} {'ap'[11 < hours]}.m."


if __name__ == "__main__":
    assert time_converter("12:30") == "12:30 p.m."
    assert time_converter("09:00") == "9:00 a.m."
    assert time_converter("23:15") == "11:15 p.m."
    assert time_converter("00:00") == "12:00 a.m."

    print("DONE!")
