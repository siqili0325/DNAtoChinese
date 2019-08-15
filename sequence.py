 #!/usr/bin/python
 #coding:utf-8

import codecs

def baseToBin(c):
    if c == 'A':
        return 0b00
    if c == 'T':
        return 0b01
    if c == 'C':
        return 0b10
    if c == 'G':
        return 0b11

def sequenceToBin(s):
    res = 0
    for base in s:
        base = baseToBin(base)
        res = (res << 2) + base
    return res


#
# u4e00-u9fa5 (中文)
def binToChinese(b):
    hexStr = "\\u" + format(b % (0x9fa5 - 0x4e00) + 0x4e00, 'x')
    return codecs.encode(hexStr, "utf-8").decode("unicode_escape")


def sequenceToChinese(s):
    b = sequenceToBin(s)
    return binToChinese(b)







    
s = sequenceToChinese("ATCGATCGG")
s = sequenceToChinese("ATCGATCGG")
s = sequenceToChinese("ATCGATCGG")
s = sequenceToChinese("ATCGATCGG")

print(s)
"""
s1 = sequenceToBin("T")
s2 = sequenceToBin("TT")
s3 = sequenceToBin("TTT")
s4 = sequenceToBin("TTTT")
s5 = sequenceToBin("TTTTT")
s6 = sequenceToBin("TTTTTT")
s7 = sequenceToBin("TTTTTTT")
s8 = sequenceToBin("TTTTTTTT")
s9 = sequenceToBin("TTTTTTTTT")
s10 = sequenceToBin("TTTTTTTTTT")

#s = sequenceToChinese("ATCGATCG")


print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(s8)
print(s9)
print(s10)
"""