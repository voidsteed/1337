"""
Example
If source="source" and target="target", return -1.

If source="abcdabcdefg" and target="bcd", return 1.

Challenge
"""

def strStr(source, target):
    # source or target is empty
    if source == '' and target == '':
        return 0
    if source == '' or source == None or target == None:
        return -1
    
    if target == '':
        return 0

    for i in range(len(source)):
        if(i + len(target) > len(source)):
            return -1
        m = i
        for j in range(len(target)):
            #print "target: ",target[j],"source: ",source[m]
            if target[j] == source[m]:
                if(j == len(target)-1):
                    return i
                m += 1
            else:
                break

    return -1



def main():
    s = "source"
    t = "target"
    ss = "abcdabcdefg"
    tt = "bcd"
    #print strStr(s,t)
    print strStr(ss,tt)
    print strStr('','a')
main()
