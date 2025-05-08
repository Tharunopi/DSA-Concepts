# def factorial(n):
#     if n == 1:
#         print(f"return 1")
#         return 1
    
#     print(f"return {n} * factorial({n} -1)")
#     return n * factorial(n -1)

# print(factorial(4))

def forLoop(start, stop):
    if start == stop:
        return 
    
    print(start)

    return forLoop(start+1, stop)

forLoop(1, 5)