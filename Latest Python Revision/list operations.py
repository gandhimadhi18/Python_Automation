# ArrayList<String> tools = new ArrayList<>();
tools = ["Aznzddf"]

# Add elements
tools.append("Python")
tools.append("Java")
tools.append("Playwright")

# tools.reverse("0")
tools.append("JSON")

# print elements
print("Tools:", tools)

# print elements length
print("Length:", len(tools))

# print index position
print("First element:", tools[0])

#Reverse list
tools.reverse()
print("Reversed:", tools)

#Extend list
tools.extend(["Naukri", "Selenium"])
print("Extended:", tools)

# Insert element at index 1
tools.insert(1, "Javascript")
print("Inserted:", tools)

#Remove element by value
tools.remove("Java")
print("Removed:", tools)

# Sort list
tools.sort()
print("Sorted:", tools)

# Count occurences
print("Python count:", tools.count("Python"))
tools.pop()
print("Last element popped:", tools)