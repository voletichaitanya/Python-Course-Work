
#Exception handling

# value Error

try:
    a=int(input("enter the value:"))
    print(a)
except ValueError:
    print("Enter the proper data type(Value error)!!")
# Type Error

try:
    c=1+'1'
except TypeError:
    print("you can't add 2 diff types(Type error)")

    print("Enter the proper data type(Value error)!!")

#Key Error
try:
    d={1:2,2:3,3:4}
    print(d[4])
except KeyError:
    print("key is not present(Keyvalue error)")

#Index Error
try:
    l=[1,2,3,4]
    k=l[7]
except IndexError:
    print('you ve entered the out of range(Index error)')

#Name Error
try:
    a+=10 
except NameError:
    print('a is not defined')



# Any Exception
try:
    a=10
    a+=10
    l=[1,2,3,4]
    k=l[2]
    d={1:2,2:3,3:4}
    print(d[1])
    b=int(input('Enter a number:'))
    print(b)
    c=1+'12'

except Exception as e:
    print(f'Error occured:{e}')

'''
except (NameError,IndexError,ValueError,TypeError,KeyError) as e:
    print(f'Error occured: {e}')
'''

try:
    a=10
    a+=10
    l=[1,2,3,4]
    k=l[2]
    d={1:2,2:3,3:4}
    print(d[1])
    b=int(input('Enter a number:'))
    print(b)
    c=1+10

except Exception as e:
    print(f'Error occured:{e}')

else:
    print('No errors')
try:
    a=10
    a+=10
    l=[1,2,3,4]
    k=l[22]
    d={1:2,2:3,3:4}
    print(d[1])
    b=int(input('Enter a number:'))
    print(b)
    c=1+10

except Exception as e:
    print(f'Error occured:{e}')

else:
    print('No errors')

finally:
    print('Code is exceuted..')




try :
    amount = int(input("Enter the amount : "))
    if amount < 0 :
        raise ValueError("Enter the positive value")
except Exception as e:
    print(f"Error occured : {e} ")
else:
    print("No errors")
    print("You can withdraw")
finally:
    print("----------Remove your card----------")