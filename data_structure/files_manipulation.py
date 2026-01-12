fname = "mbox.txt"

try:
    fh = open(fname, "r")
except:
    print("File cannot be opened:", fname)
    quit()

line_count = 0
from_count = 0
subject_count = 0

for line in fh:
    line_count += 1
    line = line.rstrip()  # remove trailing newline

    print(line.upper())

    if line.startswith("From "):
        from_count += 1

        parts = line.split()
        if len(parts) >= 2:
            email = parts[1]
            print("   EMAIL:", email)

    if line.startswith("Subject:"):
        subject_count += 1

fh.close()

print("\n--- SUMMARY ---")
print("Total lines:", line_count)
print("Lines starting with 'From ':", from_count)
print("Lines starting with 'Subject:':", subject_count)




# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


def exercise():

  fname = input("Enter file name: ")
  fh = open(fname)

  count = 0
  total = 0.0

  for line in fh:
      if not line.startswith("X-DSPAM-Confidence:"):
          continue

      value_str = line.split(":")[1].strip()
      value = float(value_str)

      count = count + 1
      total = total + value

  average = total / count
  print("Average spam confidence:", average)
