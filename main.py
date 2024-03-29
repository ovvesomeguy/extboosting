#!/usr/bin/python3
import configs.keyboards as keyboards

import datetime
import vk_api
import random
import json
import time
import os


from configs.keys         import admin_ids
from configs.rules        import rules

from src.utils.logger     import Logger
from src.vk.longpolling   import check
from src.database.control import Manager

from dotenv import load_dotenv
load_dotenv()

class VK:
    def __init__(self):
        self.vk = vk_api.VkApi(token=os.getenv('VK_KEY'))

    def get_info(self , user_id , name=False):
        v = self.vk.method('users.get' , {'user_ids': [user_id] , 'name_case': 'nom'})
        if name is True:
            return v[0]['first_name']
        else:
            return v[0]['first_name'] + ' ' + v[0]['last_name']

    def set_random_id(self):
        return random.randint(0 , 2147483647)
   
    def back_to_menu(self , user_id , message='Вот наше меню'):
        self.send_message(user_id = user_id , keyboard = json.dumps(keyboards.main_keyboard) , message = message)

    def send_message(self , user_id , message , keyboard=None):
        if keyboard is not None:
            self.vk.method('messages.send' , {'user_id': user_id , 'random_id': self.set_random_id() , 'keyboard': keyboard , 'message': message})
        else:
            self.vk.method('messages.send' , {'user_id': user_id , 'random_id': self.set_random_id() , 'message': message})
    def last_message(self , user_id):
        chat = self.vk.method('messages.getHistory' , {'user_id': user_id})
        if chat['count'] == 0:
            return None
        else:
            last_message = ''
            for item in chat['items'][1:]:
                if item['from_id'] == user_id:
                    last_message = item['text']
                    break
            return last_message
    def user_with_url(self , user_id):
        user_name = self.get_info(user_id)
        return '[id{0}|{1}]'.format(user_id , user_name)

    def know_rules(self , user_id):
        return True # TODO



chat_prefix = 'https://vk.com/gim188933965?sel{0}'
def main():
    v = VK()
    m = Manager(os.getcwd() + '/users.db')
    logger       = Logger('logs.log')
    started_time = time.strftime('%d:%m:%Y  %H:%M:%S')
    logger.log('Started time: {0}'.format(started_time))
    print('| I`am started at {0} |'.format(started_time))
    while True:
        msg = check(v.vk)
        last_user_message = v.last_message(msg['id'])
        if last_user_message is not None:
            if not m.exists(msg['id']):
                m.add_user(username=v.get_info(msg['id']) , user_id=msg['id'] , rules=0 , join_date=datetime.datetime.now() , promocode=0)
            else:
                if last_user_message == 'Настроить Discord':
                    if not '#' in msg['message'] or len(msg['message'].split('#')[1]) != 4:
                        v.back_to_menu(user_id=msg['id'] , message='Извините но это не похоже на дискорд тэг')
                    else:
                        m.change_value('discord' , msg['message'] , msg['id'])
                elif last_user_message == 'Настроить Steam':
                    m.change_value('steam' , msg['message'] , msg['id'])
        
        logger.log('Message {0} received from user {1}'.format(msg['message'] , msg['id']))
        if msg['message'] not in keyboards.keylist:            
            v.back_to_menu(msg['id'])
        else:
            if msg['message'] == 'Купить':
                if m.get_rules_status(msg['id']) == 0:
                    v.send_message(user_id = msg['id'] , keyboard = json.dumps(keyboards.products_no), message = 'Вам недоступна покупка товаров, пожалуйста ознакомтесь с правилами сообщества в разделе "Правила".')
                else:
                    v.send_message(user_id = msg['id'] , keyboard = json.dumps(keyboards.products_yes), message = 'Вот товары')
            elif msg['message'] == 'Вернуться':
                v.back_to_menu(msg['id'])
            elif msg['message'] == 'Дискорд':
                v.back_to_menu(msg['id'] , message='https://discordapp.com/invite/VaGq52d')
            elif msg['message'] == 'Вызвать Администратора':
                v.send_message(user_id = admin_ids[1] , message= 'Пользователь {0} вызвал администратора.Вот ссылка на чат:{1}'.format(v.user_with_url(msg['id']) , chat_prefix.format(msg['id'])))
                logger.log('User {0} call the admin'.format(msg['id']))
                v.back_to_menu(msg['id'] , message='{0}, спасибо.Ожидайте.'.format(v.get_info(msg['id'] , name=True)))
            elif msg['message'] == 'Правила':
                v.send_message(user_id = msg['id'] , keyboard = json.dumps(keyboards.yes_or_no) , message = rules)
            elif msg['message'] == 'Да': #TODO
                if m.get_rules_status(msg['id']) == 0:
                    v.back_to_menu(msg['id'] , message='Вы согласились с правилами нашего сообщества.Теперь вам доступны покупки в разделе "Купить товар".')
                    m.change_value('rules' , 1 , msg['id'])
                else:
                    v.back_to_menu(msg['id'] , message='Вы уже согласились с правилами нашего сообщества.')                    
            elif msg['message'] == 'Нет':
                v.back_to_menu(msg['id'] , message='Извините, но покупка товара будет ограничена до тех пор, пока вы не согласитесь с правилами сообщества.')
            elif msg['message'] == 'Настройки':
                v.send_message(user_id=msg['id'] , keyboard=json.dumps(keyboards.settings) , message='Настройки')
            elif msg['message'] == 'Настроить Discord':
                v.send_message(user_id=msg['id'] , message='Пожалуйста введите свой тэг' , keyboard=json.dumps(keyboards.clear_keyboard))
            elif msg['message'] == 'Настроить Steam':
                v.send_message(user_id=msg['id'] , message='Пожалуйста введите ссылку на свой аккаунт' , keyboard=json.dumps(keyboards.clear_keyboard))
            elif msg['message'] == 'Посмотреть настройки':
                ids = m.get_urls(msg['id'])
                v.send_message(user_id=msg['id'] , message='Привязанный аккаунт стим: {0}. Привязанные дискорд аккаунт: {1}'.format(ids[0][1] , ids[0][0]) , keyboard=json.dumps(keyboards.main_keyboard))
            elif msg['message'] == 'Помочь денюшкой':
                v.send_message(user_id=msg['id'] , message='.' , keyboard=json.dumps(keyboards.give_me_money))
if __name__ == "__main__":
    main()