""" This module analyzes emotion in strings using watson EmotionPredict """

import json
import requests

def emotion_detector(text_to_analyze):
    """ This function takes a text string to analyze and outputs the 
        emotions associated and their scores. Additionally it will 
        determine which emotion is the dominant emotion. The result is returned
        as a dictionary. 
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text_to_send = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = text_to_send, headers=headers)

    formatted_response = json.loads(response.text)

    if response.status_code == 200:

        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dom_v = 0
        dom_e = None

        for k, v in emotions.items():
            if v > dom_v:
                dom_v = v
                dom_e = k

        return {"anger": emotions['anger'], "disgust": emotions['disgust'],
                    "fear": emotions['fear'], "joy": emotions['joy'],
                    "sadness": emotions['sadness'], "dominant_emotion": dom_e}

    elif response.status_code == 400:
        return {"anger": None, "disgust": None,
                    "fear": None, "joy": None,
                    "sadness": None, "dominant_emotion": None}

    else:
        return {"anger": None, "disgust": None,
                    "fear": None, "joy": None,
                    "sadness": None, "dominant_emotion": None}