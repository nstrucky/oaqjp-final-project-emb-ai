import requests, json #import the requests library to handle HTTP requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text_to_send = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = text_to_send, headers=headers)

    formatted_response = json.loads(response.text)

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