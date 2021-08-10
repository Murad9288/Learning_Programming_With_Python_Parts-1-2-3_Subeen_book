# Code Test korar Program...
# Average Nirnoy korar Program..
'''def average(L):
     if not L:
          return None
     return sum(L) / len(L)
if __name__ == "__main__":
     L = [1,2,3,4,5]
     print(average(L))'''

# Programtike amra vinno vabe check korte pari ...Ei programtike amra vitoreo likhte pari..
'''def average(L):
     return sum(L) / len(L)
if __name__ == "__main__":
     L = [1,2,3,4,5]
     expected_result = 3.0
     result = average(L)
     if expected_result == result:
          print("test passed")
     else:
          print("test failed!", "received:", result,"expected:", expected_result)'''

# Ei code ta ami nije korchi....Others Poddhotite....
'''def average(n):
     result = sum(n) // len(n)
     return result
if __name__ == "__main__":
     n = list(map(int,input().split()))
     print(average(n))'''

# Assert er bebohar...
# Assert Error Check kora..Ei assert check kora hoy muloto interpreter file a...
'''assert 2 == 3
assert 2 == 2 #Assert Error chcek kora.. eita run korle output er shese dekhabe AssertionError...
s = '123'
assert s == 123
assert s == '123' #eita run korle output er shese dekhabe AssertionError...
assert 3 > 2, "of course 3 is greater than 2" # Assert ti te Argument o jog kora jay...
assert 3 < 2, "how can 3 be less than 2 ?"
'''
'''# eibar amra Assert bebohar kore average functionti check kori...
if __name__ == "__main__":
     L = [1,2,3,4,5]
     expected_result = 3.0
     assert expected_result == average(L), "Average() Produced incorrect result"
'''
# Unit Testing..
def average(L):
     if not L:
          return None
     return sum(L) / len(L)
def test_average():
     assert 3.0 == average([1,2,3,4,5])
