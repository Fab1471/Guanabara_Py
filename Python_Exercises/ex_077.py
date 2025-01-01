# Create a program that has one Tuple with various words (sem acentos).
# After that, you must show, to each word, what are their vowels.

words = ('learn', 'code', 'language', 'python', 
'course', 'free', 'study', 'practice', 'work', 
'market', 'programmmer', 'future')

for w in words:
    print(f'\nin the word "{w.upper()}" we have: ', end=' ')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
