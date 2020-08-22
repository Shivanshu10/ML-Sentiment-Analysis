from textblob import TextBlob
text = input("Please provide a string to perfom sentiment analysis: ")
text = TextBlob(text)
print(text.sentiment)
if text.sentiment[0] > 0:
  print("Postitive Emotion")
elif text.sentiment[0] < 0:
  print("Negative Emotion")
elif text.sentiment[0] == 0.0:
  print("No Emotion")
if text.sentiment[1] > 0.5:
  print("It is a personal belief")
elif text.sentiment[1] <= 0.5:
  print("It is general truth, not a personal belief")
