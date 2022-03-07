from pypresence import Presence
import time
from os import getenv

print("#WeAreTogetherRussian")
print("#МыВместеРоссия")
print("Спасибо, что стали частью нашего")
print("коммьюнити!")
print("===========================")

client_id = getenv("PRESENCE_ID")
rpc = Presence(client_id=client_id)

print("Авторизуемся. Дискорд должен быть запущен")
print("Подробнее читайте на нашем сайте:")
print("https://dmlomov.github.io/ruhelp/presence/")
print("===========================")

try:
    rpc.connect()
except:
    print("Авторизация не удалась. Попробуйте позже!")
    exit()

print("Авторизация успешна.")
print("Обновляю RPC...")
print("===========================")

war_start = 1645650060
buttons = [
    {
        "label": "Помочь Российской Федерации",
        "url": "https://dmlomov.github.io/ruhelp/"
    },
    {
        "label": "Связь с нами",
        "url": "https://github.com/dmlomov/"
    }
]

while True:
    try:
        rpc.update(
            state='Помогите РФ в трудное время, патриоты!',
            details='Все вместе мы справимся #МыВместеРоссия',
            start=war_start,
            end=war_start,
            buttons=buttons,
            large_image='russian_flag',
            large_text='Вместе мы справимся #МыВместеРоссия'
        )
        time.sleep(5)
    except:
        print("Обновление RPC прервано... Возможные причины:")
        print("1. Выполнение прервано Ctrl+C (перезапустите)")
        print("2. Невозможно подключится к серверам Discord (подождите, пока всё починят)")
        print("3. Слишком частое обновление (подождите)")
        break

print("Спасибо, что вы с нами! #МыВместеРоссия")
