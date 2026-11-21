def reverse(text):
    rev = ""
    for i in range(len(text) -1, -1, -1):
        rev = rev + text[i]
    print("Reversed string:", rev)
reverse("Gandhi")
reverse("Madhi")
reverse("Janaki")