import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtCore import Qt

from design import Ui_MainWindow
from hotkey import Hotkey
from thread import TranslateThread, PasteThread


class Window(QMainWindow, Ui_MainWindow):
    LANGUAGES = {
        'Auto': 'auto',
        'English': 'en',
        'Russian': 'ru',
        'Chinese': 'zh',
        'Arabic': 'ar',
        'French': 'fr',
        'German': 'de',
        'Spanish': 'es',
        'Portuguese': 'pt',
        'Italian': 'it',
        'Japanese': 'ja',
        'Korean': 'ko',
        'Greek': 'el',
        'Dutch': 'nl',
        'Hindi': 'hi',
        'Turkish': 'tr',
        'Malay': 'ms',
        'Thai': 'th',
        'Vietnamese': 'vi',
        'Indonesian': 'id',
        'Hebrew': 'he',
        'Polish': 'pl',
        'Mongolian': 'mn',
        'Czech': 'cs',
        'Hungarian': 'hu',
        'Estonian': 'et',
        'Bulgarian': 'bg',
        'Danish': 'da',
        'Finnish': 'fi',
        'Romanian': 'ro',
        'Swedish': 'sv',
        'Slovenian': 'sl',
        'Persian/farsi': 'fa',
        'Bosnian': 'bs',
        'Serbian': 'sr',
        'Fijian': 'fj',
        'Filipino': 'tl',
        'Haitiancreole': 'ht',
        'Catalan': 'ca',
        'Croatian': 'hr',
        'Latvian': 'lv',
        'Lithuanian': 'lt',
        'Urdu': 'ur',
        'Ukrainian': 'uk',
        'Welsh': 'cy',
        'Tahiti': 'ty',
        'Tongan': 'to',
        'Swahili': 'sw',
        'Samoan': 'sm',
        'Slovak': 'sk',
        'Afrikaans': 'af',
        'Norwegian': 'no',
        'Bengali': 'bn',
        'Malagasy': 'mg',
        'Maltese': 'mt',
        'Queretaro otomi': 'otq',
        'Klingon/tlhingan hol': 'tlh',
        'Gujarati': 'gu',
        'Tamil': 'ta',
        'Telugu': 'te',
        'Punjabi': 'pa',
        'Amharic': 'am',
        'Azerbaijani': 'az',
        'Bashkir': 'ba',
        'Belarusian': 'be',
        'Cebuano': 'ceb',
        'Chuvash': 'cv',
        'Esperanto': 'eo',
        'Basque': 'eu',
        'Irish': 'ga',
        'Emoji': 'emj',
    }

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        Hotkey(self)
        self.setup()

    def setup(self):
        """Конструктор, вынес в отдельный метод, чтобы не захлямлять.
        """
        self.__resize_window()
        self.__set_comboBox()
        self.__signals()

    def __resize_window(self):
        """Задаю стартовое соотношение строн приложения.
        """
        monitor = QDesktopWidget().availableGeometry()
        self.resize(monitor.width() // 3 * 2, monitor.height() // 4 * 2)

    def __set_comboBox(self):
        """Начальные настройки для comboBox'ов.
        """
        self.lang_from.addItems(self.LANGUAGES.keys())
        self.lang_from.setCurrentText('Auto')

        self.lang_to.addItems(self.LANGUAGES.keys())
        self.lang_to.setCurrentText('English')

    def __signals(self):
        """Сигналы.
        """
        self.change_lang.clicked.connect(self.push_change_lang)

        self.lang_to.currentTextChanged.connect(self.translate_in_thr)

        self.text_from.blockCountChanged.connect(self.translate_in_thr)
        self.trans_thr = TranslateThread(self)
        self.trans_thr.finish_signal.connect(self.translate_from_thr)

    def show_hide_window(self):
        if self.isVisible():
            self.hide()
        else:
            self.show(),
            self.raise_(),
            self.activateWindow(),
            self.setWindowFlag(
                Qt.WindowStaysOnTopHint,
                Qt.X11BypassWindowManagerHint
            ),
            self.show()

    def push_change_lang(self):
        """Смена языков по сигналу и смена текстов местами. При смене тексов
        перевод начинается автоматически.
        """
        lang_from = self.lang_from.currentText()
        lang_to = self.lang_to.currentText()
        self.lang_from.setCurrentText(lang_to)
        self.lang_to.setCurrentText(lang_from)

        text_from = self.text_from.toPlainText()
        text_to = self.text_to.toPlainText()
        self.text_from.setPlainText(text_to)
        self.text_to.setPlainText(text_from)

    def translate_in_thr(self):
        """Передача данных в поток.
        """
        self.trans_thr.text = self.text_from.toPlainText()
        self.trans_thr.lang_from = self.LANGUAGES[self.lang_from.currentText()]
        self.trans_thr.lang_to = self.LANGUAGES[self.lang_to.currentText()]

        self.trans_thr.start()

    def translate_from_thr(self, text):
        """Получение данных из потока.
        """
        self.text_to.setPlainText(text)

    def paste_in_thr(self):
        """Отправка данных в поток / Создание потока.
        """
        self.paste_thr = PasteThread(self)
        self.paste_thr.finish_signal.connect(self.paste_from_thr)

        self.paste_thr.start()

    def paste_from_thr(self, text):
        """Получение данных из потока.
        """
        self.text_from.setPlainText(text)
        self.translate_in_thr()
        if not self.isVisible():
            self.show(),
            self.raise_(),
            self.activateWindow(),
            self.setWindowFlag(
                Qt.WindowStaysOnTopHint,
                Qt.X11BypassWindowManagerHint
            ),
            self.show()


def main():
    """Инициализация приложения.
    """
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
