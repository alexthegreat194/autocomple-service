from prefixtree import PrefixTree
from get_words import read_words

tree = PrefixTree()

print("Reading words...")
words = read_words()
for word in words:
    tree.insert(word)

prefix = ""
while prefix != "exit":
    prefix = input("Enter a prefix: ")
    if prefix == "exit":
        break
    words = sorted(tree.complete(prefix), key=len)
    print(words)
