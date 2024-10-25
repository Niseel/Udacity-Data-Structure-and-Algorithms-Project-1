"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def count_difference_telephone_numbers():
    unique_numbers = set()
    for text in texts:
        unique_numbers.add(text[0])
        unique_numbers.add(text[1])

    for call in calls:
        unique_numbers.add(call[0])
        unique_numbers.add(call[1])

    print("There are {} unique phone number in the records.".format(len(unique_numbers)))

count_difference_telephone_numbers()
print("\n===============================")
print("Worst-Case Big-O Notation: O(n+m)")
print("n is length of texts")
print("m is length of calls")
