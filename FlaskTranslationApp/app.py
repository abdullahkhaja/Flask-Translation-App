from flask import Flask, request, render_template, jsonify
from datetime import date
import requests
import random
from dotenv import load_dotenv
import os

load_dotenv('.env.local')
api_key = os.getenv('API_KEY')

BASE_URL = "https://deep-translate1.p.rapidapi.com/language/translate/v2"
LANGUAGE_URL = f"{BASE_URL}/languages"
HEADERS = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "deep-translate1.p.rapidapi.com",
    "Content-Type": "application/json"
}

phrases = {
    "The sun is shining brightly today.": "El sol brilla intensamente hoy.",
    "Coffee is the best way to start the day.": "El café es la mejor manera de empezar el día.",
    "Every day is a new opportunity.": "Cada día es una nueva oportunidad.",
    "I love exploring new places.": "Me encanta explorar nuevos lugares.",
    "Nature is a beautiful escape.": "La naturaleza es una hermosa escapada.",
    # Add more phrases as needed
}

def translate_text(text, target_lang='es', source_lang='en'):
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    
    if response.status_code != 200:
        return None
    
    return response.json()['data']['translations']['translatedText']

app = Flask(__name__)

@app.route('/')
def home():
    current_date = date.today().strftime("%d-%B-%Y")
    return render_template('home.html', date_today=current_date, res='')

@app.route('/phrases', methods=['GET'])
def phrases_page():
    original_phrase = random.choice(list(phrases.keys()))
    translated_phrase = phrases[original_phrase]
    options = random.sample([phrase for phrase in phrases.keys() if phrase != original_phrase], 4)
    options.append(original_phrase)  # Add the correct translation
    random.shuffle(options)  # Shuffle options
    return render_template('phrases.html', translated_phrase=translated_phrase, options=options, correct_answer=original_phrase)

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['sourcetext']
    target_lang = request.form['languages']
    translation_response = translate_text(input_text, target_lang)

    if translation_response:
        res = translation_response
    else:
        res = "Translation failed or API error."

    current_date = date.today().strftime("%d-%B-%Y")
    return render_template('home.html', date_today=current_date, res=res)

@app.route('/random', methods=['GET'])
def random_phrase():
    random_value = random.choice(list(phrases.keys()))
    return jsonify({"phrase": random_value})

if __name__ == '__main__':
    app.run(debug=True)
