# Function er bebohar...
'''def add(n,m): # eikhane n,m holo Parameter...
     return n + m
n = 10
m = 5
result = add(n,m)
print("Function diye jogfol = ",result)
# eikhane amra ekoy variable(parameter) diye bar bar kaj kortechi.. asole def() function a eita sobchaite mojar bishoy...
n = 12
m = 23
result = add(n,m)
print("Function diye jogfol = ",result)
x = 23
y = 3
result = add(x,y) # function call korar somoy add(x,y) eita use kora hoy...eitake Argument bole...
print("Function diye jogfol = ",result)'''

# eibar amra function diye squre rectangle akhbo...
import turtle
def draw_squre(side_length):
     for i in range(4):
          turtle.forward(side_length)
          turtle.left(90)
          
turtle.speed(100)
turtle.color("Blue")

counter = 0
while counter < 90:
     draw_squre(100)
     turtle.right(4)
     counter += 1
# ei codeta amar hothat mone porechilo toh tai korechilam.. eita ei boite nai...tobe important mone hocche codeta...
'''while True:
     n = int(input())
     while n>=0:
          if n % 2 == 0:
               print("Even")
               break
          else:
               print("Odd")
               break'''

# Onushiloni proshno...
# ekti toiri korte hobe , jeti parameter hisebe ekti bahur doirgho nebe and ekti somobahu triangle ongkon korbe.??
'''import turtle
def triangle():
     for a in range(3):
          turtle.forward(100)
          turtle.left(120)

turtle.speed(10)
turtle.color("Red")
print(triangle())'''

# ekhn amra r o function somporke janbo..
'''def myfnc(x):
     print("Inside myfnc", x)
     x = 10 # Function er vitore je variable dewa hoy seti holo Local variable..
     print("Inside myfnc", x)
x = 20  # Function er vitore je variable dewa hoy seti holo Global variable...
myfnc(x)
print(x)'''

# Global variable er ekti function program...
'''def myfnc(y):
     print("y =", y)
     print("x =", x)
x = 20
myfnc(x)'''

# r o onno vabe korano jabe.....
'''def myfnc(y):
     print("y =", y)
     print("x =", x)

x = 20
myfnc(x)
print("y:", y) # y name kono kichu paowa jayna.. eita program a print("y:",y) er jono nameError dekhabe..
'''
# function parameter er difault man kivabe dewa  jay...
'''def myfnc(y=10):
     print("y =", y)
x = 20
myfnc(x)
myfnc()
'''
# abare r ekti program likhbo..
'''def myfnc(x, y=10, z = 0):
     print("x = ", x, "y =", y, "z =", z)

x = 5
y = 6
z = 7
myfnc(x, y, z)'''

#r ekti guttopurno program
'''def myfnc(x,z,y=10):
     print("x =", x, "y =", y, "z =", z)
myfnc(x = 1, y = 2, z = 5)
a = 5
b = 6
myfnc(x = a, z = b)
a = 1
b = 2
c = 3
myfnc(y = a , z = b, x = c)'''

# list er vitore function use kore jog kora..
'''def add_number(number):
     result = 0 
     for num in  number:
          result += num
     return result
result = add_number([1,2,30,4,5,9])
print(result)'''

# list er vitorer element ke change kora index er maddhome function use kore..
'''def test_fnc(li):
     li [0] = 10
my_list = [1,2,3,4,5]
print("Before function call = ",my_list)
test_fnc(my_list)
print("After function call = ", my_list) # eikhane ek er jaygai 10 bosano hoyche..
'''
# ek list theke dui listkei check korar program...
'''list1= [1,2,3,4,5,6,7,8] #eita Interprater a chek kora uchit..
list2 = list1
print(list2)
print(list1)
list2[0] = 100
print(list2)
print(list1)
'''
# Onushiloni proshno = 1..
# ekti function use kore list er vitore average nirnoy korar..
'''def average(n):
     sum1 = sum(n)
     length = len(n)
     result = sum1//length
     return result
n = list(map(int,input().split()))
print(average(n))
'''
# Onushiloni Proshno = 2....
'''def namta(n):
     for i in range(1,11):
          print("%d X %d = %d"%(n,i, (n*i)))
while True:
     n = int(input())
     namta(n)
'''
