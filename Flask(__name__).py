from flask import Flask, render_template, request, jsonify
import subprocess
import wolframalpha
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
import datetime
import pyjokes
import time

app = Flask(__name__)

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you today?")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/assistant', methods=['POST'])
def assistant():
    data = request.get_json()
    query = data['query'].lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        return jsonify({"response": results})
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        return jsonify({"response": "Opening YouTube..."})
    # Add more functionality handlers here

if __name__ == '__main__':
    greet()
    app.run(debug=True)
