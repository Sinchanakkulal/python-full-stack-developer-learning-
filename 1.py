"""coments sthat are used for multi line  comments"""
# This is a single line comment

#concatenation in python
first_name="sinchana"
last_name="kulal"
full_name=first_name+" "+last_name
print(full_name)

#printing the message as time as required ,that can be one with * symbal
message="This is a warning! "*2
print(message)

#string methods
print(message.upper())
print(message.lower())
print(message.title())
print(message.strip())  # removes leading and trailing spaces
print(message.replace("warning","error")) #it replace the warning into error

print(message.count("is"))
print(message.encode("utf-8"))  # encodes the string to bytes using utf-8 encoding
print(message.endswith("!"))  # checks if the string ends with "!",here it ends with space
print(message.format("warning", "error"))  # formats the string with placeholders


text = "hello world"
num_text = "12345"
alpha_text = "Python"
mixed_text = "Hello123"
space_text = "    "
tab_text = "H\te\tl\tl\to"

# 1. capitalize()
print(text.capitalize())   # Hello world

# 2. casefold()
print("PYTHON".casefold()) # python

# 3. center()
print(text.center(20, "-"))  # ----hello world-----

# 4. count()
print(text.count("l"))  # 3

# 5. encode()
print(text.encode())  # b'hello world'

# 6. endswith()
print(text.endswith("world"))  # True

# 7. expandtabs()
print(tab_text.expandtabs(4))  # H   e   l   l   o

# 8. find()
print(text.find("world"))  # 6

# 9. format()
print("My name is {} and I love {}".format("Sinchana", "Python"))

# 10. format_map()
data = {"name": "Sinchana", "lang": "Python"}
print("My name is {name} and I love {lang}".format_map(data))

# 11. index()
print(text.index("world"))  # 6

# 12. isalnum()
print(mixed_text.isalnum())  # True

# 13. isalpha()
print(alpha_text.isalpha())  # True

# 14. isascii()
print(text.isascii())  # True

# 15. isdecimal()
print(num_text.isdecimal())  # True

# 16. isdigit()
print(num_text.isdigit())  # True

# 17. isidentifier()
print("myVar1".isidentifier())  # True

# 18. islower()
print(text.islower())  # True

# 19. isnumeric()
print(num_text.isnumeric())  # True

# 20. isprintable()
print(text.isprintable())  # True

# 21. isspace()
print(space_text.isspace())  # True

# 22. istitle()
print("Hello World".istitle())  # True

# 23. isupper()
print("PYTHON".isupper())  # True

# 24. join()
print("-".join(["a", "b", "c"]))  # a-b-c

# 25. ljust()
print(text.ljust(20, "*"))  # hello world*********

# 26. lower()
print("PYTHON".lower())  # python

# 27. lstrip()
print("   hello".lstrip())  # 'hello'

# 28. maketrans() + translate()
trans = str.maketrans("h", "H")
print(text.translate(trans))  # Hello world

# 29. partition()
print(text.partition(" "))  # ('hello', ' ', 'world')

# 30. replace()
print(text.replace("world", "Python"))  # hello Python

# 31. rfind()
print(text.rfind("l"))  # 9

# 32. rindex()
print(text.rindex("l"))  # 9

# 33. rjust()
print(text.rjust(20, "-"))  # ---------hello world

# 34. rpartition()
print(text.rpartition(" "))  # ('hello', ' ', 'world')

# 35. rsplit()
print("a,b,c".rsplit(","))  # ['a', 'b', 'c']

# 36. rstrip()
print("hello   ".rstrip())  # 'hello'

# 37. split()
print("a b c".split())  # ['a', 'b', 'c']

# 38. splitlines()
print("Hello\nWorld".splitlines())  # ['Hello', 'World']

# 39. startswith()
print(text.startswith("hello"))  # True

# 40. strip()
print("   hello   ".strip())  # 'hello'

# 41. swapcase()
print("Hello World".swapcase())  # hELLO wORLD

# 42. title()
print(text.title())  # Hello World

# 43. upper()
print(text.upper())  # HELLO WORLD

# 44. zfill()
print("42".zfill(5))  # 00042

print("\t")

#in order to print multi line strings in the same order ,so we are using ''' or """
text='''my name is sinchana kulal,
iam learning python at "18th august ,2025"'''
print(text)

#to find the length of the string
print(len(text))

print("\t")

