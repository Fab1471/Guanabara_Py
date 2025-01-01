# Create a program that reads a phrase though the keyboard and shows: 

# How many times appears the letter "A"
# In which position it appears at the first time. .
# In which position it appers in the last time. .

phrase = str(input('type a phrase: ')).lower().strip()
print(f"The letter A appears {phrase.count('a')} times in the sentence.")
print(f"The letter A appears at the first time at the position {phrase.find('a')+1}.")
print(f"The letter A appears in the last time at the position {phrase.rfind('a')+1}.")
