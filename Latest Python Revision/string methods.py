name = "Selenium Automation"
tool = "TestNG"
print(len(name))
print(name.upper())
print(name.lower())
print("Boolean value is:", "Automation" in name)
print(name[0:8])

# Rmove surrounding spaces
print(name.strip())
# Join strings
print("Joined strings:",  name + " " + tool)
# Check starting text
print("Starts with:", name.startswith("Selenium"))
# Check ending text
print("End with:",  name.endswith("Automation"))
# Replace characters
print("Replacing characters:",  name.replace("S", "B"))
print("Replacing characters:", name.replace("l","p"))
# Find substring position
print("Substring is:",  name.find("Automation"))
print("split string:", name.split())