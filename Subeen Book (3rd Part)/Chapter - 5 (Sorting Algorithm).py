# Selection Sorting
'''
def selection_sort(L):
	n = len(L)
	for i in range(0, n-1):
		index_min = i
		for j in range(i+1 , n):
			if L[j] < L[index_min]:
				index_min = j
		if index_min != i:
			L[i], L[index_min] = L[index_min], L[i]
if __name__ == "__main__":
	L = [6,1,4,9,2]
	print("Before sort: ",L)
	selection_sort(L)
	print("After sort: ",L)
'''
# Selection Function chara Sorting..
'''
L = list(map(int,input("Main List: ").split()))
N = len(L)
for i in range(0, N-1): # list er '0' number indexta baad diye porer gulo abar index akare dhorbe..
     index_min = i
     for j in range(i+1, N): # eikhane 'i+1' holo i er manta 1 kore barbe..
          if L[j] < L[index_min]:
               index_min = j
     if L[index_min] != i: # ei sortota dewar karon holo ekoy sonkha thakle oita r loop cholbena..
#   (if L[index_min] != i:) ei sortota na dilew hobe..
          L[i], L[index_min] = L[index_min], L[i] # ei line a odol-bodol kora hoyeche. eitake swaping bole...
print("After Selection sort: ", L)
'''
# Selection sort er 3rd number system..

'''
L = list(map(int,input().split()))
empty = []
n = len(L)-1
while n >= 0:
     for i in range(len(L)):
          if L[i] <= L[0]:
               L[0], L[i] = L[i], L[0]
     m = L.pop(0)
     empty.append(m)
     n -= 1
print(empty)
'''
# Bubble Sorting
'''
L = [2,4,1]
n = len(L)
for i in range(0, n):
    for j in range(0, n-i-1):
         if L[j] > L[j+1]:
               L[j], L[j+1] = L[j+1], L[j]
print(L)
'''
# def() function use kore...
'''
def bubble_sort(L):
     n = len(L)
     for i in range(0, n):
          for j in range(0, n-i-1):
               if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    
L = list(map(int,input().split()))               
print("Before sort: ",L)
bubble_sort(L)
print("After Bubble sort: ",L)
'''
# 2nd def() function diye bubble sort...
'''
def bubbleSort(lis):
    length = len(lis)
    for i in range(length):
        for j in range(length - i):
            a = lis[j]
            if a != lis[-1]: # eikhane 'is[-1]' holo list er sheser upadantir mantake bujhay..
                 b = lis[j + 1]
                 if a > b:
                      lis[j] = b
                      lis[j + 1] = a
lis = list(map(int,input().split()))
print("Before sort: ", lis)
bubbleSort(lis)
print("After sort: ", lis)
'''
# 3rd function diye bubble sort...
'''
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
arr = list(map(int,input().split()))
print("Before sort: ", arr)
bubbleSort(arr)
print("After Bubble sort: ",arr)
'''
# Insertion sorting
'''
L = [6,1,4,9,2]
n = len(L)
for i in range(1, n):
     item = L[i]
     j = i - 1
     while j >= 0 and L[j] > item:
          L[j+1] = L[j]
          j = j - 1
          L[j+1] = item
print("After Insertion sort: ",L)
'''
# def() diye Insertion sorting..

def insertion_sort(L):
     n = len(L)
     for i in range(1,n):
          item = L[i]
          j = i - 1
          while j >= 0 and L[j] > item:
               L[j+1] = L[j]
               j = j - 1
               L[j+1] = item
               
L = list(map(int,input().split()))
print("Before list : ",L)
insertion_sort(L)
print("After Insertion sorting: ", L)

