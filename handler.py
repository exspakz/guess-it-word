from sdk import ViewDict
from dict import views_dict
from data import data, DataSet


choice_imm = {
    ('new',): {'view': 'hi'},
    ('stop',): {'view': 'stop'},
    ('repeat', 'YANDEX.REPEAT'): {'view': 'repeat'},
    ('scores',): {'view': 'scores'},
    ('help', 'YANDEX.HELP'): {'view': 'help'},
    ('can_you',): {'view': 'can_you'},
}


def scores_count(user_storage):
    if user_storage['prev_view'] == 'ask':
        if user_storage['view'] == 'correct' or user_storage['view'] == 'wrong':
            user_storage['questions_set'].discard(user_storage['word_received'])
            if not user_storage['questions_set']:
                user_storage['questions_set'] = DataSet
            if user_storage['scores_bank'] + user_storage['entity'].get('count_score') >= 0:
                user_storage['scores_bank'] += user_storage['entity'].get('count_score')
    return user_storage


def end_session(response, v):
    response.set_text(f"{v.get('text')}\n\n{v.get('rtext')}")
    response.set_tts(f"{v.get('tts')}\n\n{v.get('rtts')}")
    response.set_end_session(True)
    user_storage = {}
    return response, user_storage


def if_token_del_intent(token, intent, request):
    if token in request.tokens and intent in request.intents:
        ls = request.intents
        ls.remove('YANDEX.REJECT')
        request.intents = ls
    return request


def handle_dialog(request, response, user_storage):
    if request.is_new_session or user_storage is None:
        user_storage = {'view': 'new'}
        user_storage['entity'] = views_dict.get(user_storage.get('view'))
        user_storage['prev_entity'] = {}
        user_storage['scores_bank'] = 0
        user_storage['questions_set'] = DataSet.copy()
        user_storage['mistake_count'] = 0
        request.intents = ['new']

    choice = choice_imm.copy()
    choice.update(user_storage.get('entity').get('ans', ''))
    print('choice = ', choice)

    request = if_token_del_intent('другое', 'YANDEX.REJECT', request)

    if user_storage['view'] == 'ask' and 'question_reply' in request.intents:
        for w in (user_storage['question'], user_storage['wrong_1'], user_storage['wrong_2']):
            if data.get(w).get('value') == request.value:
                user_storage['word_received'] = w
        curr_views = [v for u, v in choice.items() if request.value in u]
    else:
        curr_views = [v for u, v in choice.items() for i in request.intents if i in u]
    curr_views = list(set([v.get('view') for v in curr_views]))

    if len(curr_views) == 1:
        user_storage['mistake_count'] = 0
        view = curr_views[0]
        if view != 'repeat':
            if view == 'return':
                user_storage['view'] = 'ask'   # не идти в ответы
                view_dict = ViewDict(views_dict.get('ask'))
                user_storage['entity'].clear()
                (
                    user_storage['entity'],
                    user_storage['question'],
                    user_storage['wrong_1'],
                    user_storage['wrong_2']
                ) = view_dict.compile_view(user_storage)
            else:
                if user_storage.get('view') not in ('scores', 'help', 'can_you'):
                    user_storage['prev_view'] = user_storage.get('view')
                    user_storage['prev_entity'].clear()
                    user_storage['prev_entity'] = user_storage.get('entity').copy()
                user_storage['view'] = view
                view_dict = ViewDict(views_dict.get(user_storage.get('view')))
                user_storage['entity'].clear()
                (user_storage['entity'],
                 user_storage['question'],
                 user_storage['wrong_1'],
                 user_storage['wrong_2']) = view_dict.compile_view(user_storage)

        user_storage = scores_count(user_storage)

        if user_storage.get('entity').get('end_session'):
            return end_session(response, user_storage.get('entity'))

        response.set_text(f"{user_storage.get('entity').get('text')}\n\n{user_storage.get('entity').get('rtext')}")
        response.set_tts(f"{user_storage.get('entity').get('tts')} sil<[300]> {user_storage.get('entity').get('rtts')}")
        buttons = [{'title': b, 'hide': True} for b in user_storage.get('entity').get('butt', '')]
        response.set_buttons(buttons)

        response.set_events({'name': user_storage.get('view')})

        print('собрали response = ', response)

        return response, user_storage

    else:
        user_storage['mistake_count'] += 1
        print("\nreceived curr_views = ", curr_views, '\n____________')
        if user_storage['mistake_count'] == 1:
            response.set_text(f"Не совсем тебя понял.\n\n{user_storage.get('entity').get('rtext')}")
            response.set_tts(f"Не совсем тебя понял. sil<[300]> {user_storage.get('entity').get('rtts')}")
            buttons = [{'title': b, 'hide': True} for b in user_storage.get('entity').get('butt', '')]
            response.set_buttons(buttons)
        elif user_storage['mistake_count'] == 2:
            response.set_text(f"Опять непонятно. Определись, пожалуйста.\\n\n{user_storage.get('entity').get('rtext')}")
            response.set_tts(f"Опять непонятно. Определись, пожалуйста. sil<[300]> {user_storage.get('entity').get('rtts')}")
            buttons = [{'title': b, 'hide': True} for b in user_storage.get('entity').get('butt', '')]
            response.set_buttons(buttons)
        elif user_storage['mistake_count'] == 3:
            response.set_text(f"""Что-то идет не так. \nНапомню о чем мы говорили.\
            \n\n{user_storage.get('entity').get('text')}\n\n{user_storage.get('entity').get('rtext')}""")
            response.set_tts(f"""Что-то идет не так. \nНапомню о чем мы говорили.\ 
            sil<[300]> {user_storage.get('entity').get('text')}\n\n{user_storage.get('entity').get('rtext')}""")
            buttons = [{'title': b, 'hide': True} for b in user_storage.get('entity').get('butt', '')]
            response.set_buttons(buttons)
        else:
            response.set_text(f"""Сегодня, наверное, не мой день! \nДавай попробуем в другой раз.\n\nУдачи!""")
            response.set_tts(f"""Сегодня - наверное - не мой день! \nДавай попробуем в другой раз. sil<[300]> Удачи!""")
            response.set_end_session(True)
            user_storage = {}

        response.set_events(
            {
                'name': 'mistake_handling_intents',
                'value': {'command': request.command},
            }
        )

        print('собрали response = ', response)

        return response, user_storage
