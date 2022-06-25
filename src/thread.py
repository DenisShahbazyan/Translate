from PyQt5.QtCore import QThread, pyqtSignal
import translators as ts


class TranslateThread(QThread):
    """Создание потока для перевода.
    """
    finish_signal = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__()
        self.text = ''
        self.lang_from = ''
        self.lang_to = ''

    def run(self):
        text = ts.google(self.text, self.lang_from, self.lang_to)
        self.finish_signal.emit(text)
