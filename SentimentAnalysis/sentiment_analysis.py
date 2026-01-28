import requests
import json

def sentiment_analyzer(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Safely parse JSON
    try:
        formatted_response = response.json()
    except ValueError:
        return {"label": None, "score": None}

    document_sentiment = formatted_response.get("documentSentiment")
    
    # Extracting sentiment label and score from the response
    if response.status_code == 200 and and isinstance(document_sentiment, dict):
        label = document_sentiment.get("label")
        score = document_sentiment.get("score")
        return {"label": label, "score": score}

    elif response.status_code == 500:
        label = None
        score = None

    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}