import math
import fractions
def countBits(n):
    binary = '{0:b}'.format(n)
    cnt = 0
    print(binary)
    for i in binary:
        if i == '1':
            cnt += 1
            print(cnt)
    return cnt
# countBits(1234)


def zeros(n):
    result = math.factorial(n)
    tgt = str(result)
    cnt = 0
    cur_cnt = 0
    for char in tgt:
        if char == '0':
            if cur_cnt >= cnt:
                cnt += 1
            cur_cnt += 1
        else:
            cur_cnt = 0
    return cnt


def nbr_of_laps(x, y):
    n1 = max([x, y])
    n2 = min([x, y])
    GCD = math.gcd(n1, n2)
    print(GCD)
    LCM = (x*y)/GCD
    print(LCM)
    return [int(LCM/x), int(LCM/y)]

print(nbr_of_laps(6608,7249))