def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    # Call the inner function from the outer function
    inner_function()

# Call the outer function
outer_function()
