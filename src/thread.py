from PyQt5.QtCore import QThread, pyqtSignal
import translators as ts
import keyboard
import pyautogui
import win32clipboard

from settings import DataSettings


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
        ds = DataSettings()
        key = ds.hotkey_show_paste.split('+')[0].strip()
        while True:
            if not keyboard.is_pressed(key):
                pyautogui.hotkey('ctrl', 'c')
                break
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        self.finish_signal.emit(text)
