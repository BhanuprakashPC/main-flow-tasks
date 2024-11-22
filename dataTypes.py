# Create a list
print()
print('Ccreating list and basic operations')
bhanuList = [10, 20, 30, 40, 50]
print("Original List:", bhanuList)

# Add an element to the list
bhanuList.append(60)
print("List after Adding 60:", bhanuList)

# Remove an element from the list
bhanuList.remove(30)
print("List after Removing 30:", bhanuList)

# Modify an element in the list
bhanuList[2] = 100  # Changing the 3rd element
print("List after Modifying 3rd Element to 100:", bhanuList)
print()

# Create a set
print('Ccreating set and basic operations')
bhanuSet = {10, 20, 30, 40, 50}
print("Original Set:", bhanuSet)

# Add an element to the set
bhanuSet.add(60)
print("Set after Adding 60:", bhanuSet)

# Remove an element from the set
bhanuSet.remove(30)
print("Set after Removing 30:", bhanuSet)

# Create a dictionary
print()
print('Ccreating dictionary and basic operations')
bhanuDictionary = {"name": "Bhanu", "age": 25, "city": "Hyderabad"}
print("Original Dictionary:", bhanuDictionary)

# Add a new key-value pair
bhanuDictionary["profession"] = "Engineer"
print("Dictionary after Adding 'profession':", bhanuDictionary)

# Remove a key-value pair
del bhanuDictionary["age"]
print("Dictionary after Removing 'age':", bhanuDictionary)

# Modify a value in the dictionary
bhanuDictionary["city"] = "Bangalore"
print("Dictionary after Modifying 'city':", bhanuDictionary)