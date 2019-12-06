from vk_api.longpoll     import VkLongPoll, VkEventType
from configs.keys        import vk_key
import configs.keyboards as keyboards

import vk_api
import random
import json

vk = vk_api.VkApi(token=vk_key)
lp = VkLongPoll(vk)

def check(): # функция возращающая  последнее пришедшее сообщение и ID пользователя который его отправил
    answer = {}
    longpoll = VkLongPoll(vk)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.from_user:
                answer['id'] = event.user_id
                answer['message'] = event.text
                return answer

def get_info(user_id , name=False):
    v = vk.method('users.get' , {'user_ids': [user_id] , 'name_case': 'nom'})
    if name is True:
        return v[0]['first_name']
    else:
        return v[0]['first_name'] + ' ' + v[0]['last_name']

def back_to_menu(user_id , message='Вот наше меню'):
    vk.method('messages.send' , {'user_id': user_id , 'random_id': random.randint(0 , 2147483647) , 'keyboard': json.dumps(keyboards.main_keyboard) , 'message': message})

def user_with_url(user_id):
    user_name = get_info(user_id)
    return '[id{0}|{1}]'.format(user_id , user_name)

def know_rules(user_id):
    return True # TODO


ids = ['138966574' , '263838377']
chat_prefix = 'https://vk.com/gim188933965?sel{0}'
def main():
    print('I`am started')
    while True:
        msg = check()
        if msg['message'] not in keyboards.keylist:            
            back_to_menu(msg['id'])
        else:
            if msg['message'] == 'Купить':
                vk.method('messages.send' , {'user_id': msg['id'] , 'random_id': random.randint(0 , 2147483647) , 'keyboard': json.dumps(keyboards.products) , 'message': 'Вот товары'})
            elif msg['message'] == 'Вернуться':
                back_to_menu(msg['id'])
            elif msg['message'] == 'Дискорд':
                back_to_menu(msg['id'] , message='https://discordapp.com/invite/VaGq52d')
            elif msg['message'] == 'Вызвать Администратора':
                vk.method('messages.send' , {'user_id': ids[1] , 'random_id': random.randint(0 , 2147483647) , 'message': 'Пользователь {0} вызвал администратора.Вот ссылка на чат:{1}'.format(user_with_url(msg['id']) , chat_prefix.format(msg['id']))})
                back_to_menu(msg['id'] , message='{0}, спасибо.Ожидайте.'.format(get_info(msg['id'] , name=True)))
            elif msg['message'] == 'Правила':
                vk.method('messages.send' , {'user_id': msg['id'] , 'random_id': random.randint(0 , 2147483647) , 'keyboard': json.dumps(keyboards.yes_or_no) , 'message': 'Вот типа наши правила.Вы ознакомились с ними?'})
            elif msg['message'] == 'Да':
                back_to_menu(msg['id'] , message='Вы согласились с правилами нашего сообщества.')

if __name__ == "__main__":
    main()

