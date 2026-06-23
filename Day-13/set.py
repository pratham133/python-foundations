#  Program 1 (Create a Set)

fruits = {"Apple", "Banana", "Mango"}

print(fruits)


# Program 2 (Set Removes Duplicates)

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)


# Program 3 (Add value to Set)

fruits = {"Apple", "Banana", "Mango"}

fruits.add("Orange")

print(fruits)


# Program 4 (Remmove Value from Set)

fruits = {"Apple", "Banana", "Orange","Mango"}

fruits.remove("Banana")

print(fruits)


# Program 5 (Check value in Set)
# check whether a value is present in a set using "in".

anime = {"JJK", "AOT", "Demon Slayer"}

print(f"AOT in anime: {'AOT' in anime}") 
print(f"DxD in anime: {'DxD' in anime}")


# Program 6 (List vs Tuple vs Set)

fruits_list = ["Apple", "Banana", "Orange", "Banana", "Mango"]
fruits_tuple = ("Apple", "Banana", "Orange", "Banana", "Mango")
fruits_set = {"Apple", "Banana", "Orange", "Banana", "Mango"}

print(f"List: {fruits_list}")
print(f"Tuple: {fruits_tuple}")
print(f"Set: {fruits_set}")


# Program 7 (Set Practice)

anime = {"AOT", "High School DxD", "JJK", "Naruto", "Bleach", "Black Clover"}

print(f"Original set: {anime}")

anime.add("One Piece")
print(f"After adding One Piece: {anime}")

anime.remove("High School DxD")
print(f"After removing High School DxD: {anime}")

print(f"Is One Piece in set? {'One Piece' in anime}")
print(f"Is Hell Paradise in set? {'Hell Paradise' in anime}")

