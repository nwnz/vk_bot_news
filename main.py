api_key = 'apikey'


import vk_api
import time
import random
import datetime
import news
vk = vk_api.VkApi(token=api_key)
 
vk._auth_token()
now = datetime.datetime.now()
time = now.strftime("%d-%m-%Y %H:%M")

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            #get_user_id_in_bd = 
            # '''
            # SELECT users
            # where Users_ID = 
            # '''
            name = vk.method("users.get", {"user_ids": id})
            first_name = name[0]['first_name']
            last_name = name[0]['last_name']
            body = messages["items"][0]["last_message"]["text"]
            newss = news.search_publication_in_request(body.lower(), 'ru', '1', '1')
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": f'Привет, {first_name}', "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": f'Главная новость: {newss}', "random_id": random.randint(1, 2147483647)})
            # elif body.lower() == "Пока":
            #     vk.method("messages.send", {"peer_id": id, "message": "Доброго дня!", "random_id": random.randint(1, 2147483647)})
            # else:
            #     vk.method("messages.send", {"peer_id": id, "message": "Не понял тебя!", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        vk.method("messages.send", {"peer_id": id, "message": f'АШИПКА', "random_id": random.randint(1, 2147483647)})