''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function handles text input from user
    and analyzes it using emotion detector function
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    joy = response['joy']
    sadness = response['sadness']
    fear = response['fear']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is:<br />\
                Anger : {anger}<br />\
                Disgust: {disgust}<br />\
                Fear : {fear}<br />\
                Joy : {joy}<br />\
                Sadness : {sadness}<br />\
                The dominant emotion is: {dominant_emotion}"

@app.route("/")
def render_index_page():
    """
    Renders the index.html page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
