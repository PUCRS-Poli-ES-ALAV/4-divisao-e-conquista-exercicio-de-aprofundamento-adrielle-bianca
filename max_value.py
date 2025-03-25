import random
import time

def max_val(arr):
    """Encontra o maior valor em um vetor."""
    max_value = arr[0]
    iteration_count = 0

    for i in range(1, len(arr)):
        iteration_count += 1
        if arr[i] > max_value:
            max_value = arr[i]

    return max_value, iteration_count