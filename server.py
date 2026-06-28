""" Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Final Project")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions' scores
        and the dominant emotion
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response['anger']

    if anger is None:
        return "Invalid input! Try again."

    return f"""For the given statement, the system response is 'anger': {response['anger']},
         'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}
          and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.
          """

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
