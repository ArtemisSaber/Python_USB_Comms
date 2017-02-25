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


def match_brackets(string):  # 这个用正则做在前面有额外字符的情况下会出错，原因不详
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

# print(match_brackets('hi(hi)()'))


def duplicate_encode(string):
    string = string.lower()
    processed_string = ''
    for char in string:
        i = string.count(char)
        if i != 1:
            processed_string += ')'
        else:
            processed_string += '('
    return processed_string


# print(duplicate_encode('string'))


def pig_it(text):
    # your code here
    word_list = text.split(' ')
    processed_str = ''
    print(word_list)
    for word in word_list:

        word = word[1:]+word[0]+'ay '
        processed_str += word
    return processed_str.strip(' ')

print(pig_it('This is an example with non char !'))