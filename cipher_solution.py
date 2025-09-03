# 141788964 - ID посылки
import sys


def helper(string_in: str):
    """This function finds the correct bracket sequence."""
    stack: list = []
    for i in string_in:
        if stack.count(']') > 0 and stack.count(']') == stack.count('['):
            break
        if i != ']':
            stack.append(i)
        else:
            if stack.count(']') != stack.count('['):
                stack.append(']')
    return ''.join(stack)


def perform_decryption(line: str, recursion_depth_flag: bool = False,
                       temp: list = None):
    """This function decrypts the received instruction."""
    if temp is None:
        temp = []
    value: int = 0
    digit: list = []
    while value < len(line):
        if line[value].isdigit():
            digit.append(line[value])
        elif line[value] == '[':
            recursion_depth_flag = True
            other: str = helper(line[value:])
            temp.append((int(''.join(digit)) - 1)
                        * perform_decryption(other[1:], recursion_depth_flag))
            digit = []
            recursion_depth_flag = False
        elif line[value] == ']':
            if recursion_depth_flag:
                return ''.join(temp)
        else:
            temp.append(line[value])
        value += 1
    return ''.join(temp)


if __name__ == '__main__':
    line_in = sys.stdin.readline().rstrip()
    print(perform_decryption(line_in))
