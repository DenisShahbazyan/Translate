from PyQt5.QtCore import QThread, pyqtSignal
import translators as ts
import keyboard
import pyautogui
from win32clipboard import OpenClipboard, GetClipboardData, CloseClipboard


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


class PasteThread(QThread):
    """Создание потока для вставки скопированного текста.
    """
    finish_signal = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__()

    def run(self):
        while True:
            if not keyboard.is_pressed('Alt'):
                pyautogui.hotkey('ctrl', 'c')
                break
        OpenClipboard()
        text = GetClipboardData()
        CloseClipboard()
        self.finish_signal.emit(text)
