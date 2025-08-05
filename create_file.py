# Open a file named 'sachin.txt' in write mode ('w')
file = open('sachin.txt', 'w')

# Write some content to the file
file.write("Hello, I am Sachin.\n")
file.write("New to Devops and Python.\n")
file.write("Writing first file in pyhthon\n")

# Close the file to save changes
file.close()

print("Content written to sachin.txt successfully.")
