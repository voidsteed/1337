"""
Given k strings, find the longest common prefix (LCP).

Have you met this question in a real interview? Yes
Example
For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"

For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"

"""
import sys
def longestCommonPrefix(strs):
    # find the min length string in strs:
    minLen = sys.maxint
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    for s in strs:
        if minLen > len(s):
            minLen = len(s)

    for j in range(minLen):
        prev = '0'
        for i in range(len(strs)):
            print "before: " + "j: %d, i: %d, prev: %s"%(j, i,prev)
            if i == 0:
                prev = strs[i][j]
                continue
            if strs[i][j] != prev:
                return strs[i][0:j]
            print "after: " + "j: %d, i: %d, prev: %s"%(j,i,prev)
    return strs[0][0:minLen]



def main():
    s = ["ABCD", "ABEF", "ACEF"]
    ss = [ "ABCDEFG", "ABCEFG", "ABCEFA"]
    print longestCommonPrefix(s)
    print longestCommonPrefix(ss)

main()
