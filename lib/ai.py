import os
import openai

openai.api_key = os.getenv("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") 

class AI:
    def __init__(self, api_key):
        openai.api_key = api_key
    
    def generate_prompt(self):
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = "Generate me a prommpt of some random image(max 50 words)",
            temperature = 1.4,
            max_tokens = 50,
            top_p = 1
        )
        return response['choices'][0]['text']
    
    def generate_images(self, prompt):
        response = openai.Image.create(
             prompt = prompt,
             n = 3,
             size = '512x512'
        )

        img_url = [
            response['data'][0]['url'],
            response['data'][1]['url'],
            response['data'][2]['url']
        ]
        return img_url
    
    def generate_prompt_image (self):
        prompt = self.generate_prompt()
        images = self.generate_images(prompt)
        return prompt, images
