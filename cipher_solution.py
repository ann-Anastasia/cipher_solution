# 141864540 - ID посылки
import sys
from string import digits, ascii_lowercase, ascii_uppercase


def perform_decryption(line: str):
    """This function decrypts the received instruction."""
    temp: str = ''
    value: int = 0
    digit: str = ''
    recursion_depth_flag: bool = False
    while value < len(line):
        if line[value] in ascii_lowercase or line[value] in ascii_uppercase:
            temp += line[value]
        elif line[value] in digits:
            digit += line[value]
        elif line[value] == '[':
            recursion_depth_flag: bool = True
            index_line_end: int = 0
            count_bracket: int = 0
            for index, val in enumerate(line[value + 1:]):
                if val == '[':
                    count_bracket += 1
                elif val == ']' and count_bracket == 0:
                    index_line_end = index
                    break
                elif val == ']':
                    count_bracket -= 1
            recursion_result = perform_decryption(line[value + 1:
                                                       value + 1 +
                                                       index_line_end])
            temp += (int(digit) - 1) * recursion_result
            digit = ''
            recursion_depth_flag = False
        else:
            if recursion_depth_flag:
                return temp
        value += 1
    return temp


if __name__ == '__main__':
    line_in = sys.stdin.readline().rstrip()
    print(perform_decryption(line_in))
