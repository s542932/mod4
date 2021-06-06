text = ('i changed this text to something different with more words for the homework '
    'word count example from chapter six out of the textbook')

word_counts = {}

for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        
print(f'{"WORD":<12}COUNT')
 
for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')
     
print('nNumber of Unique words:', len(word_counts))
