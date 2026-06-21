# Program 1 (Create a List)

# Create a list
fruits = ["Apple", "Banana", "Mango"]

# Print list
print(fruits)


# Program 2 (Access List Items)

fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])


# Program 3 (Print Favorite Fruit)

fruits = ["Apple", "Banana", "Mango"]

print("My favorite fruite is:", fruits[1])


# Program (Choose Fruit by Index)

fruits = ["Apple", "Banana", "Mango"]

choice = int(input("Enter index number (0, 1, or 2): "))

print("You selected:", fruits[choice])


# Program 5 (Change List Item)

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

# Program 6 (Add Item to List)

fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")

print(fruits)

#  Program 7 (Remove Item from List)

fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.remove("Banana")

print(fruits)


#  Program 8 (Favorite Anime List)

anime = ["Erased", "One Piece", "AOT", "Tokyo Ghoul", "High School DxD"]

print("Original list:", anime)

anime.append("Demon Slayer")
print("After adding an anime:", anime)

anime[2] = "Black Clover"
print("After changing an anime:", anime)

anime.remove("High School DxD")
print("After removing an anime:", anime)
