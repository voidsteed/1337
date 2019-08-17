"""
Given an array of strings, return all groups of strings that are anagrams.

Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Note
All inputs will be in lower-case
"""
def anagrams(strs):
    # write your code here
    result = []
    dic = {}
    for s in strs:
        # Now I have sorted string
        sort_string = ''.join(sorted(s))
        # Now I have the origin string index and sorted string
        # Add the indexes of all same anagram into a list
        if sort_string not in dic.keys():
            dic[sort_string] = [s]
        else:
            dic[sort_string] = dic[sort_string] + [s]

    for value in dic.values():
        if len(value) >= 2:
            result += value
    return result

def main():
    strs = ["lint", "intl", "inlt", "code"]
    ss = ["ab", "ba", "cd", "dc", "e"]
    print anagrams(strs)
    print anagrams(ss)
main()
