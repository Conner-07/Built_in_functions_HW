# Generate the group
lower_bound = int(input("Enter the lower limit for the data: "))
upper_bound = int(input("Enter the upper limit for the data: "))
step_size = int(input("Enter the step size (iteration): "))

group = list(range(lower_bound, upper_bound + 1, step_size))

# Calculate mean
mean = sum(group) / len(group)

# Calculate median
sorted_group = sorted(group)
n = len(sorted_group)
if n % 2 == 0:
    median = (sorted_group[n // 2 - 1] + sorted_group[n // 2]) / 2
else:
    median = sorted_group[n // 2]

# Calculate range
data_range = max(group) - min(group)

# Display results
print("Mean:", mean)
print("Median:", median)
print("Range:", data_range)

## break for second part of assignment
# Input string of numbers
numbers_string = "57 73 73 64 26 -108 79 -99 71 26 73 72 26 81 73 79 76 26 -109 69 64 78 65 76 -109 27"

# Split the input string into a list of numbers
numbers_list = numbers_string.split()

# Initialize an empty string to store the decoded message
decoded_message = ''

# Iterate through each number in the list
for num_str in numbers_list:
    num = int(num_str)
    if num >= 0:
        # supposed to handle positive numbers to octal, then to ASCII character however, not functioning properly 
        octal_value = oct(num)[2:]
        decoded_char = chr(int(octal_value, 8))
        decoded_message += decoded_char
    else:
        # For negative numbers this is supposed to handle encoding
        decoded_char = chr(abs(num) - 128)
        decoded_message += decoded_char

# Print the decoded message
print(decoded_message)