"""
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
"""
def twoSum(lst,target):
    dic = {}
    for i in range(0,len(lst)):
        x = lst[i]
        if target - x in dic.keys():
            return [i,lst.index(target - x)]
        dic[x] = i

def main():
    l = [2,7,11,15]
    print twoSum(l,9)

main()

