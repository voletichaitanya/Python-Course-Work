class Instagram:
    def __init__(self, username, password):
        print("Welcome to Instagram")
        self.__bio = ''  # private variable
        self.posts = []
        self.followers = []
        self.following = []
        self.username = username
        self.__password = password  # private variable
        print(f'Hello {self.username} login successful')
    
    # Getter for bio
    @property
    def bio(self):
        return self.__bio
    
    # Setter for bio
    @bio.setter
    def bio(self, upd_bio):
        self.__bio = upd_bio

    # Getter for password
    def showPassword(self):
        return self.__password
    
    # Setter for password
    def updatePassword(self, new_pwd):
        self.__password = new_pwd
        return "Password updated successfully"
        

# Create object
mani = Instagram('manikanta', 'mani@123')

# Public variables
print("Bio:", mani.bio)
print('Posts:', mani.posts)
print('Followers:', mani.followers)
print('Following:', mani.following)
print('Username:', mani.username)

# Modify public variables
mani.bio = 'sigma'
mani.posts.append('Pyth.png')
mani.followers.extend(['ras', 'varun', 'tarit'])
mani.following.extend(['ntr', 'rajini', 'kohli'])
mani.username = 'mani_09'

# After updating
print("Bio:", mani.bio)
print('Posts:', mani.posts)
print('Followers:', mani.followers)
print('Following:', mani.following)
print('Username:', mani.username)

# Private variables (through methods)
print("Old Password:", mani.showPassword())
print(mani.updatePassword('sada'))
print("New Password:", mani.showPassword())



class Login:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private
        self._otp = 1234  # protected

    # Getter for private password
    def getpassword(self):
        return self.__password

    # Setter for private password
    def updatePassword(self, new_pwd):
        self.__password = new_pwd

    # OTP getter
    @property
    def publicotp(self):
        return self._otp

    # OTP setter
    @publicotp.setter
    def publicotp(self, value):
        self._otp = value


# Create object
vikash = Login("vikash", "vk@123")

# Public variable
print("#public")
print("Username:", vikash.username)

# Private variable
print("\n#private")
print("Password:", vikash.getpassword())

# Protected variable via property
print("\n#protected")
print("OTP:", vikash.publicotp)

# Updating public
vikash.username = "_vikash_"
print("\nUpdated username:", vikash.username)

# Updating private
vikash.updatePassword("Vk@18")
print("Updated password:", vikash.getpassword())

# Updating protected via property
vikash.publicotp = 1111
print("Updated OTP:", vikash.publicotp)