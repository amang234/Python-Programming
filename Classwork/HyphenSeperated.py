# Accept hyphen-separated sequence of words
words = input("Enter hyphen-separated sequence of words: ")

# Split the input into a list of words
word_list = words.split('-')

# Sort the list alphabetically
sorted_words = sorted(word_list)

# Join the sorted words back into a hyphen-separated string
# sorted_sequence = '-'.join(sorted_words)

# Print the sorted sequence
print("Sorted sequence:", sorted_words)

