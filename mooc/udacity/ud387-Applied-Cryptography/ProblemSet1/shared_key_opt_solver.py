#!/usr/bin/env python
"""
shared-key-otp-solver.py

Requirements:
    * Python 2 or 3
    * six

Interactive solver for cyphertexts encrypted with shared one-time-pad.
Author: Cliff Chao-kuan Lu <clifflu@gmail.com>
License: CC0 / Public Domain
"""

import six.moves

def main():
    """
    Common entrypoint.
    """
    session = session_builder_applied_cryptography()
    io_loop(session)


def session_builder_applied_cryptography():
    """
    Creates OtpSolver session with parameters from Problem Set 1, Applied Cryptography.
    :return: OtpSolver as session
    :rtype: OtpSolver
    """
    C1 = "1010110010011110011111101110011001101100111010001111011101101011101000110010011000000101001110111010010111100100111101001010000011000001010001001001010000000010101001000011100100010011011011011011010111010011000101010111111110010011010111001001010101110001111101010000001011110100000000010010111001111010110000001101010010110101100010011111111011101101001011111001101111101111000100100001000111101111011011001011110011000100011111100001000101111000011101110101110010010100010111101111110011011011001101110111011101100110010100010001100011001010100110001000111100011011001000010101100001110011000000001110001011101111010100101110101000100100010111011000001111001110000011111111111110010111111000011011001010010011100011100001011001101110110001011101011101111110100001111011011000110001011111111101110110101101101001011110110010111101000111011001111"
    C2 = "1011110110100110000001101000010111001000110010000110110001101001111101010000101000110100111010000010011001100100111001101010001001010001000011011001010100001100111011010011111100100101000001001001011001110010010100101011111010001110010010101111110001100010100001110000110001111111001000100001001010100011100100001101010101111000100001111101111110111001000101111111101011001010000100100000001011001001010000101001110101110100001111100001011101100100011000110111110001000100010111110110111010010010011101011111111001011011001010010110100100011001010110110001001000100011011001110111010010010010110100110100000111100001111101111010011000100100110011111011001010101000100000011111010010110111001100011100001111100100110010010001111010111011110110001000111101010110101001110111001110111010011111111010100111000100111001011000111101111101100111011001111"

    session = OtpSolver(ascii_bits=7)
    session.load_cyphertext(C1, "bit_str")  # Loads C1 as channel 0
    session.load_cyphertext(C2, "bit_str")  # Loads C2 as channel 1

    # Keep track of confirmed guesses here

    # g(1, 0, "Space: the final frontier.")
    # Assumes "Space: the final frontier." as plaintext from channel 1 starting from pos 0

    return session


def io_loop(session):
    """
    REPL that parses user input, make guesses against Solver (session), and dump information from solver and wait for
    next guess.
    :param OtpSolver session:
    """
    while True:
        print("     " + "".join("{:<10d}".format(i) for i in range(12)))
        print("     " + "01234567890 2 4 6 8 " * 6)

        for channel in range(session.count_channels()):
            print("P%2d: %s" % (channel, session.get_plaintext(channel)))
        print("KEY: %s" % session.get_key())

        tmp = six.moves.input("Channel Pos Guess: ")

        tmp = tmp.split(" ")
        channel, pos, guess = tmp[0], tmp[1], tmp[2:]

        print(tmp)
        guess = " ".join(guess) if len(guess) > 0 else " "
        session.guess_str(int(channel), int(pos), guess)


