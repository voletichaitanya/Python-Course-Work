try :
    file = open('app.py','r+')
except FileNotFoundError:
    print('the file does not exists')
else:
    file.seek(0)
    read = file.read()
    print(f"\nFile Content using read() : \n{read}")
    file.seek(0)
    readlines = file.readlines()
    file.seek(0)
    print(f"\n File Content is using readlines() : \n{readlines}")
    readline = file.readline()
    print(f"\n File Content is using readline() : \n{readline}")
    file.seek(0,2)
    writefiles=file.write("\n\nchaitanya\nrasool\nsriram\nvarun")
    print(writefiles)
finally :
    file.close()
    print("File closed")


try :
    file = open('list.py','w+')
except FileNotFoundError:
    print("File not exixts")
else:
    file.write("monday we have exam\n")
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("resst of the code")
