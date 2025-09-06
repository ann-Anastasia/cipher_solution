# 141908481 - ID посылки
import sys
from string import digits, ascii_letters


def perform_decryption(line: list):
    """This function decrypts the received instruction."""
    temp: str = ''
    digit: str = ''
    while len(line) > 0:
        value: str = line.pop(0)
        if value in ascii_letters:
            temp += value
        elif value in digits:
            digit += value
        elif value == '[':
            temp += int(digit) * perform_decryption(line)
            digit = ''
        elif value == ']':
            return temp
    return temp


if __name__ == '__main__':
    line_in = sys.stdin.readline().rstrip()
    print(perform_decryption(list(line_in)))
