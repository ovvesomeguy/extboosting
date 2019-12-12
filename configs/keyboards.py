keylist = ['Купить', 'Вызвать Администратора' , 'Помочь денюшкой' , 'Дискорд' , 'Правила' , 'Да' , 'Нет' , 'Настройки' , 'Настроить Discord' , 'Настроить Steam' , 'Посмотреть настройки']


main_keyboard = {
    'one_time': False,
    'buttons': [
        [{'color': 'negative' , 'action': {'type': 'text', 'label': 'Вызвать Администратора'}}],
        [
            {'color': 'primary' , 'action': {'type': 'text' , 'label': 'Купить'}},
            {'color': 'primary' , 'action': {'type': 'text' , 'label': 'Помочь денюшкой'}},
        ],
        [{'color': 'primary' , 'action': {'type': 'text' , 'label': 'Дискорд'}}],
        [{'color': 'primary' , 'action': {'type': 'text' , 'label': 'Правила'}}],
        [{'color': 'primary' , 'action': {'type': 'text' , 'label': 'Настройки'}}]
    ]
}

products_yes = {    
    'one_time': False,
    'buttons': [
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Буст 5x5'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Буст 2x2'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Прайм аккаунт'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Нонпрайм аккаунт'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Буст часов'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Буст лайков'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Буст коментариев'}}],
        # [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #8'}}],
        # [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #9'}}],
        [{'color': 'primary' , 'action': {'type': 'text' , 'label': 'Вернуться'}}]
    ]
}

products_no ={    
    'one_time': False,
    'buttons': [
        [{'color': 'negative' , 'action': {'type': 'text' , 'label': 'Буст 5x5'}}],
        [{'color': 'negative' , 'action': {'type': 'text' , 'label': 'Буст 2x2'}}],
        [{'color': 'negative' , 'action': {'type': 'text' , 'label': 'Прайм аккаунт'}}],
        [{'color': 'negative' , 'action': {'type': 'text' , 'label': 'Нонпрайм аккаунт'}}],
        [{'color': 'negative' , 'action': {'type': 'text' , 'label': 'Буст часов'}}],
        [{'color': 'negative' , 'action': {'type': 'text' , 'label': 'Буст лайков'}}],
        [{'color': 'negative' , 'action': {'type': 'text' , 'label': 'Буст коментариев'}}],
        # [{'color': 'negative' , 'action': {'type': 'text' , 'label': 'Пример товара #8'}}],
        # [{'color': 'negative' , 'action': {'type': 'text' , 'label': 'Пример товара #9'}}],
        [{'color': 'primary' , 'action': {'type': 'text' , 'label': 'Вернуться'}}]
    ]
}
yes_or_no = {
    'one_time': True,
    'buttons': [
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Да'}}],
        [{'color': 'negative' , 'action': {'type': 'text' , 'label': 'Нет'}}],
    ]
}


settings = {
    'one_time': False,
    'buttons': [
        [
            {'color': 'positive' , 'action': {'type': 'text' , 'label': 'Настроить Discord'}},
            {'color': 'positive' , 'action': {'type': 'text' , 'label': 'Настроить Steam'}}
        ],
        [{'color': 'primary' , 'action': {'type': 'text' , 'label': 'Посмотреть настройки'}}]
    ]
}

give_me_money = {
    'one_time': False,
    'buttons': [
        [{'action': {'type': 'vkpay' , 'hash': 'action=pay-to-group&amount=1&group_id=188933965&aid=10.'}}]
    ]
}

clear_keyboard = {
    'one_time': True,
    'buttons': []
}