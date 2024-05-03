# Calculate and print the sum of all numbers from 1 to 100

# What do I need?
# Create a variable to track the sum
# Generate the numbers from 1 to 100: range (start, end, step=1)
# for each number in the sequence sum the previuos with the actual
suma = 0
for v in range(1, 101):
    suma += v
print(suma)