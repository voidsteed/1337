"""
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.
"""

def compareStrings(A, B):
    ss = [0] * 256
    tt = [0] * 256

    for i in range(len(A)):
        pos = ord(A[i])
        ss[pos] = ss[pos] + 1
    for j in range(len(B)):
        pos = ord(B[j])
        tt[pos] = tt[pos] + 1

    for k in range(len(ss)):
        if ss[k] < tt[k]:
            return False
    return True

def main():
    A = "ABCD"
    B = "ABC"
    C = "AABC"
    print compareStrings(A,B)
    print compareStrings(A,C)
main()
