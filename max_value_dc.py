import random
import time

# Contador global para iterações
max_val_dc_iterations = 0

def max_val_dc(arr, init, end):
    """Encontra o maior valor em um vetor usando divisão e conquista."""
    global max_val_dc_iterations

    # Caso base: se o intervalo contém apenas um elemento
    if end - init <= 1:
        max_val_dc_iterations += 1
        return max(arr[init], arr[end])

    # Dividir o intervalo ao meio
    mid = (init + end) // 2

    # Encontrar o maior valor nas duas metades
    v1 = max_val_dc(arr, init, mid)
    v2 = max_val_dc(arr, mid + 1, end)

    # Retornar o maior valor entre as duas metades
    max_val_dc_iterations += 1
    return max(v1, v2)

# Reiniciar o contador de iterações
def reset_max_val_dc_iterations():
    global max_val_dc_iterations
    max_val_dc_iterations = 0