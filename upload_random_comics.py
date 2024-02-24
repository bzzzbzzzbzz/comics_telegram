import requests
from dotenv import load_dotenv
import os
import get_send_img_text as ds
import random


def get_random_comics_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    last_comics = response.json()['num']
    random_comics = random.randrange(last_comics)
    return random_comics


if __name__ == '__main__':
    load_dotenv()
    random_comics = get_random_comics_number()
    image = 'comics.png'
    url = f'https://xkcd.com/{random_comics}/info.0.json'
    author_comment = ds.get_author_comment(url)
    try:
        ds.download_image(url, image)
        tg_token = os.environ['TG_TOKEN']
        tg_chat_id = os.environ['TG_CHAT_ID']

        ds.send_message_to_group(tg_token, tg_chat_id, author_comment)
        print('Message sent successfully!')
        ds.send_image_to_group(tg_token, tg_chat_id, image)
        print('Image post successfully!')
    finally:
        os.remove(image)
