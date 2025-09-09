class NormalUser():
    def __init__(self,username):
        self.username=username
        print(f'\nWelcome to youtube "{self.username}". explore our content..')

    def playvedio(self):
        print('Ads  Included')
        print('No Background Play')
        print('Download with Low Quality')
        print('No yt music')
    def profile(self):
        print('You can upload your profile')
    def MultipleDevice(self):
        print('you can login with different devices')
    def shorts(self):
        print('You can see the yt shorts')
    def likecommentshare(self):
        print('You can like share and comment')

class PremiumUser(NormalUser):
    def __init__(self,username):
        super().__init__(username)

    def playvedio(self):
        print('Ads Free')
        print('You can play on Background')
        print('Exclusive content')
        print('Download with hign Quality')
        print('YT music is available')

hemanth=NormalUser('hemanth')
hemanth.playvedio()
hemanth.profile()
hemanth.shorts()
hemanth.MultipleDevice()
hemanth.likecommentshare()

shesu=PremiumUser('Sheshu')
shesu.playvedio()
shesu.profile()
shesu.shorts()
shesu.MultipleDevice()
shesu.likecommentshare()

class Number:
    def __init__(self,number):
        self.number=number
    
    def __str__(self):
        return f'{self.number}'

    def __add__(self,other):
        return self.number+other.number
    
    def __sub__(self,other):
        return self.number-other.number
    
    def __mul__(self,other):
        return self.number*other.number
    
    def __truediv__(self,other):
        return self.number/other.number
    
    def __eq__(self,other):
        return self.number==other.number
    
    def __lt__(self,other):
        return self.number<other.number
    
    def __gt__(self,other):
        return self.number>other.number
   
n1=Number(10)
n2=Number(20)
print(f'number: {n2}')
print(f'add : {n1+n2}')
print(f'sub : {n2-n1}')
print(f'mul : {n1*n2}')
print(f'div : {n2/n1}')
print(f'equal : {n1==n2}')
print(f'lessthan : {n1<n2}')
print(f'greaterthan : {n1>n2}')
    