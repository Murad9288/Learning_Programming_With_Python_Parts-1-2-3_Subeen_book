def find_fib(n):
    if n <= 2:
        return 1
    x,y = 1,1
    i = 3
    while i <= n:
        i += 1
        x,y = y, x + y
        return y

    
def list_fib(n):
    fib_list = [1,1]
    if n <= 2:
        return fib_list[:n]
    x,y = 1,1
    i = 3
    while i <= n:
        i += 1
        x,y = y, x + y
        fib_list.append(y)
    return fib_list
    
for z in range(1,11):
    print(find_fib(z))

print(list_fib(1))
print(list_fib(2))
print(list_fib(3))

