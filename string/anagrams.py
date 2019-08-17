"""
Write a method anagram(s,t) to decide if two strings are anagrams or not.

Example
Given s="abcd", t="dcab", return true.
"""
# The strategy is trying to count how many times a char appears in the string

def anagram(s, t):
    # length has to be the same
    ss = [0] * 256
    tt = [0] * 256

    for i in range(len(s)):
        pos = ord(s[i])
        ss[pos] = ss[pos] + 1
    for j in range(len(t)):
        pos = ord(t[j])
        tt[pos] = tt[pos] + 1

    for k in range(len(ss)):
        if ss[k] != tt[k]:
            return False
    return True


def main():
    s = "abcd"
    t = "dcab"
    c = "aabd"
    #print anagram(s,t)
    print anagram(s,c)
main()
