import re # import regular expression module
words = [] # Initialize an empty list to store words
word_count = {} # Initialize an empty dictionary to store word counts

# Open the file in read mode
with open("sample.txt","r") as readFile :
    for line in readFile.readlines(): #line is loop variable it present each individual line that is read from the file by readlines() method.
        for word in re.split(r"[ '\n']", line): #split() function removes spaces and here word is a loop variable and after remove all the spaces from line the each words will be assign to word variable
            if word:  # If the word is not empty
             word = word.lower() # Convert the word to lower case
             words.append(word) #after take the each word from lines put it into words list.

# For each word in the words list    
for word in words:
    if word in word_count:  # If the word is already in the word_count dictionary
        word_count[word] += 1  # Increment the count of the word
    else:
        word_count[word] = 1 # If the word is not in the word_count dictionary, add it with a count of 1

# Sort the word_count dictionary by values in descending order and convert it to a list of tuples
sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

# Print the first three items in the sorted_word_count list
for i,(key, value) in enumerate(sorted_word_count):
    if i==3:
        break
    print(f"{key}: {value}")

