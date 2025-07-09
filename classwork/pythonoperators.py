#pythonoperators.py

#1 Arithmetic operators

a = 10
b = 20
print("Addition (+): ",a+b)           #Addition (+):
print("Substraction(-) : ",a-b)        #Substraction(-)
print("Multiplication(*) : ",a*b)          #Multiplication(*)
print("Division (/): ",a/b)           #Division (/)
print("Floor Division(//) : ",a//b)     #Floor Division(//)
print("Modulus (%): ",a%b)             #Modulus (%)
print("Exponentiation (**): ",a**2)   #Exponentiation (**)



#2.Comparision Operators

print("Equal  : ", a == b)              # Equal  : False
print("Not Equal : ",a!=b)              # Not Equal :True 
print("Greater Than : ",a>b)            # Greater Than : False
print("LessThan : ",a<b)                # LessThan : True
print("LessThan Or Equal : ",a<=b)      # LessThan Or Equal : True
print("Greater Than Or Equal : ",a>=b)  # Greater Than Or Equal : False


#3.Assignnment Operators

x = 5
print("Initial value of x:", x)

x += 3
print("Add & Assign (x += 3):", x)  # x = 5 + 3 = 8

x -= 2
print("Subtract & Assign (x -= 2):", x)  # x = 8 - 2 = 6

x *= 4
print("Multiply & Assign (x *= 4):", x)  # x = 6 * 4 = 24

x /= 2
print("Divide & Assign (x /= 2):", x)  # x = 24 / 2 = 12.0 (float)

x //= 3
print("Floor Divide & Assign (x //= 3):", x)  # x = 12.0 // 3 = 4.0

x %= 2
print("Modulus & Assign (x %= 2):", x)  # x = 4.0 % 2 = 0.0

x **= 3
print("Exponentiate & Assign (x **= 3):", x)  # x = 0.0 ** 3 = 0.0


#4.Logical Operators

x = 10
y = 12

print("x =", x)
print("y =", y)

print("AND (x > 5 and y < 15):", x > 5 and y < 15)  # AND   ->  True and True → True

print("OR (x < 5 or y > 15):", x < 5 or y > 15)     #  OR    ->  False or False → False

print("NOT (x > 5):", not (x > 5))                  #   NOT  ->  not True → False

<<<<<<< HEAD:pythonoperators.py

=======
>>>>>>> 5ebdbfe708b42d7bc3f4ad703851c9d4fe76efe3:classwork/pythonoperators.py
#5.Membership Operator

text = "apple"

<<<<<<< HEAD:pythonoperators.py
print('"a" in "apple" : ', "a" in text)       #  IN -> True 

print('"x" not in "apple" : ', "x" not in text)  # NOT IN -> True

# 6.Identity Operator  


x = [1, 2, 3]
y = x                      # y points to the same object as x
z = [1, 2, 3]              # z has same content as x but is a different object
=======
print('"a" in "apple" : ', "a" in text)       #  IN -> True → 'a' is in 'apple'

print('"x" not in "apple" : ', "x" not in text)  # NOT IN -> True → 'x' is not in 'apple'

# 6.Identity Operator
x = [1, 2, 3]
y = x         # y points to the same object as x
z = [1, 2, 3] # z has same content as x but is a different object
>>>>>>> 5ebdbfe708b42d7bc3f4ad703851c9d4fe76efe3:classwork/pythonoperators.py

print("x is y : ", x is y)         # IS -> True → x and y refer to the same object
print("x is z : ", x is z)         # False → x and z have same values but are different objects

print("x is not z : ", x is not z) # IS NOT -> True → x and z are different objects

# 7. Bitwise Operators

a = 5  
b = 3  

print("AND (5 & 3) :  ", a & b)        #AND ->  0101 & 0011 = 0001 → 1

print("OR (5 | 3)  : ", a | b)         # OR ->   0101 | 0011 = 0111 → 7

print("XOR (5 ^ 3) : ", a ^ b)        # XOR ->  0101 ^ 0011 = 0110 → 6

print("NOT (~5)   :  ", ~a)              # NOT  ->  ~0101 = -(0101 + 1) = -6 (in 2's complement)

print("Left Shift (5 << 1)  :  ", a << 1)  # Lefte shift -> 0101 << 1 = 1010 → 10

print("Right Shift (5 >> 1) : ", a >> 1) #Right SHift  -> 0101 >> 1 = 0010 → 2
