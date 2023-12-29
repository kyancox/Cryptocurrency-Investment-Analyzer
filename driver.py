from data import core, accelerator
from prices import getPrices
from datetime import datetime

print("\nWelcome to the 'Cryptocurrency Investment Analyzer'.")

# Checks if user input is a valid integer, and converts input from string to integer.  
def read_valid_int(prompt, min, max):

    userInput = input(prompt)
    if userInput.isdigit():
        value = int(userInput)
        if value >= min and value <= max:
            return value
        # For fun
        if value > 1000000:
            print("Please, 1please, please do not invest more than $1,000,000 at a time.")
    # If input is not a digit within min and max, the return message prompts the user to try again.
    return read_valid_int(f"Please enter your choice as an integer between {min} and {max}: ", min, max) 

# Prints prices and allocation along with respective symbols
def showPrices(portfolio):
    print()
    prices = getPrices(portfolio)
    # Header
    print(f"{'Symbol':<8} | {'Current Price':>15} | {'Allocation':>12}")
    print('-'*50)
    for key in portfolio:
        #print(f"{key}: ${prices[key]}, {portfolio[key]}%")
        current_price = round(prices[key], 4)
        allocation = portfolio[key]
        print(f"{key:<8} | ${current_price:>14} | {allocation:>11}%")
    print()

# Calculates how much to invest based on selected portfolio, desired amount to invest, and allocation percentages
def calculateInvestments(portfolio, value):
    print()
    selection = ""
    if portfolio == 1:
        selection = "Core"
        portfolio = core
    elif portfolio == 2:
        selection = "Accelerator"
        portfolio = accelerator

    prices = getPrices(portfolio)

    print(f"Here is how you should invest in the {selection} portfolio:\n")
    '''
    for key in portfolio:
        print(f"Symbol: {key} " + ' ' * (5 - len(key)) + f"| Current Price: {round(prices[key], 4)} | Invest: {portfolio[key] * value} | Allocation: {portfolio[key]}%")
    '''
    # Header
    print(f"{'Symbol':<8} | {'Current Price':>15} | {'Invest':>10} | {'Allocation':>12}")
    print('-' * 60) 
    
    for key in portfolio:
        current_price = round(prices[key], 4)
        invest_amount = round((portfolio[key]/100) * value, 2)
        allocation = portfolio[key]
        print(f"{key:<8} | ${current_price:>14} | ${invest_amount:>9} | {allocation:>11}%")

    print()

def main():
    print("""====================================================
          
1) Show Forbes Core Portfolio (May 2023) & Live Prices
2) Show Forbes Acclerator Portfolio (May 2023) & Live Prices
3) Calculate Investment Analysis
4) Exit
          """)
    
    input = read_valid_int("Choose an option: ", 1, 4)
    print()

    if input == 1: 
        print(f"Showing: Forbes Core Portfolio (May 2023) & Live Prices from {datetime.now()}")
        showPrices(core)
    elif input == 2:
        print(f"Showing: Forbes Acclerator Portfolio (May 2023) & Live Prices from {datetime.now()}")
        showPrices(accelerator)
    elif input == 3:
        print("""Which portfolio would you like to replicate?
1) Core
2) Accelerator\n""")
        portfolio = read_valid_int("", 1, 2)
        print()
        if portfolio == 1:
            print("Selected: Core")
        else:
            print("Selected: Accelerator")

        value = read_valid_int("\nHow much do you want to invest? $", 1, 999999)

        calculateInvestments(portfolio, value)
    elif input == 4:
        print("Goodbye!\n")
        return

    main()

main()