"""This is a basic ATM Application.

This is a command line application that mimics the actions of an ATM.

Example:
    $ python app.py
"""

accounts = [
    {
    "pin": 123456,
    "balance" : 1436.19},
    {
    "pin" : 246802,
    "balance": 3571.87},
    {
    "pin": 135791,
    "balance" : 543.79},
    {
    "pin" : 123987,
    "balance": 25.89},
    {
    "pin" : 269731,
    "balance": 3258.42}
]


# Create the `login` function for the ATM application.

# As a user of an ATM, I want to enter my pin to authenticate my account so that I can check my balance

def login(pin):
    for account in accounts:
        if int(pin) == account['pin']:
            print(f"The account balance is{account['balance']}.")
        else:
            print(f'There is no account here with that pin: {pin}')
    return account['balance']

account_balance = login(123456)
print(f"${account_balance} !!")
