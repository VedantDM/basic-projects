import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

def get_slot_machine_spin(rows,columns,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.item():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
def deposit():
    while True:
        amount = input('enter amount you would like to deposit: $')
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print('amount must be greater than 0.')
        else:
            print('please enter a valid number.')
    return amount

def get_number_of_lines():
    while True:
        lines = input('enter number of lines to bet on (1-'+str(MAX_LINES)+')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print('please enter a valid number of lines.')
        else:
            print('please enter a valid number.')
    return lines

def get_bet():
    while True:
        amount = input('enter amount you would like to bet on each line: $')
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print(f'amount must be between ${MIN_BET} and ${MAX_BET}.')
        else:
            print('please enter a valid number.')
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet =  bet * lines
        if total_bet>balance:
            print(f'you do not have enough to bet that amount, your current balance is ${balance}.')
        else:
            break
    print(f'you are betting ${bet} on {lines} lines. your total bet is ${total_bet}')

main()