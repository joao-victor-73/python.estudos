import math

# 1 - Acessar o numero PI
print(math.pi)
print(f'{math.pi:.2f}')

# 2 - Acessar o numero de Euler
print(math.e)

# 3 - Arredondamento de numeros
num = 10.43
print(math.ceil(num))
print(math.floor(num))

# 4 - Fatorial de um número
num2 = int(input("digite um número: "))
print(math.factorial(num2))

# 5 - Potência de números
print(math.pow(5, 5))

# 6 - Raiz quadrada de um número
print(math.sqrt(169))

# 7 - MDC - Maximo Divisor Comum
mdc = math.gcd(20, 100)
print(mdc)

# 8 - Logaritmo
print(math.log(10))