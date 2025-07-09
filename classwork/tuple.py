# Tuple creation
t1 = ()                      
t2 = (5,)                    
t3 = (1, "apple", 3.5)       
t4 = 1, 2, 3                 
print(t1, t2, t3, t4)

# Indexing & slicing
t = (10, 20, 30, 40, 50)
print(t[2])                  
print(t[-1])                 
print(t[1:4])                

# Tuple operations
a = (1, 2)
b = (3, 4)
print(a + b)                 
print(a * 3)                 
print(2 in a)                
print(5 not in a)            

# Tuple unpacking
x, y, z = (1, 2, 3)
print(x, y, z)

# Tuple methods
t = (1, 2, 2, 3)
print(t.count(2))            
print(t.index(3))            

# Built-in functions
n = (5, 10, 15)
print(len(n))                
print(max(n))                
print(min(n))                
print(sum(n))                
print(tuple([4, 5, 6]))      

# Tuple immutability
nested = (1, [2, 3])
nested[1][0] = 100
print(nested)                

# Tuple as dict key
d = {(1, 2): "yes"}
print(d[(1, 2)])

# Function returning tuple
def get_vals():
    return (10, 20)
a, b = get_vals()
print(a, b)

# Conversion
print(list((1, 2, 3)))
print(tuple([7, 8, 9]))
