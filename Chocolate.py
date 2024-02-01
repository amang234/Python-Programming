# Little Bob loves chocolate, and he goes to a store with Rs. N in his pocket.
# The price of each chocolate is Rs. C. 
#The store offers a discount: for every M wrappers he gives to the store
# he gets one chocolate for free. 
# This offer is available only once. 
# How many chocolates does Bob get to eat?

def chocolates_count():
    N = int(input("Money: "))
    C = int(input("Chocolates: "))
    M = int(input("Wrappers: "))
    chocolates_bought = N // C
    wrappers = chocolates_bought

    while wrappers >= M:
        additional_chocolates = wrappers // M
        chocolates_bought += additional_chocolates
        wrappers = additional_chocolates + (wrappers % M)

    return chocolates_bought

total_chocolates = chocolates_count()
print(f"Bob can eat a total of {total_chocolates} chocolates.")