import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

from design import Ui_MainWindow
from hotkey import Hotkey
from thread import TranslateThread


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

        self.setup()

    def setup(self):
        """Конструктор, вынес в отдельный метод, чтобы не захлямлять.
        """
        self.resize_window()
        self.set_comboBox()
        self.events()

    def resize_window(self):
        """Задаю стартовое соотношение строн приложения.
        """
        monitor = QDesktopWidget().availableGeometry()
        self.resize(monitor.width() // 3 * 2, monitor.height() // 4 * 2)

    def set_comboBox(self):
        """Начальные настройки для comboBox'ов.
        """
        self.lang_from.addItems(self.LANGUAGES.keys())
        self.lang_from.setCurrentText('Auto')

        self.lang_to.addItems(self.LANGUAGES.keys())
        self.lang_to.setCurrentText('English')

    def events(self):
        """Сигналы.
        """
        self.change_lang.clicked.connect(self.push_change_lang)

        self.lang_to.currentTextChanged.connect(self.in_thread)

        self.text_from.blockCountChanged.connect(self.in_thread)
        self.thr = TranslateThread(self)
        self.thr.finish_signal.connect(self.from_thred)

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

    def in_thread(self):
        """Передача данных в поток.
        """
        self.thr.text = self.text_from.toPlainText()
        self.thr.lang_from = self.LANGUAGES[self.lang_from.currentText()]
        self.thr.lang_to = self.LANGUAGES[self.lang_to.currentText()]
        self.thr.start()

    def from_thred(self, text):
        """Получение данных из потока.
        """
        self.text_to.setPlainText(text)


def main():
    """Инициализация приложения.
    """
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    Hotkey(window, app)
    app.exec_()


if __name__ == '__main__':
    main()
