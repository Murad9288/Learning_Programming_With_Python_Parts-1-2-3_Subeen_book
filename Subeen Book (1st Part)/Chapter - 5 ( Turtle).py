def method_name(a,b):
	print("A Method")
 
class Person:
	def __init__(self, person_name):
		self.name = person_name
	def get_name(self):
 		return self.name

method_name(10, 20)
a_person = Person("Murad Hossain")
b_person = Person("Programmer")

print(a_person.get_name)
print(b_person.get_name)





































# turtle diye borgo...
'''import turtle
turtle.shape("turtle")

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.exitonclick()'''


# somobahu triangle...
'''
import turtle

turtle.shape("turtle")
turtle.speed(10)   #turtle er speed koma and baranor jonno...
for i in range(6):
	turtle.forward(100)
	turtle.left(60)

turtle.exitonclick()


'''
# Selection Sort
'''
def selection_sort(L):
	n = len(L)
	for i in range(0, n-1):
		index_min = 1
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