```
entity Term:
    lemma: true
    values:
        id:
            айди
            id
        ip:
            айпи
            ip
        api:
            апи
        authorization:
            авторизация
        benefit:
            бенефит
        benchmark:
            бенчмарк
        backup:
            бэкап
        gestures:
            гестуры
        gradient:
            градиент
        dump:
            дамп
        upload:
            залить
        interpreter:
            интерпретатор
        iterator:
            итератор
        captcha:
            капча
        compilation:
            компиляция
        workaround:
            костыль
        meetup:
            муар
        rollback:
            откат
        parser:
            парсер
        periphery:
            периферия
        fix:
            фиксить
            пофиксить
        review:
            ревью
        repository:
            репозиторий
        software:
            софт
        stack:
            стек
        template:
            темплейт
        hackathon:
            хакатон
        feedback:
            фидбек
            фидбэк
            фитбек
            фитбэк
        usability:
            юзабилити
        hard:
            хард

entity Game:
    lemma: true
    values:
        game:
            игра
            играть

entity Word:
    lemma: true
    values:
        game:
            (другое)+ (слово)* | (другое)* (слово)+

entity Scores:
    lemma: true
    values:
        scores:
            баллы
            очки
            счет

entity Bank:
    lemma: true
    values:
        bank:
            копилка
            банк
            счет

entity Rules:
    lemma: true
    values:
        bank:
            правила
            %negative
            .* правильно
            .* неправильно
```