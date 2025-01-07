#return the factorial of the inputed number
@staticmethod
def factorial(n):
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
    print(resultado)