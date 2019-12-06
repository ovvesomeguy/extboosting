keylist = ['Купить', 'Вызвать Администратора' , 'Помочь денюшкой' , 'Дискорд' , 'Правила' , 'Да' , 'Нет']


main_keyboard = {
    'one_time': False,
    'buttons': [
        [{'color': 'negative' , 'action': {'type': 'text', 'label': 'Вызвать Администратора'}}],
        [
            {'color': 'primary' , 'action': {'type': 'text' , 'label': 'Купить'}},
            {'color': 'primary' , 'action': {'type': 'text' , 'label': 'Помочь денюшкой'}},
        ],
        [{'color': 'primary' , 'action': {'type': 'text' , 'label': 'Дискорд'}}],
        [{'color': 'secondary' , 'action': {'type': 'text' , 'label': 'Правила'}}]
    ]
}

products = {
    'one_time': False,
    'buttons': [
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #1'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #2'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #3'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #4'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #5'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #6'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #7'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #8'}}],
        [{'color': 'positive' , 'action': {'type': 'text' , 'label': 'Пример товара #9'}}],
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
