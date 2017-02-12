import re


def find_missing_letter(chars):
    start = ord(chars[0])
    end = ord(chars[-1])
    cnt = 0
    for i in range(start, end):
        if chr(i) != chars[cnt]:
            print(chr(i))
            return chr(i)
        cnt += 1

# find_missing_letter(['a', 'b', 'c', 'd', 'f'])


def match_brackets(string):
    free_open = 0
    free_close = 0
    for char in string:
        if char == '(':
            free_open += 1
        if char == ')':
            if free_open > 0:
                free_open -= 1
            else:
                free_close += 1
    if free_open == 0 and free_close == 0:
        return True
    else:
        return False

#print(match_brackets('hi(hi)()'))
