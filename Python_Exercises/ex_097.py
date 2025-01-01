# Make a program that contais a Function called
# write(), that receives any text as parameter
# and show a message with adaptable size.

def write(msg):
    size = len(msg) + 4
    print('~'*size)
    print(f'  {msg}')
    print('~'*size)


# Main Program
write('Fabri')
write("I'm gonna be a Senior Python Developer")
write('For that I must and will code and study a lot!')
