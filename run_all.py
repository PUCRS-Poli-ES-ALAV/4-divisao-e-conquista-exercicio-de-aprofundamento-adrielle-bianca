import random
import time
from merge_sort import merge_sort, reset_merge_sort_iterations, merge_sort_iterations
from max_value import max_val
from max_value_dc import max_val_dc, reset_max_val_dc_iterations, max_val_dc_iterations
from multi_bits import multiply, reset_multiply_iterations, multiply_iterations

def run_merge_sort(sizes):
    results = []
    for size in sizes:
        arr = [random.randint(0, 1000000) for _ in range(size)]
        reset_merge_sort_iterations()  # Reiniciar o contador
        start_time = time.time()
        merge_sort(arr)
        elapsed_time = time.time() - start_time
        results.append((elapsed_time, merge_sort_iterations))
    return results

def run_max_val(sizes):
    results = []
    for size in sizes:
        arr = [random.randint(0, 1000000) for _ in range(size)]
        start_time = time.time()
        _, iteration_count = max_val(arr)
        elapsed_time = time.time() - start_time
        results.append((elapsed_time, iteration_count))
    return results

def run_max_val_dc(sizes):
    results = []
    for size in sizes:
        arr = [random.randint(0, 1000000) for _ in range(size)]
        reset_max_val_dc_iterations()  # Reiniciar o contador
        start_time = time.time()
        max_val_dc(arr, 0, len(arr) - 1)
        elapsed_time = time.time() - start_time
        results.append((elapsed_time, max_val_dc_iterations))  # Ensure max_val_dc_iterations is imported
    return results

def run_multiply(bit_sizes):
    results = []
    for bits in bit_sizes:
        x = (1 << bits) - 1  # Maior número de n-bits
        y = (1 << bits) - 2  # Segundo maior número de n-bits
        reset_multiply_iterations()  # Reiniciar o contador
        start_time = time.time()
        multiply(x, y, bits)
        elapsed_time = time.time() - start_time
        results.append((elapsed_time, multiply_iterations))
    return results

def main():
    sizes = [32, 2048, 1048576]
    bit_sizes = [4, 16, 64]

    # Executar os algoritmos
    merge_sort_results = run_merge_sort(sizes)
    max_val_results = run_max_val(sizes)
    max_val_dc_results = run_max_val_dc(sizes)
    multiply_results = run_multiply(bit_sizes)

    # Gerar a tabela no arquivo .md
    with open("resultados.md", "w") as file:
        file.write("# Resultados Consolidados\n\n")
        file.write("| Algoritmo         | 32 elementos         | 2048 elementos       | 1.048.576 elementos |\n")
        file.write("|-------------------|----------------------|----------------------|----------------------|\n")
        file.write(f"| Merge Sort        | {merge_sort_results[0][0]:.4f}s, {merge_sort_results[0][1]} iteracoes | {merge_sort_results[1][0]:.4f}s, {merge_sort_results[1][1]} iteracoes | {merge_sort_results[2][0]:.4f}s, {merge_sort_results[2][1]} iteracoes |\n")
        file.write(f"| Max Val           | {max_val_results[0][0]:.4f}s, {max_val_results[0][1]} iteracoes | {max_val_results[1][0]:.4f}s, {max_val_results[1][1]} iteracoes | {max_val_results[2][0]:.4f}s, {max_val_results[2][1]} iteracoes |\n")
        file.write(f"| Max Val DC        | {max_val_dc_results[0][0]:.4f}s, {max_val_dc_results[0][1]} iteracoes | {max_val_dc_results[1][0]:.4f}s, {max_val_dc_results[1][1]} iteracoes | {max_val_dc_results[2][0]:.4f}s, {max_val_dc_results[2][1]} iteracoes |\n")
        file.write("\n\n")
        file.write("| Multiplicao     | 4 bits               | 16 bits              | 64 bits              |\n")
        file.write("|-------------------|----------------------|----------------------|----------------------|\n")
        file.write(f"| Multiply          | {multiply_results[0][0]:.4f}s, {multiply_results[0][1]} iteracoes | {multiply_results[1][0]:.4f}s, {multiply_results[1][1]} iteracoes | {multiply_results[2][0]:.4f}s, {multiply_results[2][1]} iteracoes |\n")

    print("Resultados consolidados gerados no arquivo 'resultados.md'.")

if __name__ == "__main__":
    main()