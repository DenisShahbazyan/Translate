# Переводчик.
### Автор: Денис Шахбазян.

### Перед началом работы:
1. Склонируйте репозиторий.
2. Создайте виртуальное окружение.
3. Установите зависимости ```pip install -r requirements.txt```.
4. Установить библиотеку из папки `data/lib` - это `pywin32` у меня она не установилась через pip.

### Описание:

Desktop переводчик текста для Windows. Может переводить выделенный текст из любого приложения по сочетанию клавиш. 

Внешний вид и функционал как у Google Translate:
<img src="/data/img/Screenshot_1.png" alt="sch" style="max-width: 100%;">

Окно настроек:
<img src="/data/img/Screenshot_2.png" alt="sch" style="max-width: 100%;">
- **Show / Hide Window** - Сочетание клавиш для показа / скрытия окна
- **Show & Paste Text** - Сочетание клавиш для копирования выделенного текста, открытия окна переводчика, вставки выделенного текста в поле для перевода. Перевод отобразиться в соседнем поле.
- **Fast Lang 1 / Fast Lang 2** - Языки для быстрого перевода. Т.е. при переводе текста **Show & Paste Text** переводчик будет определять, на каком языке сам текст **Fast Lang 1** или **Fast Lang 2**. К примеру, если текст на **Fast Lang 1**, то перевод будет в **Fast Lang 2**, и наоборот.

### Инструкция:
- Запуск через файл `main.py`
- Чтобы упаковать в exe, выполнить команду из корня проекта:
```
pyinstaller --onefile --noconsole --name Translate --icon=ui/icon/icon.ico src/main.py
```
- Изменить интерфейс можно через [Qt Designer](https://www.qt.io/). Файлы интерфейса в папке `ui`, иконки в ней же.
### Технологии:

- [Python](https://www.python.org/) 3.10.4
- [PyQt5](https://pypi.org/project/PyQt5/) 5.15.7
- [PyInstaller](https://pypi.org/project/pyinstaller/) 5.1
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) 0.9.53
- [keyboard](https://pypi.org/project/keyboard/) 0.13.5
- [langdetect](https://pypi.org/project/langdetect/) 1.0.9
- [translate-api](https://pypi.org/project/translate-api/) 4.9.5

