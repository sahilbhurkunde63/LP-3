
# Huffman Encoding using Greedy Strategy

import heapq
from collections import Counter

# Create Node class
class Node:
    def __init__(self, char=None, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right


# Generate Huffman Codes
def generate_codes(root, code, codes):

    if root is None:
        return

    # If leaf node is found
    if root.char is not None:
        codes[root.char] = code if code else "0"
        return

    # Left side = 0
    generate_codes(root.left, code + "0", codes)

    # Right side = 1
    generate_codes(root.right, code + "1", codes)


# Huffman Encoding Function
def huffman_encoding(data):

    if not data:
        print("Input string cannot be empty!")
        return

    # Calculate character frequencies
    frequency = Counter(data)

    # Create Min Heap
    heap = []
    counter = 0

    for char, freq in frequency.items():
        node = Node(char)
        heapq.heappush(heap, (freq, counter, node))
        counter += 1

    # Build Huffman Tree
    while len(heap) > 1:

        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)

        new_node = Node(None, left, right)

        heapq.heappush(
            heap, (freq1 + freq2, counter, new_node)
        )
        counter += 1

    # Get Root Node
    root = heap[0][2]

    # Generate Huffman Codes
    codes = {}
    generate_codes(root, "", codes)

    # Display character frequencies and codes
    print("\nCharacter Frequencies and Huffman Codes:")
    for char in sorted(codes):
        print(char, ":", frequency[char], "->", codes[char])

    # Encode the input message
    encoded_text = "".join(codes[char] for char in data)

    print("\nOriginal String:", data)
    print("Encoded String:", encoded_text)

    print("\nOriginal Size:", len(data) * 8, "bits")
    print("Compressed Size:", len(encoded_text), "bits")


# Main Program
text = input("Enter the string: ")

huffman_encoding(text)
