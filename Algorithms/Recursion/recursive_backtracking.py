def fibo(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibo(n - 1) + fibo(n - 2)

def memorized_fibo(n, memory={}):
    if n in memory:
        return memory[n]
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    memory[n] = memorized_fibo(n - 1, memory) + memorized_fibo(n - 2, memory)
    return memory[n]

print(memorized_fibo(5))