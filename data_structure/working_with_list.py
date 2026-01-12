han = open('mbox-short.txt')

for line in han:
  line = line.rstrip()
  wds = line.split()
  # print("line: ", line )

  # guardian
  # if len(wds) < 1:
  #   continue

  if len(wds) < 1 or wds[0] != 'From' :
    # print('ignore')
    continue
  print(wds[2])



# EXERCISE A (Email)
# Write a program that reads through the file and prints the email address
# (the second word) on each line that starts with "From".
# Example line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

han = open('mbox-short.txt')

for line in han:
  line = line.rstrip()
  wds = line.split()

  if len(wds) < 1 or wds[0] != 'From':
    continue

  print(wds[1])


# EXERCISE B (Count "From" lines)
# Write a program that reads through the file and counts how many lines
# start with "From". Print the final count.

han = open('mbox-short.txt')

count = 0

for line in han:
  line = line.rstrip()
  wds = line.split()

  if len(wds) < 1 or wds[0] != 'From':
    continue

  count = count + 1

print("From lines:", count)


# EXERCISE C (Print hour)
# Write a program that reads through the file and prints the hour (HH)
# from the time field on each line that starts with "From".
# Example time field: "09:14:16" -> hour is "09"

han = open('mbox-short.txt')

for line in han:
  line = line.rstrip()
  wds = line.split()

  if len(wds) < 1 or wds[0] != 'From':
    continue

  time = wds[5]
  hour = time.split(':')[0]
  print(hour)
