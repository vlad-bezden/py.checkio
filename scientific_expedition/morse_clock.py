"""Morse Clock

Help Stephen to create a module for converting a normal time string to a
morse time string. As you can see in the illustration, a gray circle means on,
while a white circle means off.
Every digit in the time string contains a different number of slots.
The first digit for the hours has a length of 2 while the second digit for
the hour has a length of 4. The first digits for the minutes and seconds have a
length of 3 while the second digits for the minutes and seconds have a length of 4.
Every digit in the time is converted to binary representation.
You will convert every on (or 1) signal to dash ("-") and every off (or 0) signal
to dot (".").

An time string could be in the follow formats: "hh:mm:ss", "h:m:s" or "hh:m:ss".
The "missing" digits are zeroes. For example, "1:2:3" is the same as "01:02:03".

The result will be a morse time string with specific format:
"h h : m m : s s"
where each digits represented as sequence of "." and "-"

Input: A normal time string as a string (unicode).
Output: The morse time string as a string.

Example:
checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"


Precondition:
time_string contains correct time.
"""

TO_MORSE = str.maketrans("01", ".-")

fmt = lambda n, s=3: f"{int(n[0]):0{s}b} {int(n[1]):04b}"


def checkio(time: str) -> str:
    h, m, s = [f"0{i}"[-2:] for i in time.split(":")]
    return f"{fmt(h, 2)} : {fmt(m)} : {fmt(s)}".translate(TO_MORSE)


if __name__ == "__main__":
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

    print("DONE!!!")
