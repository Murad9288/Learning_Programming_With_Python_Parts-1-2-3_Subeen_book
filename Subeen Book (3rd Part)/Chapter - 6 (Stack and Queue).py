# Stack 1st system...
'''
 stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() fucntion to pop
# element from stack in 
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are poped:')
print(stack)
 
# uncommenting print(stack.pop())  
# will cause an IndexError 
# as the stack is now empty

'''
# Stack
'''
class My_stack():
    def __init__(self):
        self.data = []
    def my_push(self, x):
        return (self.data.append(x))
    def my_pop(self):
        return (self.data.pop())
    def my_peak(self):
        return (self.data[-1])
    def my_contains(self, x):
        return (self.data.count(x))
    def my_show_all(self):
        return (self.data)

arrStack = My_stack()     
arrStack.my_push(1)
arrStack.my_push(2)
arrStack.my_push(1)
arrStack.my_push(3)
print(arrStack.my_show_all())
arrStack.my_pop()
print(arrStack.my_show_all())
print(arrStack.my_contains(1))
'''
# Stack
# Stack er mul kaj holo = Last in First Out kora
'''
class Stack:

    def __init__(self):
        self.Stack = []
        self.size = 0

    def DataAdd(self, new_data):
        self.Stack.append(new_data)
        self.size += 1

    def outElement(self):
        self.size -= 1
        return self.Stack.pop()

    def isEmptySTack(self):
        if self.size == 0:
            return "Stack is Empty!"
        else:
            return "Stack is Full"

    def print_Stack(self):
        return self.Stack


    def firstData(self):
        return self.Stack[0]


    def LastData(self):
        return self.Stack[-1]
     
     # Reversing korar jonno
    def ReversedStack(self):
        return self.Stack[::-1]

if __name__ == "__main__":
    op = Stack()

    # add data
    op.DataAdd('0. English')
    op.DataAdd("1. Bangla")
    op.DataAdd("2. Math")
    op.DataAdd("3. Islam")
    op.DataAdd("4. Hindi")


    print("Before Stack:", op.print_Stack())
    print("Before Stack Size", op.size)
    print()

    # remove Data
    op.outElement()
    op.outElement() # 2 element remove
    print("After Stack", op.print_Stack())
    print("After Stack Size", op.size)

    # Stack Size
    print(op.size)
    # Reversed Stack
    print("Reversed Stack", op.ReversedStack())

    # Stack First Data
    print("This is Stack First Element", op.firstData())
    print("This is Stack Last Element", op.LastData())

'''
# Second System...
'''
class BBPI:

    def __init__(self, name, roll, id):
        self.Name = name
        self.Roll = roll
        self.Id = id

    def CMT(self):
        return self.Name, self.Roll, self.Id


    def EMT(self):
        return self.Name, self.Roll, self.Id


    def RAT(self):
        pass


class CPI(BBPI):

    def emt(self):
        return self.Name, self.Roll, self.Id




# Driver Code
if _name_ == '_main_':

    op = BBPI("Murad", 165090, 677312838)
    op1 = BBPI("kamal", 214231, 124535221)

    print(op.CMT())
    print(op1.EMT())


    print("CPI")
    o = CPI("a", 121, 11)
    print(o.emt())
'''


# Queue
# First in First..
# Queue diye ekta mojar problem..
'''
queue = []
def Enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(element,"IS ADDED QUEUE ELEMENT.")
def Dequeue():
    if not queue:
        print("QUEUE IS EMPTY.")
    else:
        e = queue.pop(0)
        print("Removed element: ",e)
def display():
    print(queue)

while True:
    print("Select the operation number:\n1.Data_Add.\n2.Data_Remove.\n3.Data_Show.\n4.Quit.")
    ch = int(input("Please select option number: "))
    if ch == 1:
        Enqueue()
    elif ch == 2:
        Dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("The select option number wrong!.")

'''
# Queue Python book..
# Queue holo First in First..
'''
class Queue:
    def __init__(self,size):
        self.items = [0] * size
        self.max_size = size
        self.head, self.tail, self.size = 0,0,0

    def Enqueue(self,item):
        if self.is_full():
            print("Queue is full!")
            return
        print("Inserting", item)
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def Dequeue(self):
        item = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item


    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def is_full(self):
        if self.size == self.max_size:
            return True
        return False

if __name__ == "__main__":
    mu = Queue(3)
    mu.Enqueue("Tahmid")
    mu.Enqueue("Murad")
    mu.Enqueue("Rana")
    mu.Enqueue("Subeen")

    while not mu.is_empty():
        person = mu.Dequeue()
        print(person)

    mu.Enqueue("Subeen")
    mu.Enqueue("Murad")
    print(mu.items)
    print("Head: ",mu.head)
    print("Tail: ",mu.tail)
'''
# Circular Queue

class Circular_Queue:

    def __init__(self, max_SizeQ):
        self.queue = [0] * max_SizeQ

        self.max_size = max_SizeQ
        self.Head = 0
        self.Tail = 0
        self.Size = 0

    def Empty_Data(self):
        return self.Size == 0

    def Full_Data(self):
        return self.Size == self.max_size

    def Enqueue_Data(self,itme):
        if self.Full_Data():
            return "Queue is Full"
        else:

            # Add element to the queue
            self.queue[self.Tail] = itme
            self.Tail = (self.Tail+1) % self.max_size
            self.Size += 1

    def Dequeue_Data(self):
        if self.Empty_Data():
            return "Queue is Empty"
        else:
            # Fethc Data
            data = self.queue[self.Head]
            self.Head = (self.Head+1) % self.max_size
            self.Size -= 1
            return data

if __name__ == "__main__":
    Q_size = 5
    mu = Circular_Queue(Q_size)

    mu.Enqueue_Data("1. MD Murad Hossain")
    mu.Enqueue_Data("2. Md Anis Al Hasan")
    mu.Enqueue_Data("3. MD Hosne Mobarok")
    mu.Enqueue_Data("4. MD Araf")
    mu.Enqueue_Data("5. Md Rana Ali")

    print("Before Queue:")
    for i in mu.queue:
        print(i)

    # Call Dequeue Function
    mu.Dequeue_Data()
    mu.Dequeue_Data()

    print("\nAfter Queue: ")
    while not mu.Empty_Data():
        person = mu.Dequeue_Data()
        print(person)
