def countBits(n):
    binary = '{0:b}'.format(n)
    cnt = 0
    print(binary)
    for i in binary:
        if i == '1':
            cnt += 1
            print(cnt)
    return cnt
countBits(1234)