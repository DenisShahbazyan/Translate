import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtCore import Qt, QSettings

from settings import DataSettings, SettingsWindow
from ui.MainWindow import Ui_MainWindow
from thread import TranslateThread, PasteThread


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()

    def setup(self):
        """Конструктор, вынес в отдельный метод, чтобы не захлямлять.
        """
        self.__load_settings()
        self.__resize_window()
        self.__set_comboBox()
        self.__signals()

    def __load_settings(self):
        self.ds = DataSettings()
        settings = QSettings(self.ds.APP_NAME, self.ds.COMPANY_NAME)
        app_name = settings.value('APP_NAME')
        if app_name is not None:
            self.ds.hotkey_show_hide = settings.value('hotkey_show_hide')
            self.ds.hotkey_show_paste = settings.value('hotkey_show_paste')
            from hotkey import Hotkey
            Hotkey(self)
            self.ds.fast_lang_1 = settings.value('fast_lang_1')
            self.ds.fast_lang_2 = settings.value('fast_lang_2')

    def __resize_window(self):
        """Задаю стартовое соотношение строн приложения.
        """
        monitor = QDesktopWidget().availableGeometry()
        self.resize(monitor.width() // 3 * 2, monitor.height() // 4 * 2)

    def __set_comboBox(self):
        """Начальные настройки для comboBox'ов.
        """
        self.lang_from.addItems(self.ds.LANGUAGES.keys())
        self.lang_from.setCurrentText('Auto')

        self.lang_to.addItems(self.ds.LANGUAGES.keys())
        self.lang_to.setCurrentText('English')

    def __signals(self):
        """Сигналы.
        """
        self.action.triggered.connect(self.show_window_settings)

        self.change_lang.clicked.connect(self.push_change_lang)

        self.lang_to.currentTextChanged.connect(self.translate_in_thr)

        self.text_from.blockCountChanged.connect(self.translate_in_thr)
        self.trans_thr = TranslateThread(self)
        self.trans_thr.finish_signal.connect(self.translate_from_thr)

    def show_window_settings(self):
        self.__s = SettingsWindow()
        self.__s.show(),
        self.__s.raise_(),
        self.__s.activateWindow(),
        self.__s.setWindowFlag(
            Qt.WindowStaysOnTopHint,
            Qt.X11BypassWindowManagerHint
        ),
        self.__s.show()

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
        self.trans_thr.lang_from = (
            self.ds.LANGUAGES[self.lang_from.currentText()]
        )
        self.trans_thr.lang_to = (
            self.ds.LANGUAGES[self.lang_to.currentText()]
        )

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
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
