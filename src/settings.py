from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSettings
from ui.Settings import Ui_MainWindow


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class DataSettings(Singleton):
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
    APP_NAME: str = 'Translator'
    COMPANY_NAME: str = 'Education'
    hotkey_show_hide: str = 'Alt + F2'
    hotkey_show_paste: str = 'Alt + F3'
    fast_lang_1: str = 'Auto'
    fast_lang_2: str = 'Auto'


class SettingsWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setup()

    def setup(self):
        self.ds = DataSettings()

        self.__load_settings()
        self.__events()

    def __load_settings(self):
        self.show_hide.setKeySequence(
            self.ds.hotkey_show_hide.replace(' ', ''))
        self.show_paste.setKeySequence(
            self.ds.hotkey_show_paste.replace(' ', ''))

        self.fast_lang_1.addItems(self.ds.LANGUAGES.keys())
        self.fast_lang_1.setCurrentText(self.ds.fast_lang_1)
        self.fast_lang_2.addItems(self.ds.LANGUAGES.keys())
        self.fast_lang_2.setCurrentText(self.ds.fast_lang_2)

    def __events(self):
        self.apply.clicked.connect(self.save_settings)

    def save_settings(self):
        settings = QSettings(self.ds.APP_NAME, self.ds.COMPANY_NAME)
        settings.setValue('APP_NAME', self.ds.APP_NAME)

        hotkey_show_hide = self.show_hide.keySequence().toString()
        hotkey_show_hide = hotkey_show_hide.replace('+', ' + ')
        settings.setValue('hotkey_show_hide', hotkey_show_hide)

        hotkey_show_paste = self.show_paste.keySequence().toString()
        hotkey_show_paste = hotkey_show_paste.replace('+', ' + ')
        settings.setValue('hotkey_show_paste', hotkey_show_paste)

        settings.setValue('fast_lang_1', self.fast_lang_1.currentText())
        settings.setValue('fast_lang_2', self.fast_lang_2.currentText())
