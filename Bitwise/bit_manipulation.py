# index for bits: [7,6,5,4,3,2,1,0]

def set_bit(x, position):
    '''
    x = 00000110 = 6
    1 = 00000001
    position = 00000101 = index 5
    mask = 00100000 = moved 1 to index 5(position)
    x | mask = 00100110 = 38
    '''
    mask = 1 << position
    return x | mask
print('set bit 0b000110: ', set_bit(6,5), bin(set_bit(6,5)))

def clear_bit(x, position):
    '''
    x = 00000110 = 6
    1 = 00000001
    position = 00000010 = 2 (index)
    mask = 00000100 = moved 1 to index 2
    ~mask = 11111011
    x&~mask = 00000010 = 2
    no longer bit at position given
    '''
    mask = 1 << position
    return x &~ mask
print('clear bit 0b000110: ', clear_bit(6,2), bin(clear_bit(6,2)))

def flip_bit(x, position):
    '''
    x = 01100110 = 102
    position = 00000010 = so flip the bit at index 2
    mask = 00000100
    x^mask = 01100010
    '''
    mask = 1 << position
    return x ^ mask
print('flip bit 0b1100110: ', flip_bit(102,2), bin(flip_bit(102,2)))

def set_bit(x, position):
    '''
    returns boolean True if bit is 1 else False
    x = 01100110 = 102
    position = 00000101 = 5 (bit at index 5 shifts to right most column)
    shifted = 00000011
    if value at index 0 is 1 returns True, else returns False
    '''

    shifted = x >> position
    return bool(shifted & 1)
print('is bit set at index 5? 0b1100110: ', set_bit(102,5))
print('is bit set at index 3? 0b1100110: ', set_bit(102,3))

def modify_bit(x, position, state=1):
    '''
    x = 00000110 01100110 = 6
    position = 5
    state = 00000001 (is state=1 set bit, state=0 means clear bit)
    mask = 00100000
    ~mask = 11011111
    -state = 11111111 = -1 or 00000000 = "-0"
    x&~mask = 00000110
    ~state&mask = 00100000
    x&~mask|~state&mask = 00100110
    '''
    mask = 1<<position
    return (x & ~mask) | (-state & mask)
print('modify bit 0b000110: ', modify_bit(6,5), bin(modify_bit(6,5)))

def even_bit(x):
    '''
    if bit is even returns True else False
    '''
    mask = 1
    return x&1==0

print('even_bit 000000001:', even_bit(1))
print('even_bit 000000010:', even_bit(2))

def powerTwo_bit(x):
    '''
    checks if bit is power of two
    '''
    return (x & x-1) == 0
print('powerTwo_bit 000000001:', powerTwo_bit(1))
print('powerTwo_bit 000000010:', powerTwo_bit(2))

def countDiff_bit(x,y):
    '''
    counts # of bits different btwn two #'s
    '''
    count = 0
    for position in range(0,8):
        mask = 1 << position
        if x&mask != y&mask:
            count +=1
    return count
print('Count different bits 00000001 & 00000011: ', countDiff_bit(1,3))
print('Count different bits 00000001 & 00000010: ', countDiff_bit(1,2))
print('Count different bits 00000001 & 00000001: ', countDiff_bit(1,1))