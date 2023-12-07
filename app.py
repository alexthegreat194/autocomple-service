from prefixtree import PrefixTree
from get_words import read_words
from fastapi import FastAPI
import uvicorn
import tqdm
from dotenv import load_dotenv
import os

load_dotenv()
port = os.getenv("PORT")

tree = PrefixTree()

words = read_words()
for word in tqdm.tqdm(words, desc="Building prefix tree"):
    tree.insert(word)

app = FastAPI()

@app.get('/')
def hello_world():
    return {
        "routes": [
            "/autocomplete/<prefix>",
            "/docs",
            "/openapi.json",
            "/redoc"
        ],
        "message": "Hello, world!"
    }

@app.get('/autocomplete/<prefix>')
def autocomplete(prefix:str, limit: int = 10):
    completions = tree.complete(prefix)
    completions = sorted(completions, key=len)
    if len(completions) > limit:
        completions = completions[:limit]
    return {
        "completions": completions,
        "prefix": prefix,
        "message": "Success"
    }

@app.get('/contains/<word>')
def contains(word: str):
    return {
        "contains": tree.contains(word),
        "word": word,
        "message": "Success"
    }

@app.get('/insert/<word>')
def contains(word: str):
    tree.insert(word)
    return {
        "word": word,
        "message": "Success"
    }

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)