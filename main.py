import os
import datetime
import random
import openai
from PIL import Image
import requests
from dotenv import load_dotenv
from get_image import get_image
load_dotenv()

TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')
API_KEY = os.getenv('API_KEY')
openai.api_key = API_KEY

dalle_uses = 0

# Artists
rembrandt = "Rembrandt"
van_gogh = "Van Gogh"
pollock = "Jackson Pollock"
picasso = "Picasso"
gainsborough = "Gainsborough"
da_vinci = "Da Vinci"

# Mediums
oil_on_canvas = "Oil on Canvas"
acrylic_on_canvas = "Acrylic on Canvas"
watercolor = "Watercolor"
charcoal = "Charcoal"
pencil = "Pencil"
pastel = "Pastel"

now = datetime.datetime.now()


def get_prompt():
    print("What artist would you like to use?")
    print("1. Rembrandt")
    print("2. Van Gogh")
    print("3. Jackson Pollock")
    print("4. Picasso")
    print("5. Gainsborough")
    print("6. Da Vinci")
    print("7. Random")
    print("8. Custom (Enter your own artist name")

    artist = input("Enter the number of the artist you would like to use: ")

    num_pictures = int(input("How many pictures would you like to generate? "))

    prompt = input("What is your image prompt?\n")

    dalle(artist, num_pictures, prompt)


def dalle(artist, num_pictures, prompt):
    global dalle_uses
    dalle_uses += 1
    if artist == "1":
        artist = rembrandt
    elif artist == "2":
        artist = van_gogh
    elif artist == "3":
        artist = pollock
    elif artist == "4":
        artist = picasso
    elif artist == "5":
        artist = gainsborough
    elif artist == "6":
        artist = da_vinci
    elif artist == "7":
        artist = get_random_artist()
    elif artist == "8":
        artist = input("Enter your artist name: ")

    print("What medium would you like to use?")
    print("1. Oil on Canvas")
    print("2. Acrylic on Canvas")
    print("3. Watercolor")
    print("4. Charcoal")
    print("5. Pencil")
    print("6. Pastel")
    print("7. Random")
    print("8. Custom (Enter your own medium name")

    medium = input("Enter the number of the medium you would like to use: ")

    if medium == "1":
        medium = oil_on_canvas
    elif medium == "2":
        medium = acrylic_on_canvas
    elif medium == "3":
        medium = watercolor
    elif medium == "4":
        medium = charcoal
    elif medium == "5":
        medium = pencil
    elif medium == "6":
        medium = pastel
    elif medium == "7":
        mediums = [oil_on_canvas, acrylic_on_canvas, watercolor, charcoal, pencil, pastel]
        medium = random.choice(mediums)
    elif medium == "8":
        medium = input("Enter your medium name: ")

    full_prompt = prompt + " by " + artist + ", " + medium
    print("Generating images...")
    get_image(num_pictures, full_prompt)
    print(f"Generated {num_pictures} images for {full_prompt} at {now.strftime('%Y-%m-%d %H:%M:%S')}.")

def get_random_artist():
    artists = [rembrandt, van_gogh, pollock, picasso, gainsborough, da_vinci]
    return random.choice(artists)

def run():
    print("Welcome to DALL-E!")
    while True:
        get_prompt()

run()


