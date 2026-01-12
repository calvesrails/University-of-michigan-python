# EXERCISE 1 (Tuple indexing)
# Create a tuple with 4 values. Print:
# - the first element
# - the last element (using negative index)
# - a slice with the middle two elements

t = ("a", "b", "c", "d")

print(t[0])
print(t[-1])
print(t[1:3])


# EXERCISE 2 (Tuple unpacking)
# Assign values from a tuple into variables using unpacking.
# Print each variable.

t = (3, 4)
x, y = t

print(x)
print(y)


# EXERCISE 3 (Swap variables with tuples)
# Swap the values of a and b in one line using tuple assignment.

a = 10
b = 20

a, b = b, a

print(a, b)


# EXERCISE 4 (Loop over list of tuples)
# Create a list of tuples (name, score) and print:
# Name: <name> Score: <score> for each tuple.

pairs = [("Ana", 9), ("Caio", 10), ("Joao", 7)]

for name, score in pairs:
    print("Name:", name, "Score:", score)
