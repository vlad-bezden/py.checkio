"""AMSCO Cipher

    https://py.checkio.org/en/mission/amsco-cipher/
"""

from itertools import zip_longest, accumulate


class Decoder:
    @classmethod
    def decode(cls, message: str, key: int):
        d = cls(message, str(key))
        matrix = d._matrix()
        columns = d._fill_in(matrix)
        return d._decode(matrix, columns)

    def __init__(self, message: str, key: int) -> None:
        self._message = message
        self._key = str(key)

    def _matrix(self):
        """Creates matrix with size for each position."""
        matrix = []
        one_two = 0
        counter = 0
        row = []
        message_size = len(self._message)
        key_size = len(self._key)

        while counter < message_size:
            # create new row
            if len(row) % key_size == 0:
                row = []
                matrix.append(row)

            # new row, check for the first char in the row
            if not row:
                one_two = 1 if len(matrix) % 2 == 1 else 2
            # check if it's the last char in the message
            elif message_size - counter <= 1:
                one_two = 1
            # default, alternate between 1 and 2
            else:
                one_two = 1 if one_two == 2 else 2
            row.append(one_two)
            counter += one_two

        # rotate matrix
        return list(zip_longest(*matrix, fillvalue=0))

    def _fill_in(self, matrix):
        """Get words (string) for each column."""

        col_sizes = [sum(i) for i in matrix]
        # sort col_sizes based on the key position
        ordered_col_sizes = [None] * len(self._key)
        for i, k in enumerate(self._key):
            ordered_col_sizes[int(k) - 1] = col_sizes[i]

        start = 0
        columns = []
        # get starting point for each word in the message
        for i in list(accumulate(ordered_col_sizes)):
            columns.append(self._message[start:i])
            start = i
        return columns

    def _decode(self, matrix, columns):
        """Decodes columns to final message."""
        chars_matrix = []

        for i, k in enumerate(self._key):
            word = columns[int(k) - 1]
            sizes = matrix[i]
            start = 0
            word_of_chars = []
            for w in sizes:
                word_of_chars.append(word[start : start + w])
                start += w
            chars_matrix.append(word_of_chars)

        decoded_word = "".join("".join(i) for i in list(zip(*chars_matrix)))
        return decoded_word


def decode_amsco(message, key):
    return Decoder.decode(message, key)


if __name__ == "__main__":
    assert (
        decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet"
    ), "Lorem Ipsum"
    assert decode_amsco("kicheco", 23415) == "checkio", "Checkio"
    assert (
        decode_amsco("hrewhoorrowyilmmmoaouletow", 123) == "howareyouwillhometommorrow"
    ), "How are you"
    print("PASSED!")
