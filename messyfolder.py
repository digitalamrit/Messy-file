# Open the notes file for reading
file = open(r"C:\Users\User\Desktop\OneDrive\Python\filehandling\notes.txt", "r")

# Read all lines from the file
lines = file.readlines()

# Open a new file for writing
clean_file = open(r"C:\Users\User\Desktop\OneDrive\Python\filehandling\clean_notes.txt", "w")

# Check each line
for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        clean_file.write(line)

# Close both files
file.close()
clean_file.close()

print("Clean notes file created successfully!")