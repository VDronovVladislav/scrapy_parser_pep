# Проект парсинга PEP - scrapy_parser_pep
## Описание

Приоложение предназначено для парсинга актуальной информации о PEP python.

## Стек:
Scrapy, aiohttp.
### Парсер выполняет функции:
- Собирает информацию обо всех документах pep (Номер, Название, Статус).
- Считает количество PEP в каждом статусе и общее количество PEP и сохраняет результат в табличном виде.

## Установка:
Клонировать репозиторий и перейти в него в командной строке:
```sh
git@github.com:VDronovVladislav/scrapy_parser_pep.git
cd scrapy_parser_pep
```
Cоздать и активировать виртуальное окружение:
```sh
python -m venv env
```
* Если у вас Linux/macOS

```
source venv/bin/activate

```

* Если у вас windows

```
source venv/Scripts/activate

```
Установить зависимости из файла requirements.txt:
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Использование:
Команду необходимо вводить в терминале.
Данная команда создаст два файла в директории results/
- Файл со всеми PEP, их номер/название/статус/
- Файл с количеством PEP в каждом статусе и общим количеством.
```sh
scrapy crawl pep
```
