from lib.ai import AI
from lib.bot import Bot

import requests
from PIL import Image
from io import BytesIO
import time
from datetime import datetime, timedelta 

api_key ='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'
generator = AI(api_key)
instabot =  Bot("tammys_bot", "owewapi") 
instabot.sign_in() 

def make_post():
    print("Task execute at:", datetime.now()) 

    res, image_url = generator.generate_prompt_image()

    print('prompt: ', res)
    print('Images: ', image_url )

    for i in range(3):
        response = requests.get(image_url[i]) 
        img = Image.open(BytesIO(response.content))
        img.save(f"images/{i}.jpg")
    
    path = ["images/0.jpg", "images/1.jpg", "images/2.jpg"]
    caption = "AI generated brooo"
    instabot.multiple_post(caption, path) 

make_post()