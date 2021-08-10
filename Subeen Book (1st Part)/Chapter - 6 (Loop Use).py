# loop er kaj
'''for i in range(10):
     print("I want to be a great programmer.")

for j in range(100):
     print("I love you Bangladeash")'''

# for loop diye turtle er kaj..
'''import turtle

turtle.shape("turtle")
turtle.speed(2)

for i in range(4):   # for loop use kore squre rectangle..
     turtle.forward(100)
     turtle.left(90)
turtle.exitonclick()'''

# ei program a 100 ta '1' er jogfol nirnoy koreche...
'''result = 0
for _ in range(100):  # ei for loop er vitore amra for i in range(100) eitaw likhte pari...
     result += 1
print(result)'''

# 10 ta songkhar jogfol....
'''result = 0
num = 1
for i in range(10):
     result += num
     num += 1
print("1+2+3+4+5+6+7+8+9+10 = ",result)'''

# ei progreamtike eivabew likha jay..
'''r = 0
for i in range(1,51):
     r  += i # eitake (r = r + i) eivabew likha jay.. tobe sort poddhoti bebohar kora valo...
print(r)'''

# input niye Dharar jogfol...
'''while True:
     n = int(input())
     result = 0
     for i in range(1,n+1):
          result += i
          print(result) # eikhane print(result) dewa karonta holo kivave dharati jog hoyeche seiti dekhar jonno....
     print("1 theke",n,"er jogfol = ",result)'''

# eibar amra ekti list theke boro songkhati dekhbo..
'''num = [1,2,4,7,6,5,88,21,11,22]
max_n = num[0]
for n in num:
     if n > max_n:
          max_n = n
print(max_n)'''

# ei problem take sohoz vabe kora jay...
'''num = [1,2,4,7,6,5,88,21,11,22]
print(max(num))'''


# eibar amra r o ekti udharon dekhbo jeti 1 theke 100 porjonto 5 dara nisshese bivarjo kore oi songkha guloke jog kore print korbo..
'''result = 0
for i in range(101):   # for loop a index akare suru hoy...index er man = 0 theke suru...
     if i % 5 == 0:
          print(i)
          result = result + i
print("Sum is:",result)'''

# ei program tike sohoze kora jay eivabe...
'''r = 0
for i in range(5, 101, 5):
     print(i)
     r = r +  i
print(r)'''

# Turtle diye (--) dash line akghbo...
'''import turtle

turtle.speed(1)
for i in range(20):
     turtle.forward(20)
     turtle.penup()
     turtle.forward(5)
     turtle.pendown()

turtle.exitonclick()'''

# turtle diye rectangle er side length briddhi.....
'''import turtle
turtle.shape("turtle")
turtle.speed(1)

for side_length in range(50,100,10):
     for i in range(4):
          turtle.forward(side_length)
          turtle.left(90)
turtle.exitonclick()'''

# list er moddhe for loop..
'''sarrc = ["Bangladesh", "Afghanistan","Bhutan","Nepal","Pakistan","Sri Lanka"]
for i in sarrc:
     print(i,"is a Member of SAARC.")'''

#amar chaile list() function er vitore reange() bebohar korte pari..
'''li = list(range(21))
print(li)
'''

# while loop er bebohar..
'''i = 0
while i < 5:
     print(i)
     i += 1'''

# while diye ulot pashe..
'''i = 10
while i >= 0:
     i -= 1
     print(i+1) #eikhane i+1 dewar koron holo 10 thekei print korbe output a..'''

# while loop bebohar kore Namta nirnoy kora..
'''while True:
     n = int(input("Please enter a positive integer: "))
     count = 0
     while count < 10:
          count += 1
          print(n, "X", count, " =", n*count)'''
# while loop and for loop  er vitore turtle...
'''import turtle
turtle.color("orange") #eikhane color change kora jabe..
turtle.speed(6)
c = 0
while c < 4: #eit holo koto bar rectangle cholebe...
     for i in range(4): # eita bahur songkha nirdesh kore..
          turtle.forward(100)
          turtle.right(90)
     turtle.left(40)
     c += 1
turtle.exitonclick()'''

# ektu different vabe while loop and for loop er vitore turtle .....

'''import turtle
turtle.color("Yellow") #eikhane color change kora jabe..
turtle.speed(6)
c = 0
while c < 4:
     for i in range(4):
          turtle.forward(100)
          turtle.right(90)
     turtle.left(4)
     c += 1
turtle.exitonclick()'''

# dot() Function bebohar kora chhok aka...
'''import turtle
height = 5
width = 5

turtle.speed(5)
turtle.penup()

for y in range(height):
     for x in range(width):
          turtle.dot(20) #eikhane dot() er vitore songkha dile dot boro choto korano jay...
          turtle.forward(50)
     turtle.backward(50 * width)
     turtle.right(90)
     turtle.forward(40)
     turtle.left(90)
turtle.exitonclick()
'''
# break and continue er kaj
'''while True:
     n = int(input("Please enter a number (0 to exit): "))
     if n == 0:
          break
     print("Squre of", n, "is", n*n)'''

# break and continue er kaj 2.....
'''while True:
     n = int(input("Please enter the positive number (0 to exit): "))
     if n < 0:
          print("We only allow positive number. Please try again.")
          continue
     if n == 0:
          break
     print("Squre of", n, "is", n*n)'''

# onnovabew kora jay oi program ti...
'''while True:
     n = int(input())
     if n <= 0:
          print("We only allow positive number and to start 1.Pleasee try again..")
          continue
     print("Squre of",n, "is", n*n)
'''
# break and continue er r o ekti program...
'''terminate = False
while not terminate:
     num1 = int(input("Please enter a number: "))
     num2 = int(input("Please enter another number: "))
     while True:
          operation =  input("Please enter add/sub or quit to exit: ")
          if operation == "quit":
               terminate = True
               break
          if operation not in ["add", "sub"]:
               print("Unknown operation!")
               continue
          if operation == "add":
               print("Result is" , num1 + num2)
               break
          if operation == "sub":
               print("Result is", num1 - num2)
               break'''
# ei code tike amar vasay korano hoyeche...
'''
t = False
while not t:
    
    while True:
        n = int(input())
        m = int(input())
        o = input("Please enter add/sub or quit to exit: ")
        if o == "quit":
            t = True
            break
        if o not in ["add","sub"]:
            print("Unknown operation!")
            continue
        if o == "add":
            print("Result is", n + m)
            break
        if o == "sub":
            print("Result is", n-m)
            break
'''
