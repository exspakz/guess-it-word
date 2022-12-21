views_dict = {
    'new': {
        'ans': {
            'new': {'view': 'hi'},
        },
    },
    'hi': {
        'text': 'Привет! Давай сыграем в Угадай АйТи слово.',
        'tts': 'Прив+ет! - Дав+ай сыгр+аем в Угадай +АйТи слово',
        'rtext': 'Играем сразу или сначала Рассказать правила?',  # Текст для переспроса
        'rtts': 'Играем сразу или сначала - Рассказать правила',
        'butt': ('Начать игру', 'Рассказать правила', 'Выйти'),
        'ans': {
            'start_game': {'view': 'ask'},
            'YANDEX.CONFIRM': {'view': 'ask'},
            'rules': {'view': 'rules'},
            'end_game': {'view': 'exit'},
            'YANDEX.REJECT': {'view': 'exit'},
        },
    },
    'ask': {
        'text': ('Скажи, каким словом называют ', 'Попробуй угадать, как называют '),
        'tts': ('Скажи, каким словом называют ', 'Попробуй угадать, как называют '),  # Собирать разметку по частям!
        'text1': '%short_text%',
        'tts1': '%short_text%',  # Сделать разметку!
        'text2': ".",
        'tts2': "",
        'rtext': 'Выбери: это ',  # Текст для переспроса
        'rtts': 'Выбери: это ',  # Сделать разметку?
        'rtext1': '%word_list%',  # Текст для переспроса
        'rtts1': '%word_list%',  # Сделать разметку?
        'butt': (),
        'ans': {
            '%corr%': {'view': 'correct'},
            '%wrong%': {'view': 'wrong'},
            'end_game': {'view': 'exit'},
            'YANDEX.REJECT': {'view': 'exit'},

        },
    },
    'correct': {
        'text': ('Верно!\n\n', 'Ты прав!\n\n'),
        'tts': ('Верно!', 'Ты прав!'),  # Собирать разметку по частям!
        'text1': '%word%',
        'tts1': '%word%',
        'text2': " - правильный ответ. Добавляю тебе три балла.",
        'tts2': " - правильный ответ. Добавляю тебе три балла.",  # Собирать разметку по частям!
        'rtext': f'Играем дальше?',  # Текст для переспроса
        'rtts': f'Играем дальше?',  # Сделать разметку!
        'butt': ('Играем', 'Выйти'),
        'ans': {
            'start_game': {'view': 'ask'},
            'YANDEX.CONFIRM': {'view': 'ask'},
            'end_game': {'view': 'exit'},
            'YANDEX.REJECT': {'view': 'exit'},
        },
        'count_score': 3,
    },
    'wrong': {
        'text': ('Не совсем верно. Правильный ответ ',
                 'В этот раз не получилось. Правильный ответ '),
        'tts': ('Не совсем верно. - Правильный ответ -', 'В этот раз не получилось. - Правильный ответ -'),
        'text1': '%word%',
        'tts1': '%word%',
        'text2': "%minus_score%",
        'tts2': "%minus_score%",  # Собирать разметку по частям!
        'rtext': f'Попробуем Другое слово?',  # Текст для переспроса
        'rtts': f'Попробуем другое слово?',  # Сделать разметку!
        'butt': ('Другое слово', 'Выйти'),
        'ans': {
            'start_game': {'view': 'ask'},
            'YANDEX.CONFIRM': {'view': 'ask'},
            'end_game': {'view': 'exit'},
            'YANDEX.REJECT': {'view': 'exit'},
        },
        'pref_choice': ('Не совсем верно.', 'В этот раз не получилось.'),
        'count_score': -1,
    },
    'exit': {
        'text': 'Спасибо за игру! В твоей копилке ',
        'tts': 'Спасибо за игру! В твоей копилке ',  # Собирать разметку по частям!
        'text1': '%scores%',
        'tts1': '%scores%',  # Сделать разметку!
        'text2': '%балл%',
        'tts2': '%балл%',  # Сделать разметку!
        'rtext': ('Хорошего дня!', 'Хорошего вечера!'),  # Выбор по текущему времени?
        'rtts': ('Хорошего дня!', 'Хорошего вечера!'),  # Сделать разметку!
        'end_session': True,
    },
    'stop': {
        'text': 'Услышимся!',
        'tts': 'Усл+ышимся!',
        'end_session': True
    },
    'scores': {
        'text': 'В твоей копилке ',
        'tts': 'В твоей копилке ',  # Сделать разметку!
        'text1': '%scores%',
        'tts1': '%scores%',  # Сделать разметку!
        'text2': '%балл%',
        'tts2': '%балл%',  # Сделать разметку!
        'rtext': 'Вернуться в игру?',  # Текст для переспроса
        'rtts': 'Вернуться в игру?',  # Сделать разметку!
        'butt': ('Вернуться в игру', 'Выйти'),
        'ans': {
            'return': {'view': 'return'},
            'YANDEX.CONFIRM': {'view': 'return'},
            'YANDEX.BOOK.NAVIGATION.PREVIOUS': {'view': 'return'},
            'end_game': {'view': 'exit'},
            'YANDEX.REJECT': {'view': 'exit'},
        },
    },
    'help': {
        'text': '''Ты всегда можешь сказать Хватит, чтобы немедленно выйти из навыка, или Повтори, чтобы я повторил.\
        \n\nМожно спросить Баллы в копилке, чтобы узнать свои накопленные баллы, или Рейтинг, чтобы узнать рейтинг лучших игроков.\
        \n\nЕсли ты выберешь Вернуться в игру, то продолжишь играть с того же места.''',
        'tts': '''Ты всегда можешь сказать Хватит, чтобы немедленно выйти из навыка, или Повтори, чтобы я повторил. 
        Можно спросить Баллы в копилке, чтобы узнать свои накопленные баллы, или Рейтинг, чтобы узнать рейтинг лучших игроков. 
        Если ты выберешь Вернуться в игру, то продолжишь играть с того же места.''',  # Сделать разметку!
        'rtext': '\nМне Повторить или Вернуться в игру?',  # Текст для переспроса
        'rtts': 'sil<[300]> Мне Повторить или - Вернуться в игру?',  # Сделать разметку!
        'butt': ('Вернуться в игру', 'Повтори', 'Выйти'),
        'ans': {
            'return': {'view': 'return'},
            'YANDEX.BOOK.NAVIGATION.PREVIOUS': {'view': 'return'},
            'end_game': {'view': 'exit'},
            'YANDEX.REJECT': {'view': 'exit'},
        },
    },
    'can_you': {
        'text': '''Я могу сыграть с тобой в игру Угадай АйТи слово. Я дам короткое описание слова, а ты по описанию выберешь правильный ответ.\
        \n\nЗа каждый правильный ответ ты получишь 3 балла, а за неправильный ответ потеряешь 1 балл.\
        \n\nЯ храню твои баллы в копилке до конца игры.''',   # 'и расскажу об успехах других игроков' - пока нет
        'tts': '''Я могу сыграть с тобой в игру Угадай АйТи слово. Я дам короткое описание слова, а ты по описанию 
        выберешь правильный ответ. За каждый правильный ответ ты получишь 3 балла, а за неправильный ответ 
        потеряешь 1 балл. Я храню твои баллы в копилке до конца игры.''',  # 'и расскажу об успехах других игроков' - пока нет
        'rtext': 'Вернемся в игру или Повторить?',  # Текст для переспроса
        'rtts': 'sil<[300]> Вернемся в игру или - Повторить?',  # Сделать разметку!
        'butt': ('Вернуться в игру', 'Повтори', 'Выйти'),
        'ans': {
            'return': {'view': 'return'},
            'YANDEX.BOOK.NAVIGATION.PREVIOUS': {'view': 'return'},
            'end_game': {'view': 'exit'},
            'YANDEX.REJECT': {'view': 'exit'},
        },
    },
    'rules': {
        'text': '''Есть на свете такая каста людей - айтишники. Они вместо писем пишут код, выходят из программы не вставая со стула и говорят на непонятном языке.\
        \n\nСможешь ли ты угадать о чем говорят айтишники? Правила игры простые: я даю описание слова и называю три варианта ответа.\
        \n\nТы выбираешь правильный вариант и получаешь 3 балла в копилку, а если не угадал - минус 1 балл.''',
        'tts': '''Есть на свете такая каста людей - айтишники.  Они вместо писем пишут к+од, -выходят из программы 
         не вставая со стула - и говорят на непонятном языке. Сможешь ли т+ы - угадать о чем говорят айтишники? 
         sil<[300]> Правила игры простые: я даю описание слова и называю три варианта ответа. 
         Ты выбираешь правильный вариант и получаешь 3 балла в коп+илку, а если не угадал - минус 1 б+алл.''',
        'rtext': 'Начнем игру или Повторить?',  # Текст для переспроса
        'rtts': 'sil<[300]> Начнем игру или - Повторить?',  # Сделать разметку!
        'butt': ('Начать игру', 'Повтори', 'Выйти'),
        'ans': {
            'start_game': {'view': 'ask'},
            'YANDEX.CONFIRM': {'view': 'ask'},
            'end_game': {'view': 'exit'},
            'YANDEX.REJECT': {'view': 'exit'},
        },
    },
}
