# List er bivinno Methode....
# Append() Methode...
'''
saarc = ["Bangladesh", "India","Sri Lanka","Pakistan","Nepal","Bhutan"]
print("Before List = ",saarc)
saarc.append("Afghanistan")
print("After List = ",saarc)
# sort() methode er kaj...
saarc.sort()
print("Sort Methode = ",saarc)
# reverse() methode er kaj..
saarc.reverse()
print("Reverse Methode = ",saarc)
#Insert() methode.....insert() methode er niyom holo = insert(index,item)...
saarc.insert(0,"America")
print("Insert() methode = ",saarc)
# remove Methode...
saarc.remove("India") # remove korar somoy remove() er vitore jei songkhati likhbo seiti jodi main list na thake tahole seita error dekhabe..
print("Remove methode =",saarc)
# pop methode....
saarc.pop() # eikhane pop() bracket er vitore index akare man dileo seitike deleter kore dibe...
print("pop() methode = ",saarc)
# Extend() methode...
li = [1,2,3,4]
print("1st List = ",li)
li2 = [5,6,7,8]
print("2nd List =",li2)
li.extend(li2)
print("Extend methode = ",li)
# del() function ..
li3 = [1,2,3,4,5,6,7,8,9,6,32,11]
print("List 3 =",li3)
del(li3[10])
print("del() methode = ",li3)
'''
# li =[] faka list theke purno list....
'''
li = []
for i in range(10):
     li.append(i)
print("Faka list a append kora = ",li)
'''
# list er moddhe (+,*) kora..
'''
li1 = [2,3,4]
li2 = [6,7,8]
li = li1 + li2 # eikhane jog korata insert er motoi....
print("List er moddhe jog kora = ",li)
print("li1 = ",li1)
li4 = li1 * 3
print("li1  er moddhe gun = ",li4)
'''
# eikti list a jodi ekadhik string thake tahole oiguloke jokto korar program..
'''
li = ["M","u","r","a","d"]
print(li)
str = "".join(li)
print("li string ke aksathe kora = ",str)
str2 = ",".join(li)
print("li string ke aksathe komar maddhome = ",str2)
str3 = "-".join(li)
print("li string ke aksathe '-' er maddhome  = ",str3)
str4 = "_".join(li)
print("li string ke aksathe '_' er maddhome = ",str4)
'''
# List comprehensions:
'''
li = [1,2,3,4]
new_li =[]
for i in li:
     new_li.append(2*i)
print("Eikhane uporer list ta ke 2 dara gun kora hoye = ",new_li)
'''
# eita ke list comprehensions korle pawa jabe:
'''
li = [1,2,3,4]
new = [2*i for i in li]
print("List comprehensions kore = ",new)
'''
#ekti list a shudhu jor sonkha gulo ber kora...
'''
li = list(map(int,input().split()))
print("Main List =",li)
even = [i for i in li if i % 2 == 0]
print("Main list theke Even songkha nirnoy = ",even)
'''
# Onushiloni list er comprehensions....
'''
li2 = [1,3,4,5,6,7]
li = []
for i in li2:
    li.append(i**2)
print(li)
'''
# eita list comprehensions poddhotir maddhome kora lagbe..
'''
list1 = list(map(int,input().split()))
new_li = [i**2 for i in list1]
print(new_li)
'''
# Tuple korar program..
'''
s = 1,
print("Tuple check = ",type(s))
s1 = ()
print("Tuple check = ",type(s1))
s2 = (1,2,3)
print("Tuple check = ",type(s2))
# tuple er man gulo index akare bare...
print("# tuple er man gulo index akare bare..")
tpl = (1,2,3,4,5,6)
a = tpl[4]
print(a)
b = tpl[0]
print(b)
'''
# amra onek gulo tuple ke unpack kore variable er moddhe upadan gulo rakha jay..
'''
numbers = (12,3,44,45)
print("numbers = (12,3,44,45)")
a,b,c,d = numbers
print("a,b,c,d = numbers")
print("'a' er man =",a)
print("'c' er man =",c)
print("'d' er man =",d)
print("'b' er man =",b)
t = a,b
print(type(t))
'''
# tuple er vitore bivinno jinis rakha jay..and for loop chalo jay..
'''
items = (1,2,3,4,5.5, ["M","u","r","a","d"],("apple","mango","orange"))
for i in items:
     print(i," = ",type(i))

print("#tuple er upadan diye sohojei amra list toiri korte pari..")
tupl = (1,2,3,43,4)
print("Tuple  = ",tupl)
li = list(tupl)
print("Tuple theke list = ",li)
'''
# Set....
'''
items = {"pen","laptop","cellphone"}
print(items)
print(type(items))
li = [1,2,23,3]
tpl = (1,2,3,4)
A = set(li)
print(li,"ke set a rupantor = ",A)
b = set(tpl)
print(b,"ke set a rupantor =",b)
'''
# set er ekta kotha khub joruri.. jeti holo set a thaka upadan gulo dharabahik vabe change naw hote pare...

A = set("Bangladesh")
print(A) # eitir dharabahik chage ta ek ek somoy ek ek ta hoye thake..
# ekti set theke upadan khuje paile seta True hobe.r set oi upadan na thakle False hobe.
B = {1,2,3,4,5}
print(1 in B)
print(6 in B)
