import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the payload dictionary
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the API
    response = requests.post(url, json = myobj, headers = header)
    
    # Return the text attribute of the response
    return response.text