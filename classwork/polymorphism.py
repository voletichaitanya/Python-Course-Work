class NormalUser:
    def __init__(self,username):
        self.username = username
        print(f'\nWelcome to youtube \n {self.username} \naccount is created')
    def playvideo(self):
        print("Ads included")
        print("No Background play")
        print("Limited Content")
        print("Download Quality less")
        print("ads on YT music")
    def profile(self):
        print("You can upload your profile")
    def MultipleDevice(self):
        print("You can login from different devices")
    def shorts(self):
        print("You can see shorts")
    def likes(self):
        print("Likes")
    def comments(self):
        print("Comments")
    def share(self):
        print("Share")
    def subscribe(self):
        print("Subscribe")


class PremiumUser(NormalUser):
    def __init__(self, username):
        super().__init__(username)
    def playvideo(self):
        print('Ads Free')
        print('You can play on Background')
        print('Exclusive content')
        print('Download with hign Quality')
        print('YT music is available')

hemanth=NormalUser('hemanth')
hemanth.playvideo()
hemanth.profile()
hemanth.shorts()
hemanth.MultipleDevice()
hemanth.likes()
hemanth.share()
hemanth.comments()
hemanth.subscribe()

shesu=PremiumUser('Sheshu')
shesu.playvideo()
shesu.profile()
shesu.shorts()
shesu.MultipleDevice()
shesu.likes()
shesu.share()
shesu.comments()
shesu.subscribe()