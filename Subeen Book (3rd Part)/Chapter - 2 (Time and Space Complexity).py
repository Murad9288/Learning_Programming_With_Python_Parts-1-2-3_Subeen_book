# Dharar jogfol sutrer maddhome..
'''n = input()
n = int(n)
result = n * (n+1) / 2
print(result)   # eitar time complexity hobe = O(1)
'''

# Loop use kore Dharar jogfol..
'''n = int(input())
result = 0
for i in range(1,n+1):
     result = result + i
print(result)     #eitar complexity hobe= O(n)'''


# complixity nirnoyer khetre..page number= 20...
'''n = input()
n = int(n)
if n % 2 == 0:
     print(n, "is even number")
else:
     print(n, "is odd number") # eitar speace complexity hobe = O(1)'''

# Nested for loop er bebohar....
'''n = int(input())
count = 0
for i in range(n):
     for j in range(n):
          count += 1
print("n =", n, "count =", count) #eitar Complexity hobe= O(n^2)'''

# Nested-3 for loop er bebohar....
'''n = int(input())
count = 0
for i in range(n):
     for j in range(n):
          for k in range(n):
               count += 1
print("n =",n, "count =", count) #eitar Complexity hobe= O(n^3)'''

# Onushiloni Proshno...
'''n = int(input())
count = 0
for i in range(n):
      count += 1
for i in range(n):
     for j in range(n):
          count += 1
print("n =", n, "count =", count) # eitar complexity hobe = O(n^2)'''
