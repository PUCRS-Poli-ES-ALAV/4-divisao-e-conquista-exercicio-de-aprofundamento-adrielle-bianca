import random
import time

# Contador global para iterações
merge_sort_iterations = 0

def merge_sort(arr):
    global merge_sort_iterations
    if len(arr) <= 1:
        return arr

    # Dividir a lista em duas metades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente ordenar as metades
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Mesclar as duas metades ordenadas
    return merge(left_sorted, right_sorted)

def merge(left, right):
    global merge_sort_iterations
    result = []
    i = j = 0

    # Mesclar as duas listas ordenadas
    while i < len(left) and j < len(right):
        merge_sort_iterations += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Adicionar os elementos restantes
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Reiniciar o contador de iterações
def reset_merge_sort_iterations():
    global merge_sort_iterations
    merge_sort_iterations = 0