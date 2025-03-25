import time

# Contador global para iterações
multiply_iterations = 0

def multiply(x, y, n):
    global multiply_iterations

    # Caso base
    if n <= 1:
        multiply_iterations += 1
        return x * y

    # Dividir n ao meio
    m = n // 2

    # Dividir os números em partes altas e baixas
    a = x >> m
    b = x & ((1 << m) - 1)
    c = y >> m
    d = y & ((1 << m) - 1)

    # Recursivamente calcular os produtos
    e = multiply(a, c, m)
    f = multiply(b, d, m)
    g = multiply(b, c, m)
    h = multiply(a, d, m)

    # Combinar os resultados
    multiply_iterations += 1
    return (e << (2 * m)) + ((g + h) << m) + f

# Reiniciar o contador de iterações
def reset_multiply_iterations():
    global multiply_iterations
    multiply_iterations = 0