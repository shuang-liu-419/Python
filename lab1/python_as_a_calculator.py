amount = 1000
years = 3
rate = 5

def value(amount, years, rate):
    # place your mortgage calculator code here
    
    return amount* (1 + rate/100) ** years

final_amount = value(amount, years, rate)
    

## formula: A* (1 + p/100)^n


print("The final amount is " + str(final_amount))
