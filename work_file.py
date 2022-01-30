import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-ключ созданный ранее
token = "2ee57b0c0022a5aa25b0357ac7eb7a6123b7ae5d52cf90dfe00ae837e8e7e4a040f7c28f401060f8ed777"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

print("Работа пошла!")
# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(
                event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key=(''),  # ВСТАВИТЬ ПАРАМЕТРЫ
                    server=(''),
                    ts=(''),
                    random_id=get_random_id(),
                    message='Привет!',
                    chat_id=event.chat_id
                )
        if 'Клавиатура' in str(event):
            if event.from_chat:
                vk.messages.send(
                    keyboard=keyboard.get_keyboard(),
                    key=(''),  # ВСТАВИТЬ ПАРАМЕТРЫ
                    server=(''),
                    ts=(''),
                    random_id=get_random_id(),
                    message='Держи',
                    chat_id=event.chat_id
                )
