import requests


def send_image_to_group(bot_token, chat_id, image_path):
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    files = {'photo': open(image_path, 'rb')}
    data = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print("Image post successfully!")
    else:
        print(f"Failed to send image. Status code: {response.status_code}")


def send_message_to_group(bot_token, chat_id, text):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")



def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    image_link = response.json()['img']
    image_response = requests.get(image_link)
    image_response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(image_response.content)


def get_author_comment(url):
    response = requests.get(url)
    response.raise_for_status()
    author_comment = response.json()['alt']
    return author_comment


