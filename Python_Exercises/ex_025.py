# Create a program that reads the name of a person and tells whether it has
# "Silva" in it.

name = str(input('Tell me your name: ')).strip()
print(f"Does your name have Silva? {('silva' in name.lower())}")
