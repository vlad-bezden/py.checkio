"""
Help Sofia write a decrypter for the passwords that Nikola will encrypt
through the cipher map. A cipher grille is a 4×4 square of paper with four
windows cut out. Placing the grille on a paper sheet of the same size,
the encoder writes down the first four symbols of his password inside
the windows (see fig. below). After that, the encoder turns the grille
90 degrees clockwise. The symbols written earlier become hidden under
the grille and clean paper appears inside the windows.
The encoder then writes down the next four symbols of the password in
the windows and turns the grille 90 degrees again. Then, they write down
the following four symbols and turns the grille once more.
Lastly, they write down the final four symbols of the password.
Without the same cipher grille, it is difficult to discern the
password from the resulting square comprised of 16 symbols.
Thus, the encoder can be confident that no hooligan will easily gain access
to the locked door.

Write a module that enables the robots to easily recall their passwords
through codes when they return home.
The cipher grille and the ciphered password are represented as an
array (tuple) of strings.
Input: A cipher grille and a ciphered password as a tuples of strings.
Output: The password as a string.
Precondition: len(cipher_grille) == 4
len(ciphered_password) == 4
all(len(row) == 4 for row in ciphered_password)
all(len(row) == 4 for row in cipher_grille)
all(all(ch in string.ascii_lowercase for ch in row)
for row in ciphered_password)
all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)

"""

GRILL_SIDES = 4
PUNCH_WHOLE = 'X'


def rotate_matrix(cipher_grille):
    """Rotates matrix by 90 degrees."""
    column_index = 0
    new_grille = []
    # take column by column and convert it to row
    while column_index < len(cipher_grille):
        row = ''.join(
            [row[column_index]
             for row in reversed(cipher_grille)]
        )
        new_grille.append(row)
        column_index += 1
    return tuple(new_grille)


def grille_generator(cipher_grille):
    """Rotates cipher grill 4 times and generates new cipher grill."""
    for i in range(GRILL_SIDES):
        yield cipher_grille
        cipher_grille = rotate_matrix(cipher_grille)


def word_from_cipher_grille(cipher_grille, ciphered_password):
    """Applies grille to cipher and gets word from it."""
    word = ''
    for i, row in enumerate(cipher_grille):
        for j, item in enumerate(row):
            if item.upper() == PUNCH_WHOLE:
                word += ciphered_password[i][j]
    return word


def recall_password(cipher_grille, ciphered_password):
    deciphered_password = ''
    for grill in grille_generator(cipher_grille):
        deciphered_password += word_from_cipher_grille(
            grill,
            ciphered_password)
    return deciphered_password


if __name__ == '__main__':
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
