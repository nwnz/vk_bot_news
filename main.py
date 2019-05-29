api_key = 'f5911bd162fee3301832f928246ef3c3b9534352d2f1f7da48f68212d9019f8c0c7da5d7cc123ada372ba'


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
            body = messages["items"][0]["last_message"]["text"]
            newss = news.search_publication_in_request(body.lower(), 'ru', '1', '1')
            vk.method("messages.send", {"peer_id": id, "message": f'Главная новость: {newss}', "random_id": random.randint(1, 2147483647)})
            # if body.lower() == "привет":
            #     vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            # elif body.lower() == "Пока":
            #     vk.method("messages.send", {"peer_id": id, "message": "Доброго дня!", "random_id": random.randint(1, 2147483647)})
            # else:
            #     vk.method("messages.send", {"peer_id": id, "message": "Не понял тебя!", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        vk.method("messages.send", {"peer_id": id, "message": f'АШИПКА', "random_id": random.randint(1, 2147483647)})