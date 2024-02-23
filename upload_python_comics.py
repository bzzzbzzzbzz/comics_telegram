from dotenv import load_dotenv
import os
import dwnld_sent_img_text as ds

if __name__ == '__main__':
    load_dotenv()
    image = 'comics.png'
    url = 'https://xkcd.com/353/info.0.json'
    author_comment = ds.get_author_comment(url)
    ds.download_image(url, image)
    tg_token = os.environ['TG_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']

    ds.send_message_to_group(tg_token, tg_chat_id, author_comment)
    ds.send_image_to_group(tg_token, tg_chat_id, image)
    os.remove(image)
