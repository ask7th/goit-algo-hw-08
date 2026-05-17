import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from avl import insert
import random

def sum_values(root):
    if root is None:
        return 0

    return root.key + sum_values(root.left) + sum_values(root.right)

root = None
keys = random.sample(range(1000), 10)

print("Keys:", keys)

for key in keys:
    root = insert(root, key)

print("\nAVL tree:")
print(root)
print("Сума всіх значень в AVL-дереві:", sum_values(root))
