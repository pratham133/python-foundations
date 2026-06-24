# Program (Write text to File)

with open ("notes.txt", "w") as file:
    file.write("Hello, this my first file.\n")
    file.write("I am learning Python file handling.\n")

print("Text written successfully.")


# Program 2 (Read Text from File)

with open("notes.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)

# Program 3 (Append Text to File)

with open("notes.txt", "a") as file:
    file.write("This line was added later.\n")

print("Text appended successfully.")

# Program 4 (Read File Line by Line)

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())


# Program 5 (Count Number of Line in File)

line_count = 0

with open("notes.txt", "r") as file:
    for line in file:
        line_count += 1

print(f"Total lines: {line_count}")


# Program 6 (Simple Note Saver)

note = input("Enter a note: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Note saved successfully")


# Program 7 (Note Reader + Line Counter)

with open("notes.txt", "r") as file: 
    lines = file.readlines()

print("Saved notes:")
for line in lines:
    print(line.strip())

print(f"Total notes/lines: {len(lines)}")
