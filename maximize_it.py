from itertools import product
import sys


def main():
    K, M = sys.stdin.readline().strip().split()
    M = int(M)
    K = int(K)

    lists_with_numbers_to_optimize = []
    for i, line in enumerate(sys.stdin.readlines()):
        input_list = [int(number) for number in line.strip().split()][1:]
        lists_with_numbers_to_optimize.append(input_list)
        if i + 1 >= K:
            break

    max_sum = None
    for selected_elements in product(*lists_with_numbers_to_optimize):
        squared_elements = [el ** 2 for el in selected_elements]
        sum_modulo = sum(squared_elements) % M
        if max_sum is None or max_sum < sum_modulo:
            max_sum = sum_modulo

    print(max_sum)


if __name__ == "__main__":
    main()




