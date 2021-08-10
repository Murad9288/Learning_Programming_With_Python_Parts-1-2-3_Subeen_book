
'''

#The list size limit in heap

heap = [None]*10
print("The size limit =",heap)

heap[1] = 19
heap[1*2] = 7
heap[1*2+1] = 17
print("Update heap list =",heap)


heap[2*2] = 3
heap[2*2+1] = 5
heap[3*2] = 12
heap[3*2+1] = 10
heap[4*2] = 1
heap[4*2+1] = 2
print("Update Heap list =",heap)
'''

# কোনো Tree-নোডে right-চাইল্ডে কে আছে সেইটা দেখতে হলে (2*1) করতে হবে।
def left(i):
    return 2*i

# কোনো Tree-নোডে left-চাইল্ডে কে আছে সেইটা দেখতে হলে (2*i+1) করতে হবে।
def right(i):
    return 2*i+1

# কোনো Tree-নোডে parent কে আছে সেইটা দেখতে হলে (i//2) করতে হবে।
def parent(i):
    return i//2
'''
# Max_Heap function:
def is_max_heap (H):
    n = len(H) - 1
    for i in range(n, 1, -1):
        p = parent(i)
        if H[p] < H[i]:
            return False
    return True

if __name__ == "__main__":
    H = [None, 19 , 7, 17, 3, 5, 12, 10, 1, 2]
    print(H,"=",is_max_heap(H))
    H = [None, 19, 7 , 17, 3, 5, 12, 10, 1, 4]
    print(H,"=",is_max_heap(H))
    H = [None,1, 2, 3]
    print(H,"=",is_max_heap(H))
    H = [None, 2, 1, 3]
    print(H,"=",is_max_heap(H))
    H = [None, 3, 1, 2]
    print(H,"=",is_max_heap(H))

'''
def max_heapify(heap, heap_size, i):
    l = left(i)
    r = right(i)
    if l<= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and heap[r] > heap[largest]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap,heap_size,largest)

    if largest == i:
        return
    heap[i],heap[largest] = heap[largest],heap[i]

if __name__ == "__main__":
    h = [None, 19, 7, 12, 3, 5, 17, 10, 1, 2]
    print(h)
    max_heapify(h,9,3)
    print(h)
    print()
    h = [None, 1, 2, 3]
    print(h)
    max_heapify(h , 3, 1)
    print(h)






