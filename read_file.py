# Open the file named 'sachin.txt' in read mode ('r')
file = open('sachin.txt', 'r')

# Read the entire content of the file
content = file.read()

# Print the content to the screen
print("File Content:")
print(content)

# Close the file after reading
file.close()
