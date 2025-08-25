import os
print(os.getcwd())

if not os.path.exists("DSDA"):
    os.mkdir("DSDA")
    print("File created")
    os.rmdir("DSDA")
    print("File operations done and deleted")
os.system("notepad")

if not os.path.exists("DADS"):
    os.mkdir("DADS")
    filepath = os.path.join()