"""
Given two strings, find the longest common substring.

Return the length of it.

Have you met this question in a real interview? Yes
Example
Given A = "ABCD", B = "CBCE", return 2.
"""
def longestCommonSubstring(A, B):
    # write your code here
    maxLen = 0
    aLen = len(A)
    bLen = len(B)
    for i in range(aLen):
        for j in range(bLen):
            resultLen = 0
            while i + resultLen < aLen and j + resultLen < bLen and A[i+resultLen] == B[j+resultLen]:
                resultLen += 1
            if (resultLen > maxLen):
                print "I'm in IFFFF"
                maxLen = resultLen

    return maxLen

def main():
    a = "ABCD"
    b = "CBCE"

    print longestCommonSubstring(a,b)

main()
