"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example
Given [2->4->null,null,-1->null], return  -1->2->4->null
"""
import heapq
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
# Method 1 using Min Heap to solve
def mergeKLists(lists):
    # write your code here
    heap = []
    for node in lists:
        if node != None:
            heap.append((node.val,node))
    heapq.heapify(heap)
    # set up for dummy node
    head = ListNode(0)
    cur = head

    while heap:
        pop = heapq.heappop(heap)
        cur.next = ListNode(pop[0])
        cur = cur.next
        # the node.next is not None
        if pop[1].next:
            heapq.heappush(heap,(pop[1].next.val,pop[1].next))
    return head.next
"""
# Method 2 using divide and conquer
def mergeKLists(lists):
    if len(lists) == 0:
        return None

    while len(lists) > 1:
        nextLists = []
        for i in range(0,len(lists)-1,2):
            nextLists.append(merge2Lists(lists[i],lists[i+1]))
        if len(lists) % 2 ==1:
            nextLists.append(lists[len(lists)-1])
        lists = nextLists

    return lists[0]

def merge2Lists(l1,l2):
    head = ListNode(0)
    cur = head
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1 != None:
        cur.next = l1
    if l2 != None:
        cur.next = l2
    cur = head
    head = head.next
    return head
        

def main():
    a = ListNode(2)
    b = ListNode(4)
    a.next = b
    c = None
    d = ListNode(-1)
    e = ListNode(1)
    lst = [a,c,d]
    lst2 = [ListNode(2),None,d]
    nn = mergeKLists(lst2)
    #nn = mergeKLists(test3)
    while nn:
        print nn.val
        nn = nn.next
main()