class OtpSolver(object):
    """
    Encapsulates methods for handling multiple cyphertext channels with shared key. Also converts between ordinals and
    (printable) characters.
    """
    # Chars expected in plaintext.
    PRINTABLE_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456890. !@#$%^&*()-=_+[]{};':\",.<>/?"

    # Placeholder for chars awaiting key
    NONE_CHAR = "_"

    # Represents plaintext seems to be unprintable.
    FALLBACK_CHAR = "#"

    def ordinals_from_bit_str(self, bit_str):
        """
        Convert bit strings to list of ordinals.
        :param str bit_str: eg. "0001011", length must be N * ASCII_BITS
        :returns: Converted ordinals
        :rtype: list[int]
        """

        output = []
        for offset in range(0, len(bit_str), self._ascii_bits):
            bits = [int(c) for c in bit_str[offset:offset+self._ascii_bits]]
            output.append(sum([a * b for a, b in zip(bits, self._bit_values)]))

        return output

    @classmethod
    def decrypt(cls, ordinals, key):
        """
        Decrypt ordinals with given key using xor. Decrypt to None if key is none.
        :param list[int] ordinals: Cyphertext
        :param list[int] key: the key
        :returns: decrypted plaintext
        :rtype: list[int]
        """
        assert len(ordinals) == len(key)

        return [None if k is None else b ^ k for b, k in zip(ordinals, key)]

    @classmethod
    def printable_str_from_ordinals(cls, ordinals):
        """
        Convert ordinals to string. Unprintable characters (see PRINTABLE_CHARS) are replaced with FALLBACK_CHAR.
        :param list[int] ordinals: ordinals
        :returns: Converted string
        :rtype: str
        """
        return "".join(cls.NONE_CHAR if o is None else
                       chr(o) if chr(o) in cls.PRINTABLE_CHARS else
                       cls.FALLBACK_CHAR for o in ordinals)

    def __init__(self, ascii_bits=7):
        """
        Constructor.
        :param int ascii_bits: Number of bits in a character. Default=7
        :return: OtpSolver instance
        :rtype: OtpSolver
        """

        self._msg_len = None
        self._cyphertexts = []
        self._key = None
        self._ascii_bits = ascii_bits
        self._bit_values = [2 ** (ascii_bits - i - 1) for i in range(ascii_bits)]

    def load_cyphertext(self, cyphertext, format="ordinals"):
        """
        Load cyphertext into OtpSolver. All cyphertext must have same length for they were encrypted with the same OTP.
        Comment the assert clause if it's not true in your case.
        :param list[int]|str cyphertext: list of ordinals or strings of "0" and "1" representing bits.
        :param str format: "ordinal" or "bit_str"
        :return: channel id, 0-based
        :rtype: int
        """
        if format == "bit_str":
            cyphertext = self.ordinals_from_bit_str(cyphertext)

        if self._msg_len is None:
            self._msg_len = len(cyphertext)
            self._key = [None] * self._msg_len

        assert self._msg_len == len(cyphertext)
        self._cyphertexts.append(cyphertext)

        return len(self._cyphertexts)

    def guess_char(self, channel, pos, char):
        """
        Guess plaintext in specified channel and position.
        :param int channel: Channel ID
        :param int pos: 0-based offset for the character
        :param str char: The character
        """
        o = ord(char)
        self._key[pos] = o ^ self._cyphertexts[channel][pos]

    def guess_str(self, channel, pos, guess):
        """
        Guess plaintext in specified channel and position.
        :param int channel: Channel ID
        :param int pos: 0-based offset for the plaintext
        :param str guess: The plaintext
        """
        for c in guess:
            self.guess_char(channel, pos, c)
            pos += 1

    def get_plaintext(self, channel):
        """
        :param int channel: Channel ID
        :return: Printable representation of the plaintext
        """
        return self.printable_str_from_ordinals(self.decrypt(self._cyphertexts[channel], self._key))

    def get_key(self):
        """
        Compose a string representing current key status: NONE_CHAR if key is None, and FALLBACK_CHAR(#) otherwise.
        :return: String representing key status.
        :rtype: str
        """
        return "".join(self.FALLBACK_CHAR if k is not None else self.NONE_CHAR for k in self._key)

    def count_channels(self):
        """
        :return: Number of channels
        :rtype: int
        """
        return len(self._cyphertexts)

if __name__ == "__main__":
    main()
