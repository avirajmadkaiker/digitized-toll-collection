from flask import Flask, url_for, jsonify, render_template
import speech_recognition as sr

app = Flask(__name__)

@app.route('/reporting')
def reporting():
   image_path = url_for('static', filename='images/personal-voice-assistant-icon.jpg')
   print('Request for reporting page received')
   return render_template('voice.html', image_path=image_path)

@app.route('/reports', methods=['POST'])
def get_reports():
   print('Request for get_reports page received')
   try:
        text = "text report"
        return jsonify({'text': text})
   except sr.RequestError as e:
        return jsonify({'error': f"Could not request results from DB; {e}"})

if __name__ == '__main__':
    app.run(debug=True)