#recursion er bebohar.....
'''
import sys
print("Limit = ",sys.getrecursionlimit())
sys.setrecursionlimit(1500)
count = 0
def My_fucntion():
     global count
     count += 1
     print("My count = ",count)
     My_fucntion()
My_fucntion()
'''
# Recursion diye Fibonacci sonkha nirnoy...
'''
def fibo(n):
     if n in [1,2]:
          return 1
     return fibo(n-2) + fibo(n-1)
def test_fibo():
     assert fibo(1) == 1
     assert fibo(2) == 1
     assert fibo(3) == 2
     assert fibo(4) == 3
     assert fibo(5) == 4
     assert fibo(6) == 5
     assert fibo(7) == 6
     assert fibo(8) == 7
     assert fibo(9) == 8
     test_fibo()
print(test_fibo())
'''
# Onushiloni 1
'''
def print_number(n):
     if n == 0:
          return
     print(n)
     print_number(n-1)
if __name__ == "__main__":
     print_number(5)
'''
# Onushiloni 2:
'''
def Print_number(n):
     if n == 0:
          return
     Print_number(n-1) # eita niche dile sonkhati ulta pashe hoye thake... 
     print(n)
if __name__== "__main__":
     Print_number(5)
'''
def Number(n):
     if n == 0:
          return
     Number(n-1)
     print(n)
Number(10)
