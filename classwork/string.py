s = "chaitanya"          #string declaration
s1 = 'hii'               #string declaration
s2 = '''voleti'''            #String initialization
a = s + s1              
print(a)              #string concatination without space
b = s + " " + s1           
print(b)              #String concatination with space
c = s * 3                 
print(c)              #Repeating Strings
d = s[1]              
print(d)                 #getting elements vis indexing
e = len(s)              
print(e)                #length of string
f = min(s)             
print(f)                 # minimum of string
g = max(s)               
print(g)               # maxium element
l = ['hi','hii','apple','banana','hello']
print(sorted(l))           # sorted list
print(ord('a'))             # returns order of a    
print(chr(65))              #character of 65
print(s.upper())            # uppercase the string
print(s.lower())           # lower case the string
print(s.capitalize())      # capitalizze the string
print(s.title())           # capitalize each word in string
print(s.swapcase())        # change lower case to upper case
print(s.casefold())        #converts string into lowercase more aggresively
print(s.center(10,'*'))    # center the string with * both sides
print(s.ljust(10,'-'))     # fill left side with - and gives the string
print(s.rjust(10,';'))     # fill rightside with ; and gives the string
print(s.zfill(5))          # pads the string with zeros on left side 
print(f'hi how are you {s} ')  # formatting the string with f  
print(s.find(a))
print(s.rfind(a))
print(s.count(a))
  #String Testing Methods
print(s.startswith(a))
print(s.endswith(a))
print(s.isalpha())
print(s.isalnum())
print(s.islower())
print(s.islower())
print(s.isspace())
print(s.istitle())
print(s.isidentifier())
print(s.split(a))
print(s.rsplit(a))
print(s.join("hello"))
print(s.partition(c))
print(s.strip(a))
print(s.encode())