''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    if (not text_to_analyze):
        return "Please enter text!"
    else:
        # Pass the text to the sentiment_analyzer function and store the response
        response = emotion_detector(text_to_analyze)

        # Extract the label and score from the response
        anger = response['anger']
        disgust = response['disgust']
        joy = response['joy']
        sadness = response['sadness']
        fear = response['fear']
        dominant_emotion = response['dominant_emotion']

        
        if dominant_emotion is None:
            return "Invalid input! Try again."
        else:
            # Return a formatted string with the sentiment label and score
            #return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)
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
    app.run(host="0.0.0.0", port=5000)