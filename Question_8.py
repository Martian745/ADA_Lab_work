
import heapq
from itertools import count


class Node:
    def __init__(self, char, frequency, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency


class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies):
        if not frequencies:
            raise ValueError("Frequency dictionary cannot be empty.")

        if any(not isinstance(freq, int) or freq <= 0
               for freq in frequencies.values()):
            raise ValueError("Frequencies must be positive integers.")

        # Counter ensures unique heap entries for equal frequencies
        sequence = count()
        min_heap = [
            (freq, next(sequence), Node(char, freq))
            for char, freq in frequencies.items()
        ]

        heapq.heapify(min_heap)

        while len(min_heap) > 1:
            freq1, _, left = heapq.heappop(min_heap)
            freq2, _, right = heapq.heappop(min_heap)

            merged = Node(None, freq1 + freq2, left, right)

            heapq.heappush(
                min_heap,
                (merged.frequency, next(sequence), merged)
            )

        self.root = min_heap[0][2]
        self.codes = {}

        return self.root

    def generate_codes(self):
        if self.root is None:
            raise ValueError("Build the Huffman tree first.")

        self.codes = {}

        def traverse(node, code):
            if node.left is None and node.right is None:
                self.codes[node.char] = code if code else "0"
                return

            if node.left:
                traverse(node.left, code + "0")

            if node.right:
                traverse(node.right, code + "1")

        traverse(self.root, "")
        return self.codes


def main():
    coder = HuffmanCoder()

    n = int(input("Enter number of characters: "))

    if n <= 0:
        print("Number of characters must be positive.")
        return

    frequencies = {}

    print("Enter character and frequency:")
    for _ in range(n):
        char, freq = input().split()

        if len(char) != 1:
            print("Enter only single characters.")
            return

        if char in frequencies:
            print("Duplicate character detected.")
            return

        frequencies[char] = int(freq)

    try:
        coder.build_tree(frequencies)
        codes = coder.generate_codes()

        print("\nHuffman Encoding Table:")
        print("Character\tFrequency\tHuffman Code")

        for char, freq in frequencies.items():
            print(f"{char}\t\t{freq}\t\t{codes[char]}")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
