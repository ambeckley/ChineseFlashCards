from flask import Flask, render_template, redirect, url_for
import random
import json

app = Flask(__name__)

# Load flashcards from the JSON file
with open('hsk_flashcards.json', 'r', encoding='utf-8') as f:
    flashcards = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/level_select')
def level_select():
    # Print available levels and their counts for debugging
    available_levels = {level: len(flashcards[level]) for level in flashcards}
    print("Available levels and their flashcards:", available_levels)  # Debug output
    return render_template('level_select.html', flashcards=flashcards)

@app.route('/flashcard/<level>')
def flashcard(level):
    print(f"Attempting to access flashcard for level: {level}")
    
    if level not in flashcards or not flashcards[level]:
        print(f"Level {level} is not valid or has no flashcards.")
        return redirect(url_for('level_select'))
    
    # Pass the entire list of flashcards for the level
    return render_template('flashcard.html', flashcards=flashcards[level], level=level)


if __name__ == '__main__':
    app.run(debug=True)
