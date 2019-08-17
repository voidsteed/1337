def backpack(m, A):
    if len(A) == 0 or m < 1:
        return 0
    f = [[False for x in range(m+1)] for x in range(len(A)+1)]
    f[0][0] = True
    for i in range(len(A)):
        for j in range(m+1):
            f[i+1][j] = f[i][j]
            if j>=A[i] and f[i][j-A[i]]:
                f[i+1][j] = True
    for i in range(m,-1,-1):
        if f[len(A)][i]:
            return i
    return 0

def main():
    A = [2,3,5,7]
    print backpack(11,A)
    print backpack(12,A)
main()
