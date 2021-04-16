# Проектирование и анализ алгоритмов
### Выполнено Шалугиным Евгением гр. 7307

## Что здесь реализовано
1. Сложение двух длинных чисел.
2. Рекурсивный алгоритм бинарного поиска
3. Рекурсивный алгоритм бинарного поиска по ответу
4. Бинарное дерево без балансировки (с поиском следующего по значению узла)
5. Декартово дерево (с поиском следующего по значению узла)
6. Система непересекающихся множеств с помощью леса корневых деревьев

## О структуре проекта
src - папка с реализованными алгоритмами + классами, реализуюшими структуры данных

|__BinSearch.py

|__BinTree.py

|__...


tests - папка с .txt файлами тестов (.in и .out)

|__binary-search

|__binary-tree

|__...


tests.py - скрипт для запуска тестов (тесты запускаются сразу по всем файлам).

## Как запустить тесты 
1. Создаём виртуальное окружение командой `python -m venv venv`
2. Активируем его `/venv/Scripts/activate`
3. Устанавливаем зависимости `pip install -r requirements.txt`
4. Запускаем тесты с помощью команды `python tests.py`

## Структура ответа тестов
Корректность полученного ответа проверяется автоматически.

Сначала на экран выводится название задачи.

Дальше для каждого .in файла выводится результат проверки на совпадение ответа с соответствующим .out файлом.

В случае верного ответа:

:heavy_check_mark:True

иначе:

:x:False

## Примечания
1. Из-за наивной реализации Бинарное дерево падает на последнем тесте из-за слишком большой глубины (это нормально, показывает эффективность декартова дерева)
2. Для тестов используется библиотека tqdm (progress bar) для того, чтобы понимать состояние испольняемой задачи. Из-за этого выводы результатов тестирования могут выводится не с новой строки.
