import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from avl import insert
import random

def find_min(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current.key

root = None
keys = random.sample(range(1000), 10)

print("Keys:", keys)

for key in keys:
    root = insert(root, key)

print("\nAVL tree:")
print(root)
print("Мінімальне значення:", find_min(root))
