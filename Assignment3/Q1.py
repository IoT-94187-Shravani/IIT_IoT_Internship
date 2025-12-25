text = " Python programming language"

print("Original:", text)
print("Length:", len(text))
print("Strip:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())
print("Replace:", text.replace("Python", "Java"))
print("Find 'programming':", text.find("programming"))
print("Index 'Python':", text.index("Python"))
print("Count 'g':", text.count("g"))
print("Starts with 'Python':", text.startswith("Python"))
print("Ends with 'language':", text.endswith("language"))
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Capitalize:", text.capitalize())
print("Swapcase:", text.swapcase())
print("Is Alphanumeric:", text.isalnum())
print("Is Alphabetic:", text.isalpha())
print("Is Digit:", text.isdigit())
print("Is Lower:", "python".islower())
print("Is Upper:", "PYTHON".isupper())
print("Is Space:", text.isspace())

words = text.split()
print("Split:", words)

joined_text = "-".join(words)
print("Joined:", joined_text)

lines = "Line1\nLine2\nLine3"
print("Split Lines:", lines.splitlines())


name = "Shravani"
age = 20
print("Using format(): My name is {} and I am {} years old".format(name, age))
print(f"Using f-string: My name is {name} and I am {age} years old")