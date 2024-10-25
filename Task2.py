"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def find_longest_phone_call():
    phones_and_times = {}
    for call in calls:
        if call[0] in phones_and_times:
            phones_and_times[call[0]] += int(call[3])
        else:
            phones_and_times[call[0]] = int(call[3])

        if call[1] in phones_and_times:
            phones_and_times[call[1]] += int(call[3])
        else:
            phones_and_times[call[1]] = int(call[3])

    max_value = 0
    max_key = ''

    for key, value in phones_and_times.items():
        if value > max_value:
            max_value = value
            max_key = key

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key, max_value))

find_longest_phone_call()
print("\n===============================")
print("Worst-Case Big-O Notation: O(n+m)")
print("n is length of texts")
print("m is length of calls")
