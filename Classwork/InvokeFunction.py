import time

def invoke_after_delay(func, delay):
    print(f"Delaying execution of {func.__name__} by {delay} seconds...")
    time.sleep(delay)
    func()

# Define a function to be invoked after delay
def my_function():
    print("Custom function called after delay")

# Call the custom function after a delay of 3 seconds
invoke_after_delay(my_function, 3)
