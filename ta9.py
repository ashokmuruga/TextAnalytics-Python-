from textblob import TextBlob

sentence = TextBlob('Use 4 spaces per indentation level.')

print(sentence.words)
print(sentence.words[2].singularize())
print(sentence.words[-1].pluralize())
