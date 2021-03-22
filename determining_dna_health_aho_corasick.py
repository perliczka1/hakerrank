#!/bin/python3

from __future__ import annotations

import math
import queue
from bisect import bisect_left
from typing import List, Dict


## Trie implementation

class Node:
    def __init__(self) -> None:
        self.children: Dict[str, Node] = {}
        self.failure_node: Node = None
        self.dictionary_node: Node = None
        self.positions: List[int] = []
        self.values: List[int] = []

    def update_values(self, position: int, value: int) -> None:
        self.positions.append(position)
        self.values.append(value)

    def get_child(self, letter: str, insert_missing: bool = False):
        try:
            return self.children[letter]
        except KeyError:
            if insert_missing:
                new_node = Node()
                self.children[letter] = new_node
                return new_node
            else:
                return None

    def get_value(self, position_from: int, position_to: int) -> int:
        first_ind = max(0, bisect_left(self.positions, position_from))
        last_ind = bisect_left(self.positions, position_to + 1)
        return sum(self.values[first_ind:last_ind])


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, sequence: str, position: int, value: int) -> None:
        current_node = self.root
        for ch in sequence:
            current_node = current_node.get_child(ch, True)
        current_node.update_values(position, value)

    def add_failure_edge(self, ch: str, node: Node, parent_node: Node):
        if node is self.root:
            node.failure_node = self.root
            return
        current_search_node = parent_node.failure_node
        while True:
            failure_node_candidate = current_search_node.get_child(ch, False)
            if failure_node_candidate is node:
                node.failure_node = self.root
                return
            if failure_node_candidate is not None:
                node.failure_node = failure_node_candidate
                if len(node.failure_node.values) > 0:
                    node.dictionary_node = node.failure_node
                else:
                    node.dictionary_node = node.failure_node.dictionary_node
                return
            if current_search_node is self.root:
                node.failure_node = self.root
                return
            current_search_node = current_search_node.failure_node

    def add_failure_edges(self):
        bfs_queue = queue.Queue()
        bfs_queue.put(('', self.root, None))
        while not bfs_queue.empty():
            ch, node, parent_node = bfs_queue.get()
            self.add_failure_edge(ch, node, parent_node)
            for ch, child in node.children.items():
                bfs_queue.put((ch, child, node))

    def add_dictionary_edges_from_node(self, node: Node):
        if len(node.failure_node.values) > 0:
            node.dictionary_node = node.failure_node
        for child in node.children.values():
            self.add_dictionary_edges_from_node(child)

    def add_dictionary_edges(self):
        self.add_dictionary_edges_from_node(self.root)

    def value_from_node(self, node: Node, position_from: int, position_to: int):
        global found
        added_value = 0
        while node is not None:
            added_value += node.get_value(position_from, position_to)
            node = node.dictionary_node
        return added_value

    def match(self, input: str, position_from: int, position_to: int) -> int:
        current_sum = 0
        current_node = self.root
        letter_index = 0
        while letter_index < len(input):
            ch = input[letter_index]
            while True:
                current_node_candidate = current_node.get_child(ch, False)
                if current_node_candidate is not None:
                    current_node = current_node_candidate
                    added_value = self.value_from_node(current_node, position_from, position_to)
                    current_sum += added_value
                    letter_index += 1
                    break
                elif current_node is not self.root:
                    current_node = current_node.failure_node
                else:
                    letter_index += 1
                    break
        return current_sum


def main():
    n = int(input())

    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    trie = Trie()
    for pos, gene in enumerate(genes):
        trie.insert(gene, pos, health[pos])

    trie.add_failure_edges()

    max_health = 0
    min_health = math.inf

    s = int(input())
    results_dict = {}
    for s_itr in range(s):
        firstLastd = input().split()
        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]
        current_health = trie.match(d, first, last)
        max_health = max(current_health, max_health)
        min_health = min(current_health, min_health)
        results_dict[current_health] = d

    print(min_health, max_health, sep=" ")


if __name__ == '__main__':
    main()
