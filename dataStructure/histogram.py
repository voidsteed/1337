"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.
"""
# average is O(n)
def largestRectangleArea(height):
    result = 0
    stack = []

    # Has to reach height's length
    for i in range(0,len(height)+1):
        curHeight = 0
        
        if len(height) == i:
            curHeight = 0
        else:
            curHeight = height[i]
        # check if the stack is empty
        while stack != []:
            if curHeight < height[stack[-1]]:
                heightId = stack.pop(-1)
                prev = -1
                if stack != []:
                    prev = stack[-1]
                result = max(result, (i - prev - 1) * height[heightId])
            else:
                break

        stack.append(i)

    return result

def main():
    l = [2,1,5,6,2,3]
    print largestRectangleArea(l)
main()
