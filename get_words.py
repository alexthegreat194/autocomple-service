import os
import re
import json

dir = "/usr/share/dict/words"

def get_words():
    with open(dir, 'r') as f:
        words = f.read().splitlines()
    with open('words.json', 'w') as f:
        json.dump(words, f) 
    return words

def read_words():
    print("Reading words...")
    if not os.path.exists('words.json'):
        print("\"words.json\" does not exist. Reading words off of OS...")
        get_words()  

    with open('words.json', 'r') as f:
        words = json.load(f)
    return words

def main():
    words = get_words()
    for word in words:
        print(word)

if __name__ == "__main__":
    main()
