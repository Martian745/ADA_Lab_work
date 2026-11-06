
import random


# Knuth-Morris-Pratt String Matching
def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    n, m = len(haystack), len(needle)

    # Construct LPS (Longest Prefix Suffix) array
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # Search pattern in text
    i = j = 0

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == m:
                return i - j

        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


# Reservoir Sampling
class Randomizer:
    def __init__(self, stream):
        self.stream = iter(stream)
        self.count = 0
        self.selected = None

        for item in self.stream:
            self.count += 1

            # Replace selected item with probability 1/count
            if random.randrange(self.count) == 0:
                self.selected = item

    def getRandom(self) -> int:
        if self.count == 0:
            raise ValueError("Cannot sample from an empty stream.")

        return self.selected


def main():
    print("=== KMP String Matching ===")

    text = input("Enter text: ")
    pattern = input("Enter pattern: ")

    index = strStr(text, pattern)

    print("Pattern Found At Index:", index)

    print("\n=== Randomized Stream Sampling ===")

    stream = list(map(int, input("Enter stream elements: ").split()))

    try:
        sampler = Randomizer(stream)
        print("Randomly Selected Element:", sampler.getRandom())

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
