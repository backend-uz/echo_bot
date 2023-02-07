import requests

TOKEN = '1950937652:AAGc_5TlnoAyuZdwGAago1E8msTLc1xtmec'

def get_last_updates():
    """
    Use this function to get updates from Telegram.

    Args:
        None
    Returns:
        int(chat_id): Telegram chat id
        str(text): Message text
        int(update_id): Telegram update id
    """
    r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
    return r.json()

def send_message():
    """
    Use this function to send text messages.

    Args:
        chat_id (int): Telegram chat id
        text (str): Message text
    Returns:
        None
    """

    user_msg = get_last_updates()['result'][-1]['message']

    payload = {
        "chat_id":f"{user_msg['chat']['id']}",
        "text":f"||{user_msg['text']}||",
        "reply_to_message_id":f"{user_msg['message_id']}",
        "parse_mode":"MarkdownV2",
        "protect_content":True,
            }
    
    r = requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params=payload)
    
    return r.json()

print(send_message())