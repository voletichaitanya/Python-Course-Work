s = "chaitanya"          # string declaration
s1 = 'hii'               # string declaration
s2 = '''voleti'''        # string initialization

a = s + s1               # concatenate strings without space
print(a)

b = s + " " + s1         # concatenate with space
print(b)

c = s * 3                # repeat string 3 times
print(c)

d = s[1]                 # indexing (2nd character)
print(d)

e = len(s)               # length of string
print(e)

f = min(s)               # minimum (lexicographically)
print(f)

g = max(s)               # maximum (lexicographically)
print(g)

l = ['hi', 'hii', 'apple', 'banana', 'hello']
print(sorted(l))         # sort list alphabetically

print(ord('a'))          # ASCII value of 'a'
print(chr(65))           # character for ASCII 65

print(s.upper())         # convert to uppercase
print(s.lower())         # convert to lowercase
print(s.capitalize())    # capitalize first letter
print(s.title())         # capitalize each word
print(s.swapcase())      # swap case
print(s.casefold())      # aggressive lowercase (for comparisons)

print(s.center(10, '*')) # center with '*'
print(s.ljust(10, '-'))  # left-justify with '-'
print(s.rjust(10, ';'))  # right-justify with ';'
print(s.zfill(5))        # pad with zeros on the left

print(f'hi how are you {s} ')  # f-string formatting

print(s.find(a))         # index of substring a
print(s.rfind(a))        # last index of substring a
print(s.count(a))        # count occurrences of a

# String testing methods
print(s.startswith(a))   # check start
print(s.endswith(a))     # check end
print(s.isalpha())       # all alphabetic?
print(s.isalnum())       # alphanumeric?
print(s.islower())       # all lowercase?
print(s.isspace())       # only spaces?
print(s.istitle())       # title case?
print(s.isidentifier())  # valid variable name?

print(s.split(a))        # split by substring a
print(s.rsplit(a))       # split from right
print(s.join("hello"))   # insert s between each char of "hello"

print(s.partition(c))    # split at first occurrence of c
print(s.strip(a))        # remove a from both ends if present
print(s.encode())        # encode to bytes
