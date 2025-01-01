# Write a program to approve a bank loan to buy a house. The program will ask the 'value of the house',
# the 'salary' of the buyer and in 'how many years' will they pay.

# Calculate the value of the monthly charge, knowing that it can't exceed 30% of the salary.
# Otherwise the loan will be denied.

from time import sleep
print('Hello, Welcome to [YOUR BANK]')
sleep(1)
name = str(input('What is your name? '))
print(f'Hello, {name}')
yn = str(input('This is the tab to negotiate loans. Would you like to proceed? [y/n] '))
if yn == 'y':
    print('OK, processing your data. .')
    sleep(2)
    value = float(input('What is the value of the house? '))
    salary = float(input('Okay. Now I need to know your monthly income, please: R$ '))
    print('Information collected.')
    sleep(2)
    print ('Just a moment. .')
    sleep(2)
    hmyears = int(input('In how many years would you like to pay the loan? '))
    print('OK, processing the data. .')
    sleep(4)
    acharge = value/hmyears
    mcharge = acharge/12
    salary30 = salary*30/100
    if mcharge<=salary30:
        print(f'Congratulations, you loan has been granted, {name}!')
        sleep(2)
        print(f'The monthly charge for your loan will be of: R${mcharge:.2f}')
    elif mcharge>salary30:
        print ('We are sorry to inform you but, unfortunately your current profile does not match with our requirements for this loan.') 
        sleep(3)
        print('But, our team is always updating our intern policies and aiming for the best experience of our customers.')
        sleep(2)
        yn2 = str(input('Therefore if you like, we can notify you when we have an offer for you.\nWould you like to be notified? [y/n] ')).strip()
        if yn2 == 'y':
            print(f'Right, {name}. When an offer turns available you will receive a notification.')
        elif yn == 'n':
            print('Okay, it was a pleasure to have you here.')
            print('Finishing the session. .')
            sleep(2)
    yn3 = str(input(f'May we help you with anything else today, {name}? [y/n] ')).strip()
    if yn3 == 'y':
        print('OK, what would you like to do?')
        print('==='*20)
        sleep(2)
        options = str(input('Type 1 to access the main menu. \nType 2 to exit. ')).strip()
        if options == '1':
            print('Now, choose an option below: ')
            selection = str(input(' 1.Credit Card \n 2.Investments \n 3.Pix\n 4.DotZ \n 5.Exit ')).strip()
            if selection == '1':
                print('Welcome to the credit card tab.')
                sleep(1)
                print('Here you can edit and check your limit.\nCheck and pay your invoice card.\nAmong other things. .')
                str(input(f'What would you like to do today, {name}? ')).strip()
            elif selection == '2':
                print('Hello again, dear Investor.')
                sleep(1)
                print('In what would you like to invest today?')
                sleep(1)
                print('Here we have a plenty of options that match your profile.')
                str(input('Would you like to check them out now? ')).strip()
            elif selection == '3':
                print('Welcome to the Pix interface.')
                print('Here you can instantly, easily and efficiently transfer money to another account.')
                sleep(1)
                str(input('Would you like to make a transfer? ')).strip()
            elif selection == '4':
                print ('Welcome to our fidelity program DotZ')
                print('Here you can check your DotZ, transfer, use and buy new DotZ')
                str(input('What would you like to do? ')).strip()
            elif selection == '5':
                print('OK, finishing the session.')
                sleep(2)
            print('OK, finishing the session.')
            sleep(2)
        elif options == '2':
            print('OK, finishing the session. .')
            sleep(2)
    elif yn3 == 'n':
            print(f'Okay, {name}. Have a good day!')
            print('Finishing the session. .')
elif yn == 'n':
    print('OK, finishing the session. .')
    sleep(2)
# end='' - faz com q a linha do print de baixo grude na de cima?
