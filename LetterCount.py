# This Python script takes a sentence as input from the user and then asks the user to specify a character (letter) they would like to
# count in that sentence. It then calculates and displays the count of the specified character. 

# sentence input from the user
sentence = input("Please enter a sentence: ")

# specific letter from the user to count
letter = input("Which letter would you like to count in your sentence? ")

# Count the occurrences of the letter in the sentence
count = sentence.count(letter)

# Print the result
print(f"The letter '{letter}' appears {count} times in the sentence you entered.")
 