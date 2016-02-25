#!/usr/bin/python


def welcomeScreen():
    print("Welcome to the ATM server")
    print("Please enter your ATM card")
 
 
def validatePIN():
    enteredPIN = input("Enter PIN number:")
    while enteredPIN != PIN:
        enteredPIN = input("Enter PIN number:")
 
def commandLoop():
    cmd = getCommand()
    while cmd != 'Q':
        if cmd == 'B':
            bal = balance + amt
            print 'Your current balance is', balance
        elif cmd == 'D':
            amt = getDepositamount()
            balance = balance + amt
            print "Your new balance is", balance
        elif cmd == 'W':
            balance = balance - amt
            print 'Your current balance is', balance
 
def getCommand():
    cmd = raw_input('Enter Command: ')
    allowed = ['B', 'D', 'Q', 'W']
    while cmd not in allowed:
        cmd = raw_input('Enter Command: ')
 
def getDeposit():
    amt = raw_input("Enter deposit amount:")
    return amt
def getWithDrawAmount():
    amt = input("Enter withdraw amount:")
    while amt > balance:
        print "Insuffiecient Funds"
        amt = input("Enter withdraw amount:")
    return amt
def signOut():
    if 'Q':
        print "Thank you for your service, have a nice day"
 
 
#main
PIN = 1234
balance = 1000
 
welcomeScreen()
validatePIN()
commandLoop()
       
if __name__ == '__main__':
    commandLoop()
       
def commandLoop():
    getCommand()
       
def getCommand():
    #Get the command using raw_input, not raw.input
    cmd = raw_input('Enter Command: ')
 
    # To remove all of your conditionals
    allowed = ['B', 'D', 'Q', 'W']
    while cmd not in allowed:
        #Keep asking
       
#In the command loop
 
commands = { 'Q' : signOut,
             'D' : getDeposit,
             'B' : viewBalance,
             'W' : getWithDrawAmount }
 
while cmd not in commands.keys():
    # Keep asking
 
#If they do give the right command, execute the function
commands[cmd]()
       
# your existing code
 
welcomeScreen()
commandLoop()
       
def welcomeScreen():
    print("Welcome to the ATM server")
    print("Please enter your ATM card")
 
def validatePIN(PIN):
    enteredPIN = input("Enter PIN number:")
    while enteredPIN != PIN:
        enteredPIN = input("Enter PIN number:")
 
def commandLoop(balance):
    cmd = getCommand()
    while cmd != 'Q':
        if cmd == 'B':
            #you used the variable bal unnecissarily
            #also you used bal = balance + amt unnecessarily as balance has already changed with Withdraw and Deposit            
            print 'Your current balance is', balance
        elif cmd == 'D':
            #you called getDepositamount() when your function name it getDeposit()
            amt = getDeposit()
            balance = balance + amt
            print "Your new balance is", balance
        elif cmd == 'W':
            #you never called getWithDrawAmount() function
            amt = getWithDrawAmount(balance)
            balance = balance - amt
            print 'Your current balance is', balance
        #your while loop was infinite because you never asked for cmd again
        cmd = getCommand()
    #you never called the signOut function
    signOut()
 
def getCommand():
    cmd = raw_input('Enter Command: ')
    allowed = ['B', 'D', 'Q', 'W']
    while cmd not in allowed:
        cmd = raw_input('Enter Command: ')
    #you never returned cmd back to commandLoop
    return cmd
 
def getDeposit():
    #raw_input makes amt a string, needs to be input
    amt = input("Enter deposit amount:")
    return amt
def getWithDrawAmount(balance):
    amt = input("Enter withdraw amount:")
    while amt > balance:
        print "Insuffiecient Funds"
        amt = input("Enter withdraw amount:")
    return amt
def signOut():
    #you had if 'Q' here which made no sense, if you have signOut in a seperate function and call on exit, it's always true
    print "Thank you for your service, have a nice day"
 
 
#main
PIN = 1234
balance = 1000
 
welcomeScreen()
#you forgot to pass your variables to the functions
validatePIN(PIN)
commandLoop(balance)
