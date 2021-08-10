# Linear Searching
'''
for _ in range(int(input())):
    n = input()
    c = n.lower()
    L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in  range(len(L)):
        if L[i] == c:
            print(i+1)
            break
    else:
        print("Sorry")
'''
# Def Function use kore Linear Searching..
'''
def linear_search(l,x):
     x2 = x.lower()
     n = len(l)
     i =0
     while i < n:
          if l[i] == x2:
               return i+1   # Eikhane i+1 dewar karonta holo index akare ber na howa..
          i += 1
     i = -1
     return i
while True:
     l = L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
     x = input()
     print(linear_search(l,x))
'''
# Binary Searching
'''
def binary_search(L,i):
     left, right = 0, len(L)-1
     while left <= right:
          mid = (left + right)//2     # integer divison
          if L[mid] == i:
               return mid
          if L[mid] < i:
               left = mid + 1
          else:
               right = mid -1
     return -1
if __name__ == "__main__":
     L = [1,2,3,4,5,6,7,8]
     for  i in range(1,11):
          position = binary_search(L,i)
          if position == -1:
               if i in L:
                    print(i, "is in L, But function freturned -1")
               else:
                    print(i, "not in list")
          else:
               if L[position] == i:
                    print(i, "found in correct position.")
               else:
                    print("Binary search returned", position, "for", i,"which is incorrect")
     print("Program terminated")
'''

