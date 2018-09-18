from textblob import TextBlob

zen = TextBlob("Beautiful is better than ugly Explicit is better than implicit Simple is better than complex")
print(zen.words)
print(zen.sentences)

for sentence in zen.sentences:
     print(sentence.sentiment)
