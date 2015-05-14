"""
Similar to Question [1. Two Sum], except that the input array is already sorted in ascending order.
"""
#list is sorted
def twoSum(lst,target):
    i = 0
    j = len(lst) - 1
    while i < j:
        sumOfTwo = lst[i] + lst[j]
        if sumOfTwo < target:
            i += 1
        elif sumOfTwo > target:
            j -= 1
        else:
            return [i+1,j+1]

def main():
    l = [2,7,11,15]
    print twoSum(l,9)

main()
