import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print("-----------My example--------------")

word1 = nlp("dog")
word2 = nlp("bone")
word3 = nlp("ball")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# I found it interesting that banana was more similar with monkey than cat, incorporating that monkeys 
# eat bananas and cats don't.
