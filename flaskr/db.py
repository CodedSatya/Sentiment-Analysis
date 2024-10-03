import pandas as pd

def get_sentiment():
  df = pd.read_csv('E:\Projects\Python\Flask\Sentiment Analysis\data.csv')
  data = df[["name", "description", "contact_number", "email_address", "user_type","remarks" , "created_on", "category", "country"]]
  data.dropna(subset=["remarks"], inplace=True)
  from textblob import TextBlob
  import nltk
  from nltk.sentiment.vader import SentimentIntensityAnalyzer
  nltk.download('vader_lexicon')
  sid = SentimentIntensityAnalyzer()
  score = []
  sentiment = []
  
  for index in data.index:
    row = data.loc[index]
    blob = sid.polarity_scores(row["remarks"])
    score.append((row["name"], blob, row["description"], row["remarks"], row["contact_number"], row["email_address"], row["user_type"],row["created_on"],row["category"],row["country"]))
  
  for i in score:
    # if i[2] == 0:
    #   continue
    # else:
      if i[1]['neg'] == 0:
        sentiment.append((i[0], f"Negative ({i[1]['neg']*10:.2f})", i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
      # elif i[1] == 0:
      #   sentiment.append((i[0], f"Neutral ({i[1]['neg']*10:.2f})", i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
      elif 0 < i[1]['neg'] <= 1:
        sentiment.append((i[0], f"Positive ({i[1]['neg']*10:.2f})", i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
      # sentiment.append((i[0], f"({i[1]['neg']*10:.2f})", i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
  return sentiment
