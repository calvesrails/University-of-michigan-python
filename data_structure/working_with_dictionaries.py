# 9.4
# Write a program to read through the mbox-short.txt and figure out who
# has sent the greatest number of mail messages. The program looks for
# 'From ' lines and takes the second word of those lines as the person
# who sent the mail. The program creates a Python dictionary that maps
# the sender's mail address to a count of the number of times they appear
# in the file. After the dictionary is produced, the program reads through
# the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.rstrip()
    wds = line.split()

    # Guardian to avoid IndexError and skip non-From lines
    if len(wds) < 1 or wds[0] != 'From':
        continue

    email = wds[1]
    counts[email] = counts.get(email, 0) + 1

bigcount = None
bigword = None

for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = email

print(bigword, bigcount)


# EXERCISE 1 (items) - Print sender and count
# Read the file and build a dictionary of email counts for lines that start with "From".
# Then print each email and its count using dict.items().

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    wds = line.split()
    if len(wds) < 2 or wds[0] != "From":
        continue
    email = wds[1]
    counts[email] = counts.get(email, 0) + 1

for email, count in counts.items():
    print(email, count)



# EXERCISE 2 (values) - Sum all counts
# Build the email count dictionary and compute the total number of "From" messages
# using dict.values() (sum the values manually, without sum()).

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    wds = line.split()
    if len(wds) < 2 or wds[0] != "From":
        continue
    email = wds[1]
    counts[email] = counts.get(email, 0) + 1

total = 0
for v in counts.values():
    total = total + v

print("Total From messages:", total)



# EXERCISE 3 (keys) - Count how many unique senders
# Build the dictionary and print how many unique email addresses exist
# using len(dict.keys()).

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    wds = line.split()
    if len(wds) < 2 or wds[0] != "From":
        continue
    email = wds[1]
    counts[email] = counts.get(email, 0) + 1

print("Unique senders:", len(counts.keys()))
