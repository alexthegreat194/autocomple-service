import os
import re
import json
from tqdm import tqdm

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

    file_size = os.path.getsize('words.json')
    with tqdm(total=file_size, unit='B', unit_scale=True, desc='Reading JSON') as pbar:
        pbar.update(0)
        with open('words.json', 'r') as f:
            words = json.load(f)
        pbar.update(file_size) 
    return words

def main():
    words = get_words()
    for word in words:
        print(word)

if __name__ == "__main__":
    main()
