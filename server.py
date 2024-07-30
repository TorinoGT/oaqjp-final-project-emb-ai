''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    
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
    else:
        
        return "For the given statement, the system response is:<br />\
                    Anger : {}<br />\
                    Disgust: {}<br />\
                    Fear : {}<br />\
                    Joy : {}<br />\
                    Sadness : {}<br />\
                    The dominant emotion is: {}".format(anger,disgust,fear,joy,sadness,dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)