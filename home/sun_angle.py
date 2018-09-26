"""
Sun Angle


Every true traveler must know how to do 3 things: fix the fire,
find the water and extract useful information from the nature around him.
Programming won't help you with the fire and water,
but when it comes to the information extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the day.
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees.
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees.
If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
your function should return - "I don't see the sun!".

Input: The time of the day.
Output: The angle of the sun, rounded to 2 decimal places.
Precondition:
00:00 <= time <= 23:59
"""

ONE_MIN_IN_GRAD = 180 / 12 / 60
MINS_IN_DAY = 12 * 60
NO_SUN = "I don't see the sun!"


def minutes(time: str) -> float:
    hours, minutes = time.split(":")
    return (int(hours) - 6) * 60 + int(minutes)


def sun_angle(time):

    mins = minutes(time)

    if 0 <= mins <= MINS_IN_DAY:
        return round(mins * ONE_MIN_IN_GRAD, 2)

    return NO_SUN


if __name__ == "__main__":
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == NO_SUN
    assert sun_angle("18:01") == NO_SUN
