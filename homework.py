# Roget’s Thesaurus

import requests
link =  "https://www.gutenberg.org/files/22/22-0.txt"

result = requests.get(link)
unique_words = {}
punctuation = ", . ' ? - = ()"
for line in result.text.splitlines():
    for p in punctuation :
        line = line.replace(p, " ")
    words = line.split()
    for word in words:
        word = word.lower()
        unique_words[word] = unique_words.get(word, 0)+ 1

roget_count = len(unique_words)
print(f"Number of unique words in Roget’s Thesaurus:", roget_count)

#Tarzan and the Jewels of Opar
import requests

link = "https://www.gutenberg.org/files/92/92-0.txt"

result = requests.get(link)
#print(result.text)
unique_words = {}
punctuation = ", . ' ? - = ()"
for line in result.text.splitlines():
    for p in punctuation :
        line = line.replace(p, " ")
    words = line.split()
    for word in words:
        word = word.lower()
        unique_words[word] = unique_words.get(word, 0)+ 1

tarzan_count = len(unique_words)
print(f"Number of unique words in Tarzan and the Jewels of Opar:", tarzan_count)


if roget_count < tarzan_count:
    print(f"Roget’s Thesaurus has less unique words than Tarzan and the Jewels of Opar")
else:
    print(f"Roget’s Thesaurus has more or the same unique words than Tarzan and the Jewels of Opar")