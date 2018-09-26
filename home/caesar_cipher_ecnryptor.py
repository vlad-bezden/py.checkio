"""
Caesar Cipher (encryptor)

Your mission is to encrypt a secret message
(text only, without special chars like "!", "&", "?" etc.)
using Caesar cipher where each letter of input text is replaced
by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"

Input: A secret message as a string (lowercase letters only and white spaces)

Output: The same string, but encrypted

Precondition:
0 < len(text) < 50
-26 < delta < 26
"""

from string import ascii_lowercase


def to_encrypt(text, delta):
    return "".join(
        [
            ascii_lowercase[(ord(c) - 97 + delta) % 26] if c.isalpha() else c
            for c in text
        ]
    )


if __name__ == "__main__":
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
