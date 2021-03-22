#!/bin/python3

import math
from collections import defaultdict
from bisect import bisect_left

def main():
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))
    genes_pos = defaultdict(list)
    genes_health = defaultdict(list)
    genes_health_cumulative = {}
    prefixes = set()

    for pos, gene in enumerate(genes):
        genes_pos[gene].append(pos)
        genes_health[gene].append(health[pos])
        for j in range(1, min(len(gene), 500)+1):
            prefixes.add(gene[:j])

    for gene, health in genes_health.items():
        genes_health_cumulative[gene] = [0]
        genes_health_cumulative[gene] += [sum(health[:i]) for i in range(1, 1+len(health))]

    possible_lengths = {len(gene) for gene in genes}

    max_health = 0
    min_health = math.inf
    s = int(input())
    for s_itr in range(s):
        firstLastd = input().split()
        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]
        d_len = len(d)
        current_health = 0

        for start_index in range(d_len):
            for gene_length in possible_lengths:
                if start_index + gene_length > d_len:
                    break
                subsequence = d[start_index:start_index + gene_length]
                if subsequence not in prefixes:
                    break
                matching_genes_pos = genes_pos.get(subsequence)

                if matching_genes_pos:
                    first_gene_ind = max(0, bisect_left(matching_genes_pos, first))
                    last_gene_ind = bisect_left(matching_genes_pos, last+1)
                    matching_genes_health_cumulative = genes_health_cumulative.get(subsequence)
                    current_health += matching_genes_health_cumulative[last_gene_ind] - matching_genes_health_cumulative[first_gene_ind]

        max_health = max(current_health, max_health)
        min_health = min(current_health, min_health)

    print(min_health, max_health, sep=" ")


if __name__ == '__main__':
    main()