import json
from random import sample, choice
from data import data, DataSet


class AliceRequest:
    def __init__(self, request_dict):
        self._request_dict = request_dict
        self._intents = request_dict.get('request').get('nlu').get('intents')

    @property
    def version(self):
        return self._request_dict.get('version')

    @property
    def session(self):
        return self._request_dict.get('session')

    @property
    def user_id(self):
        return self.session.get('user_id')

    @property
    def is_new_session(self):
        return bool(self.session.get('new'))

    @property
    def intents(self):
        return list(self._intents)

    @intents.setter
    def intents(self, value):
        self._intents = value

    @property
    def value(self):
        return self._request_dict.get('request').get('nlu').get('intents').get('question_reply').get('slots') \
           .get('term').get('value')

    @property
    def command(self):
        return self._request_dict.get('request').get('command')

    def __str__(self):
        return str(self._request_dict)


class AliceResponse:
    def __init__(self, alice_request):
        self._response_dict = {
            'version': alice_request.version,
            'session': alice_request.session,
            'response': {
                "end_session": False,
            },
            'analytics': {
                'events': []
            },
        }

    def dumps(self):
        return json.dumps(
            self._response_dict,
            ensure_ascii=False,
            indent=2,
        )

    def set_text(self, text):
        self._response_dict['response']['text'] = text[:1024]

    def set_tts(self, tts):
        self._response_dict['response']['tts'] = tts[:1024]

    def set_buttons(self, buttons):
        self._response_dict['response']['buttons'] = buttons

    def set_end_session(self, flag):
        self._response_dict['response']['end_session'] = flag

    def set_events(self, event):
        self._response_dict['analytics']['events'].append(event)

    def __str__(self):
        return self.dumps()


class ViewDict:
    def __init__(self, curr_view):
        self.text = curr_view.get('text', '')
        self.tts = curr_view.get('tts', '')
        self.text1 = curr_view.get('text1', '')
        self.tts1 = curr_view.get('tts1', '')
        self.text2 = curr_view.get('text2', '')
        self.tts2 = curr_view.get('tts2', '')
        self.rtext = curr_view.get('rtext', '')
        self.rtts = curr_view.get('rtts', '')
        self.rtext1 = curr_view.get('rtext1', '')
        self.rtts1 = curr_view.get('rtts1', '')
        self.butt = curr_view.get('butt', '')
        self.ans = curr_view.get('ans', {}).copy()
        self.end_session = curr_view.get('end_session', None)
        self.count_score = curr_view.get('count_score', None)
        self.question = ''
        self.wrong_1, self.wrong_2 = '', ''

    def compile_view(self, user_storage):

        compiled_view = {}

        if isinstance(self.text, tuple):
            self.text = choice(self.text)
            self.tts = self.text
        if self.text1 == '%scores%':
            self.text1 = user_storage.get('scores_bank')
            self.tts1 = self.text1
        elif self.text1 == '%word%':
            self.text1 = data.get(user_storage.get('question')).get('word').capitalize()
            self.tts1 = self.text1
        elif self.text1 == '%short_text%':
            self.question = choice(list(user_storage.get('questions_set')))
            self.text1 = data.get(self.question).get('short_text')
            self.tts1 = self.text1
            ds = DataSet.copy()
            ds.discard(self.question)
            self.wrong_1, self.wrong_2 = sample(list(ds), k=2)
            self.butt = sample([data.get(self.question).get('word'),
                                data.get(self.wrong_1).get('word'), data.get(self.wrong_2).get('word')], k=3)
            self.rtext1 = f"{self.butt[0]}, {self.butt[1]} или {self.butt[2]}"
            self.rtts1 = f"- {self.butt[0]}, - {self.butt[1]} или - {self.butt[2]}"
            self.ans[f"{data.get(self.question).get('value')}"] = self.ans.get('%corr%')
            self.ans[(f"{data.get(self.wrong_1).get('value')}",
                      f"{data.get(self.wrong_2).get('value')}")] = self.ans.get('%wrong%')

        if self.text2 == '%minus_score%':
            if user_storage.get('scores_bank') + self.count_score >= 0:
                self.text2 = '. \n\nМинус один балл.'
                self.tts2 = ' - Минус один балл.'
            else:
                self.text2 = '. \n\nУ тебя пока ноль баллов.'
                self.tts2 = ' - У тебя пока ноль баллов.'
        elif self.text2 == '%балл%':
            if user_storage.get('scores_bank') % 10 == 1 \
                    and (user_storage.get('scores_bank') // 10) % 10 != 1:
                self.text2 = ' балл.'
            elif user_storage.get('scores_bank') % 10 in (2, 3, 4) \
                    and (user_storage.get('scores_bank') // 10) % 10 != 1:
                self.text2 = ' балла.'
            else:
                self.text2 = ' баллов.'
            self.tts2 = self.text2

        compiled_view['text'] = f"{self.text}{self.text1}{self.text2}"
        compiled_view['tts'] = f"{self.tts}{self.tts1}{self.tts2}"

        if isinstance(self.rtext, tuple):
            self.rtext = choice(self.rtext)
            self.rtts = self.rtext
        compiled_view['rtext'] = f"{self.rtext}{self.rtext1}"
        compiled_view['rtts'] = f"{self.rtts}{self.rtts1}"
        compiled_view['butt'] = self.butt
        compiled_view['ans'] = self.ans

        if self.end_session:
            compiled_view['end_session'] = self.end_session
        if self.count_score:
            compiled_view['count_score'] = self.count_score

        return compiled_view, self.question, self.wrong_1, self.wrong_2

