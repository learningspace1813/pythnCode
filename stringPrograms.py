#split
text = "I love Python"
words = text.split()
print(words)

#strip
text = " hello World "
words = text.strip()
print(words)

#replace(a, b)
text = "I love bikes"
words = text.replace("bikes","cars")
print(words)

#lower()
text = "I Love Bikes"
words = text.lower()
print(words)

#upper()
text = "I love Bikes"
words = text.upper()
print(words)

#capitalize()
text = "i love cars"
words = text.capitalize()
print(words)

#title()
text = "i love cars!"
words = text.title()
print(words)

#find(x)
text = "I love carx"
words = text.find("x")
print(words)
#----OR----
print(text.find("x"))

#startswith(x)
text = "Hayku-anime is one of my best anime"
words = text.startswith("Hayku")
temp = text.startswith("best")
print(words)
print(temp)

#endwith()
text = "Hayku-anime is one of my best anime"
words = text.endswith("anime")
temp = text.endswith("Hayku")
print(words)
print(temp)

#join(list)
words = ["I","love","bikes"]
sentence = " ".join(words)
print(sentence)

#finding digits from string
text = "abc123xyz"
numbers = "".join(char for char in text if char.isdigit())
print(numbers)

#reverse string (TYPE - 1 - most Pythonic)
text = "KotaK"
reverse = text[::-1]
print(reverse)

#reverse string (TYPE - 1.1 - with user input)
text = input("Enter a string: ")
print("Reversed string: ", text[::-1])

#reverse string (TYPE - 2 - Using loop)
text = "JawaN"
reverse = ""
for char in text:
    reverse = char + reverse
print(reverse)

#reverse string (TYPE - 3 - Reverse + join)
text = "hello world"
reverse = "".join(reversed(text))
print(reverse)

#reverse string (TYPE - 4 - recursion)(For practice, not recommanded in real use)
def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("hello"))

# #reverse string (TYPE - 1.1 - with user input)
# text = input("Enter a string: ")
# print("Reversed string: ", text[::-1])

# #finding digits from string
# text = "abc123xyz"
# numbers = "".join(char for char in text if char.isdigit())
# print(numbers)

