# Project Readme

## Prefix Tree Autocomplete API

This project provides a simple FastAPI-based API for autocomplete functionality using a Prefix Tree (Trie). The API allows users to query for word completions, check if a word is contained in the dataset, and insert new words into the Prefix Tree. FastAPI has automatic interactive documentation and validation for all API endpoints, which can be accessed at [http://localhost:3000/docs](http://localhost:3000/docs) in your browser.

### Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and set the desired port for the FastAPI application:
   ```env
   PORT=3000
   ```

4. Run the application using Uvicorn:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port $PORT --reload
   ```
   or using the python runtime:
   ```bash
   python3 app.py
   ```

5. Access the API at [http://localhost:3000](http://localhost:3000) in your browser.

### API Endpoints

#### 1. Autocomplete

- **Endpoint:** `/autocomplete/<prefix>`
- **Description:** Get word completions for a given prefix.
- **Parameters:**
  - `prefix` (string): The prefix for which autocomplete suggestions are requested.
  - `limit` (optional, int): Limit the number of autocomplete suggestions (default is 10).
- **Example Request:**
  ```http
  GET /autocomplete/hel
  ```
- **Example Response:**
  ```json
  {
    "completions": ["hello", "hell", "helmet", ...],
    "prefix": "hel",
    "message": "Success"
  }
  ```

#### 2. Contains

- **Endpoint:** `/contains/<word>`
- **Description:** Check if a word is contained in the Prefix Tree.
- **Parameters:**
  - `word` (string): The word to check for existence in the dataset.
- **Example Request:**
  ```http
  GET /contains/world
  ```
- **Example Response:**
  ```json
  {
    "contains": true,
    "word": "world",
    "message": "Success"
  }
  ```

#### 3. Insert

- **Endpoint:** `/insert/<word>`
- **Description:** Insert a new word into the Prefix Tree.
- **Parameters:**
  - `word` (string): The word to insert into the dataset.
- **Example Request:**
  ```http
  GET /insert/newword
  ```
- **Example Response:**
  ```json
  {
    "word": "newword",
    "message": "Success"
  }
  ```

### Additional Information

- The Prefix Tree is built from a dataset of words obtained using the `get_words` module.
- The FastAPI application runs on the specified port, and the available routes are `/autocomplete/<prefix>`, `/docs`, `/openapi.json`, and `/redoc`.
- The application can be customized further by modifying the `app.py` file.

Feel free to explore and enhance the functionality of this Prefix Tree Autocomplete API for your specific use case!