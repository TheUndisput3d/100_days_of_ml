import nlpcloud

class Sent:
  def analyze_sent(self, text):
    client = nlpcloud.Client("distilbert-base-uncased-emotion", "0e497b6ca5d6c0e1f6fdef6c0639540a99eced29", gpu=False)
    response = client.sentiment(
        text,
        target="NLP Cloud"
    )

    result = sorted(response['scored_labels'], key=lambda x: x['score'], reverse=True)[0]['label']
    return result