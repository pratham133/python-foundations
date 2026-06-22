# Program 1 (Print Numbers)

# Start number
count = 1

# Loop
while count <= 5:
    print(count)
    count += 1


# Program 2 (Countdown)

# Start number
count = 5

# Countdown
while count >= 1:
    print(count)
    count -= 1

print("Times up!")


# Program 3 (User Countdown)

# Get number input
count = int(input("Enter the number: "))

# Countdown
while count >= 1:
    print(count)
    count -= 1

print("Finished!")


# Program 4 (Password Checker)

# Correct password
password = "python123"

# Ask user
user_input = input("Enter the password: ")

# Check password
while user_input != password:
    print("Wrong password")
    user_input = input("Try again: ")

print("Access granted")


# Program 5 (Guess the Number)

# Secret number
secret_number = 69

# Get first guess
guess = int(input("Enter the number: "))

# Keep asking until correct
while guess != secret_number:
    print("Wrong guess")
    guess = int(input("Try again: "))

print("You guessed correctly")
