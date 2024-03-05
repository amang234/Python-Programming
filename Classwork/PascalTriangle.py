def print_pascals_triangle(n):
    for i in range(n):
        # Calculate the binomial coefficient for each element in the current row
        for j in range(n - i):
            print(" ", end="")
        
        C = 1
        for j in range(i + 1):
            print(" ", C, sep="", end="")
            C = C * (i - j) // (j + 1)
        print()

# Example usage
n = 5
print_pascals_triangle(n)
