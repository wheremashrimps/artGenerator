import openai
from PIL import Image
import requests

def get_image(num_images, prompt):
    for i in range(num_images):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        image = Image.open(requests.get(image_url, stream=True).raw)
        image.save("images/" + prompt + str(i) + ".png", "PNG")
        print(prompt + '\n' + image_url)