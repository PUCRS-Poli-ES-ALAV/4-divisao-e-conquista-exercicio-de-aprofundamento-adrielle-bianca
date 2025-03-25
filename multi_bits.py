import time

# Contador global para iterações
iteration_count = 0

def multiply(x, y, n):
    """Multiplicação de inteiros de n-bits usando divisão e conquista."""
    global iteration_count

    # Caso base: se n = 1, retorna o produto diretamente
    if n == 1:
        iteration_count += 1
        return x * y

    # Dividir n ao meio
    m = (n + 1) // 2

    # Dividir os números em partes altas e baixas
    a = x >> m  # Parte alta de x (x // 2^m)
    b = x & ((1 << m) - 1)  # Parte baixa de x (x mod 2^m)
    c = y >> m  # Parte alta de y (y // 2^m)
    d = y & ((1 << m) - 1)  # Parte baixa de y (y mod 2^m)

    # Recursivamente calcular os produtos
    e = multiply(a, c, m)
    f = multiply(b, d, m)
    g = multiply(b, c, m)
    h = multiply(a, d, m)

    # Combinar os resultados
    iteration_count += 1
    return (e << (2 * m)) + ((g + h) << m) + f