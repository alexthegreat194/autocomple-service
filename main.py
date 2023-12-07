from prefixtree import PrefixTree
from get_words import read_words
from flask import Flask


tree = PrefixTree()

print("Reading words...")
words = read_words()
for word in words:
    tree.insert(word)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/autocomplete/<prefix>')
def autocomplete(prefix):
    completions = tree.complete(prefix)
    return {
        "completions": completions
    }

@app.route('/words')
def words():
    return {
        "words": tree.strings()
    }

app.run(debug=True)