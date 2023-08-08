from instagrapi import Client 

class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password 
        self.client = Client()
    
    def sign_in(self):
        self.client.login(self.username, self.password)
    
    def sign_out(self):
        self.client.logout(self.username, self.password)

    def post(self, image, caption):
        self.client.photo_upload(image, caption)
    
    def multiple_post(self, caption, images):
         self.client.album_upload(images, caption)