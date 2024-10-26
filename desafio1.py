def isFromFibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return f"O número {num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {num} não pertence à sequência de Fibonacci."

num = int(input("Informe um número: "))
print(isFromFibonacci(num))
