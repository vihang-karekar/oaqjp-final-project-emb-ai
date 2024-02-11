"""
Main server.py file to handle 'Emotion Detector' requests
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    '''
    Handle emotion_detector for the input textToAnalyze
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    msg = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']}, "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}"
        )
    return msg

@app.route("/")
def render_index_page():
    '''
    Render default index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
