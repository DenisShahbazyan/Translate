from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSettings
from ui.Settings import Ui_MainWindow


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class DataSettings(Singleton):
    APP_NAME: str = 'Translator'
    COMPANY_NAME: str = 'Education'
    hotkey_show_hide: str = 'Alt + F2'
    hotkey_show_paste: str = 'Alt + F3'


class SettingsWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setup()

    def setup(self):
        self.__events()

    def __events(self):
        self.apply.clicked.connect(self.save_settings)

    def save_settings(self):
        ds = DataSettings()
        settings = QSettings(ds.APP_NAME, ds.COMPANY_NAME)
        settings.setValue('APP_NAME', ds.APP_NAME)

        hotkey_show_hide = self.show_hide.keySequence().toString()
        ds.hotkey_show_hide = hotkey_show_hide.replace('+', ' + ')
        settings.setValue('hotkey_show_hide', ds.hotkey_show_hide)

        hotkey_show_paste = self.show_paste.keySequence().toString()
        ds.hotkey_show_paste = hotkey_show_paste.replace('+', ' + ')
        settings.setValue('hotkey_show_paste', ds.hotkey_show_paste)
