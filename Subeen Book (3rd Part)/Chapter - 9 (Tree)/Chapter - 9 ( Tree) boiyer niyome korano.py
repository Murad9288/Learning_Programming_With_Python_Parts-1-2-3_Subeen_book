# Boiyer niyome...
#এইখানে Bainary Tree টা Recursion দিয়ে করানো হয়েছে ।
# Bainary Tree:
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self,node):
        self.left = node

    def add_right(self,node):
        self.right = node
'''
Example:
          _2_
        /     \
       7       9
      / \       \
     1   6       8
         / \     / \
       5   10  3   4
'''

def create_tree_2():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the root node
    return two
def create_tree_7():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the node
    return seven
def create_tree_1():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the node
    return one
def create_tree_6():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the node
    return six
def create_tree_5():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the node
    return five
def create_tree_10():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the node
    return ten
def create_tree_9():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the node
    return nine
def create_tree_8():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the node
    return eight
def create_tree_3():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the node
    return three
def create_tree_4():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the node
    return four
if __name__ == "__main__":
    root = create_tree_2()
    seven = create_tree_7()
    one = create_tree_1()
    six = create_tree_6()
    five = create_tree_5()
    ten = create_tree_10()
    nine = create_tree_9()
    eight = create_tree_8()
    three = create_tree_3()
    four = create_tree_4()
    # now at print
    print('root =',root)
    print('two left =',seven)
    print('seven left =',one)
    print('seven right =',six)
    print('six left =',five)
    print('six right =',ten)
    print('root(two) right =',nine)
    print('nine right =',eight)
    print('eight left =',three)
    print('eight right =',four)
    
"""
# Amra Bainary tree ta k ek system a korte pari...eita ami amar niyome korechhi....
# Bainary Tree second system:
"""
class Node:
     def __init__(self,root):
          self.root = root
          self.left = None
          self.right = None

     def __repr__(self):
          return repr(self.root)

     def add_left(self,node):
          self.left = node

     def add_right(self,node):
          self.right = node
'''
Example:
          _2_
        /       \
       7         9
      / \         \
     1   6         8
         / \       / \
       5   10   3   4
'''
def create_tree():
     one = Node(1)
     two = Node(2)
     three = Node(3)
     four = Node(4)
     five = Node(5)
     six = Node(6)
     seven = Node(7)
     eight = Node(8)
     nine = Node(9)
     ten = Node(10)
     two.add_left(seven)
     two.add_right(nine)
     seven.add_left(one)
     seven.add_right(six)
     six.add_left(five)
     six.add_right(ten)
     nine.add_right(eight)
     eight.add_left(three)
     eight.add_right(four)
     print("Root =",two)
     print("Root left =",seven)
     print("Seven left =",one)
     print("Seven right =",six)
     print("Six left =",five)
     print("Six right =",ten)
     print("Root right =",nine)
     print("Nine right =",eight)
     print("Eight left =",three)
     print("Eight right =",four)

if __name__ == "__main__":
    create_tree()
"""
# Traversal Tree:
# এইখানে Traversal Tree টা Recursion দিয়ে করানো হয়েছে ।
# Traversal tree - 3 প্রকার:
'''
-যেমনঃ--
১. Pre-order traversal
২. In-order traversal
৩. Post-order traversal
'''
"""
class Node:
     def __init__(self,root):
          self.root = root
          self.left = None
          self.right = None

     def __repr__(self):
          return repr(self.root)

     def add_left(self,node):
          self.left = node

     def add_right(self,node):
          self.right = node
'''
Example:
           _(2)_
         /          \
     (7)         (9)
     /  \             \
   (1) (6)        (8)
         /   \       /   \
      (5) (10) (3) (4)
'''
def create_tree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the root node
    return two

# Pre-order(রুবাডা)  [ এইখানে ‍আমি বুঝার জন্য কিছু বাংলা কথা ‍আমার ভাষায় লিখেছি ।]
# রুবাডা অর্থ:
'''
রু = রুট(root)
বা = বাম(left)
ডা = ডান(right)
'''
def pre_order(node):
    print(node) # node holo = root(রুট)
    if node.left:
        # 1st shortota holo = left(বাম)
        pre_order(node.left)
    if node.right:
        # 2nd shortota holo = right(ডান)
        pre_order(node.right)

# In-order(বারুডা)
# বারুডা অর্থ:
'''
বা = বাম(left)
রু = রুট(root)
ডা = ডান(right)
'''
def in_order(node):
    if node.left:
        # 1st shortota holo = left(বাম)
        in_order(node.left)
    print(node)# node holo = root(রুট)
    if node.right:
        # 2nd shortota holo = right(ডান)
        in_order(node.right)

# Post-order(বাডারু)
# বাডারু অর্থ:
'''
বা = বাম(left)
ডা = ডান(right)
রু = রুট(root)
'''
def post_order(node):
    if node.left:
        # 1st shortota holo = left(বাম)
        post_order(node.left)
    if node.right:
        # 2nd shortota holo = right(ডান)
        post_order(node.right)
    print(node) # node holo = root(রুট)

if __name__ == "__main__":
    root = create_tree()
    print("\nPre-order traversal:")
    pre_order(root)
    print("\nIn-order traversal:")
    in_order(root)
    print("\nPost-order traversal:")
    post_order(root)
"""
# এই প্রোগ্রামটি Traversal Tree দিয়ে করানো হয়েছে ।
class Node:
     def __init__(self,data):
          self.data = data
          self.parent = None
          self.left = None
          self.right = None

     def __repr__(self):
          return repr(self.data)

     def add_left(self,node):
         self.left = node
         if node is not None:
             node.parent = self

     def add_right(self,node):
         self.right = node
         if node is not None:
             node.parent = self
'''
Example:
          _2_
        /       \
       7         9
      / \         \
     1   6         8
         / \       / \
       5   10   3   4
'''
def create_tree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the root node
    return two

def pre_order(node):
    print(node)
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)

def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node)

if __name__ == "__main__":
    root = create_tree()
    print("\nPre-order traversal:")
    pre_order(root)
    print("\nIn-order traversal:")
    in_order(root)
    print("\nPost-order traversal:")
    post_order(root)

