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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_phone_type(number):
    start_index = number.find('(')
    end_index = number.find(')')

    if start_index != -1 and end_index != -1 and number[1] == '0':
        return number[start_index:end_index + 1]

    elif number.find(' ') and (number.startswith('7') or number.startswith('8') or number.startswith('9')):
        return number[:4]

    elif number.startswith('140'):
        return '140'

    else:
        return 'undefined'


def get_list_phone_number():
    list_number = []
    for call in calls:
        if '(080)' in call[0]:
            list_number.append(get_phone_type(call[1]))
    return list_number

def part_a():
    print("The numbers called by people in Bangalore have codes:")
    code_list = set()
    for code in get_list_phone_number():
        code_list.add(code)

    for dial in sorted(code_list):
        print(dial)

def part_b():
    list_number = get_list_phone_number()
    count = 0
    for number in list_number:
        if number == '(080)':
            count += 1

    percent = (count / len(list_number)) * 100
    print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))


part_a()
print("\n===============================")
part_b()
print("\n===============================")
print("Part A: Worst-Case Big-O Notation: O(n + m + o Log o)")
print("n is length of calls")
print("m is length of list number called form Bangalore")
print("0 is sort records in set (n>m>o)")

print("\n===============================")
print("Part B: Worst-Case Big-O Notation: O(n+m)")
print("n is length of calls")
print("m is length of list number called from Bangalore (n > m)")

