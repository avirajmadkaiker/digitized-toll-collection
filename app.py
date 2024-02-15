from flask import Flask, url_for, jsonify, render_template
import speech_recognition as sr

app = Flask(__name__)

@app.route('/reporting')
def index():
   image_path = url_for('static', filename='images/personal-voice-assistant-icon.jpg')
   print('Request for main page received')
   return render_template('voice.html', image_path=image_path)

@app.route('/speech_to_text', methods=['POST'])
def speech_to_text():
    try:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)

        return jsonify({'text': text})

    except sr.UnknownValueError:
        return jsonify({'error': 'Speech recognition could not understand audio.'})
    except sr.RequestError as e:
        return jsonify({'error': f"Could not request results from Google Web Speech API; {e}"})

if __name__ == '__main__':
    app.run(debug=True)