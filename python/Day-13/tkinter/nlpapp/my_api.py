import nlpcloud

class api:

  def __init__(self):
        self.client = nlpcloud.Client("distilbert-base-uncased-emotion", "0e497b6ca5d6c0e1f6fdef6c0639540a99eced29", gpu=False)
        
    
  def analyze_sent(self, text):
    self.response = self.client.sentiment(
            text,
            target="NLP Cloud"
        )

    all_scores = ''

    for i in self.response['scored_labels']:
      all_scores += f"{i['label']} -> {round(i['score'], 6)}\n"

    final_label = sorted(self.response['scored_labels'], key=lambda x: x['score'], reverse=True)[0]['label']

    all_scores += f'\nThe overall sentiment of the text is {final_label}\n'
    return all_scores