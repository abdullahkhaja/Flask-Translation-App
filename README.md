# Flask Translation App

This is a simple language translation web application built with **Flask**, allowing users to translate text to various languages using the Deep Translate API. The app also includes an interactive translation quiz to test users' translation skills with pre-defined phrases.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Setup](#api-setup)

## Installation

To run this application, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/flask-translation-app.git
    ```

2. **Navigate into the project directory:**
    ```bash
    cd flask-translation-app
    ```

3. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Create a `.env.local` file in the root directory** and add your Deep Translate API key:
    ```bash
    API_KEY=your_api_key_here
    ```

## Usage

1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **Navigate to `http://127.0.0.1:5000/`** in your web browser to use the translation app.

3. **Features:**
   - **Translate Text:** Input text and select a target language to translate the text.
   - **Phrase Translation Quiz:** Guess the translation of a random phrase and test your skills.

## API Setup

This project uses the **Deep Translate API** to perform translations between various languages. To get started:

1. Sign up at [RapidAPI](https://rapidapi.com/) and get your API key.
2. Add the following line to a `.env.local` file in the root directory of your project:
    ```
    API_KEY=your_api_key_here
    ```

The Deep Translate API is used to translate the input text to the selected target language.

```python
# Load the API key from the environment
api_key = os.getenv('API_KEY')

# API URLs and headers
BASE_URL = "https://deep-translate1.p.rapidapi.com/language/translate/v2"
LANGUAGE_URL = f"{BASE_URL}/languages"
HEADERS = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "deep-translate1.p.rapidapi.com",
    "Content-Type": "application/json"
}
