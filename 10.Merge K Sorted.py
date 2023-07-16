class Node:
    def __init__(self):
        self.data = 0
        self.next = None

def printList(node):
    while (node != None):
        print(node.data, end=' ')
        node = node.next
def newNode(data):
    temp = Node()
    temp.data = data
    temp.next = None
    return temp

no_of_lists = 3

arr = [0 for i in range(no_of_lists)]

arr[0] = newNode(1)
arr[0].next = newNode(3)
arr[0].next.next = newNode(5)
arr[0].next.next.next = newNode(7)

arr[1] = newNode(2)
arr[1].next = newNode(4)
arr[1].next.next = newNode(6)
arr[1].next.next.next = newNode(8)

arr[2] = newNode(0)
arr[2].next = newNode(9)
arr[2].next.next = newNode(10)
arr[2].next.next.next = newNode(11)

def mergeTwoSorted(l1 , l2):
    result = None
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.data > l2.data:
        result = l2
        result.next = mergeTwoSorted(l1, l2.next)
    else:
        result = l1
        result.next = mergeTwoSorted(l1.next,l2)

    return result

def mergeKlist(arr ,end):
    while (end > 0):
        i = 0
        j = end
        while (i<j):
            arr[i] = mergeTwoSorted(arr[i],arr[j])
            i = i+1
            j = j-1
            if i >= j:
                end = j
    return arr[0]

ans = mergeKlist(arr , len(arr)-1)
printList(ans)