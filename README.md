# Проект парсинга PEP - scrapy_parser_pep
## 1. Описание

Приоложение предназначено для парсинга актуальной информации о PEP python.
### Парсер выполняет функции:
- Собирает информацию обо всех документах pep (Номер, Название, Статус).
- Считает количество PEP в каждом статусе и общее количество PEP и сохраняет результат в табличном виде.

## 2. Установка:
Клонировать репозиторий и перейти в него в командной строке:
```sh
git@github.com:VDronovVladislav/scrapy_parser_pep.git
cd scrapy_parser_pep
```
Cоздать и активировать виртуальное окружение:
```sh
python -m venv env
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Использование:
Команду необходимо вводить в терминале.
Данная команда создаст два файла в директории results/
- Файл со всеми PEP, их номер/название/статус/
- Файл с количеством PEP в каждом статусе и общим количеством.
```sh
scrapy crawl pep
```
