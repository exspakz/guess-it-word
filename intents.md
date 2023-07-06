## can_you
```
$Canyou:
    %lemma
    что (ты)* (умеешь|можешь)
root:
    .* $Canyou .*
filler:
    алиса
```

## end_game
```
slots:
    game:
        source: $Game
        type: Game
$End:
    %lemma
    выйти (из)*
    закончить
    остановить
    надоело
    домой
    выход
    уйти
    хватит .* играть
root:
    [($End)+ ($Game)*]
filler:
    алиса
```

## help
```
$Help:
    %lemma
    помоги
    помощь
root:
    .* $Help .*
filler:
    алиса
```

## new
```
root:
    Угадай АйТи слово
    mmm test
```

## question_reply
```
slots:
    term:
        source: $Term
        type: Term
root:
    .* $Term .*
filler:
    алиса
    попробуем
    давай
    ну
    возможно
    вероятно
    может
    если
    допустим
    допустимо
    тоже
    или нет
    вроде
    думаю
    это
```

## repeat
```
$Repeat:
    %lemma
    повтор
    повтори
    [не понял (ничего)*]
root:
    $Repeat
filler:
    алиса
```

## return
```
slots:
    game:
        source: $Game
        type: Game
$Return:
    %lemma
    вернуться
    назад
    .* в игру
root:
    [($Return)+ ($Game)*]
filler:
    алиса
    в
```

## rules
```
slots:
    rules:
        source: $Rules
        type: Rules
$Tell:
    %lemma
    скажи
    расскажи
    объясни
root:
    [($Tell)* ($Rules)+] | [($Tell)+ ($Rules)*]
filler:
    алиса
    о
    про
```

## scores
```
slots:
    scores:
        source: $Scores
        type: Scores
    bank:
        source: $Bank
        type: Bank
root:
    [($Scores)+ ($Bank)*] | [($Scores)* ($Bank)+]
filler:
    алиса
    в
    с
    на
    сколько
    у меня
    какой
```

## start_game
```
slots:
    game:
        source: $Game
        type: Game
    word:
        source: $Word
        type: Word
$Start:
    %lemma
    давай
    начать
    начинать
    начинаться
    угадать
    спрашивать
    сыграем
    поиграем
    жги
    старт
    стартовать
    игра
    играть
    продолжить
root:
    [($Start)+ ($Game)* ($Word)*] | [($Start)* ($Game)+ | ($Word)+]
filler:
    алиса
    еще
```

## stop
```
$Stop:
    %lemma
    стоп
    хватит
root:
    $Stop
filler:
    алиса
```