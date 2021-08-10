#String diye output a cotationsohokare print kora....
'''s = 'You\'re a Right!'
print(s)
'''
# eivabe kora jay...
'''
s  = "You're a Right"
print(s)
'''
# String er moddhe for loop chalano jay..
'''country = "Bangladesh"
for i in country:
     print(i)
'''
#String er moddeh duiti string ke jog kora...
'''string = "Bangla" + "desh"
print(string)
string2 = "50" + "5"
print(string2)
'''
# Ekti String er vitore bishes ekti string khuje ber kora...
'''
a = "Bangladesh"
print("Main Stirng: ",a)
r = a.find("Ban")
print(r)

r2 = a.find("ang")
print(r2)

r3 = a.find("Bengla")
print("Jehetu ei 'Bengle' ta string a nai.. tai eita -1 return korbe = ",r3)

r4 = a.find("desh")
print(r4)

r5 = a.find("la")
print(r5)
'''
#String er vitore kono kichuke bodle dile Replace() mathode bebohar kora hoy..
'''country = "North Korea"
print("Before String = ",country)
new_country = country.replace("North","South")
print("New String = ",new_country)
'''
# ekta string er vitore ekoy dhoroner word thakle ki hoy dekhi toh...
'''
text = "this is a test. this is another test. this is final test."
print("Before string = ",text)
new_text = text.replace("this","This")
print("New Replace String = ",new_text)
'''
# ekhn amra strip(), lstrip(), rstrip() mathode er bebohar dekhbo..
'''
s = ' \' This is a String.  \'       '
print("Orginal String: ", s)
new = s.lstrip() #eita diye shudhu left diker space guloke baad dibe...
print("New Update Left-Strip(lstrip) String: ",new)
new2 = s.rstrip() #eita diye shudhu Right diker space guloke baad dibe...
print("New Update Right-Strip(rstrip) String: ",new2)
new3 = s.strip() #eita diye dui diker space guloke baad dibe...
print("New Update All-Strip(strip) Sring: ",new3)
'''
#eibar upper(), lower(), capitalize() er bebohar..
'''
s1 = "Bangladesh"
print("Santance ke boro kore dibe = ",s1.upper())
s2 = "BANGLADESH"
print("Santance ke lower kore dibe = ",s2.lower())
s3 = "bangladesh"
print("Shudu Prothom Word ta Capital hobe = ",s3.capitalize())
'''
# split() Mathode bebohar kore list er moto newa hoy santance..
'''
s = "I am a programmmer"
word = s.split()
print(word)
for i in word:
     print(i)
'''
# String er vitorer Stringke (Sub-string) bole... ekhn string er vitore ekti string kotobar ache seiti gonona korbo...
'''
str = "This is"
print("Main String = ",str)
a = str.count("is")
print("Total count string = ",a)
'''
# Ekti string er shurute kingba shese ekti sub-string ache kina seita check korar problem...
'''
s = "Bangladesh"
r = s.startswith("Ban") # ei startswith() mathode diye shurute sub-string ke check korbe..
print("Shurute sub-string thakle output a asbe True: ",r)
r2 = s.endswith("la")
print("Shese jodi sub-string thake tahole output a asbe True: ",r2)
r3 = s.startswith("an")
print(r3)
r4 = s.endswith("desh")
print(r4)
'''
# Startswith() mathode er r o ekta udahoron..
'''
name = "Mr. Murad"
if name.startswith("Mr. "):
     print("Dear Sir")
     
if name.endswith("Murad"):
     print("Miraj")
'''
# ei noyom take turtle diye korano holo.. startswith() mathode er bebohar...
'''
import turtle
name = turtle.textinput("name", "what is your name?")
name = name.lower()
if name.startswith("mr"):
     print("Hello Sir, how are you?")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
     print("Hello Madam, how are you?")
else:
     name = name.capitalize()
     str = "Hi " + name + "! How are you?"
     print(str)
turtle.exitonclick()
'''
#Mojar ekti program..
'''
str = "a quick brown fox jumps over the lazy dog"
for c in "abcdefghijklmnopqrstuvwxyz":
     print(c," = ",str.count(c))
'''
# Onushiloni Proshno = 1....
'''
a = str(input())
b = a[::-1]
if b == a:
     print("Palindrome")
else:
     print("Not Palindrome")
'''
# Onushiloni Proshno = 2....
