def my_function():
    # Local variables
    a = 1
    b = 2
    c = 3

    # Use locals() to get a dictionary of local variables
    local_vars = locals()

    # Print the local variables
    print("Local variables:", local_vars)

# Call the function
my_function()
