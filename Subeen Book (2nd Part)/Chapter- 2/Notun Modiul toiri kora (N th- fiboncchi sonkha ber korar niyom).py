def list_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
        i += 1
        fib_x,  fib_next =  fib_next,fib_x + fib_next
    return fib_next
for x in range(1, 11):
    print(list_fib(x)) 
