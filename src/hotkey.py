import keyboard
from PyQt5.QtCore import Qt


class Hotkey:
    """Горячие клавиши для приложения.
    """

    def __init__(self, window, app) -> None:
        keyboard.add_hotkey(
            'Alt + F2',
            lambda: (
                window.hide()
            )
            if window.isVisible(
            ) else (
                window.show(),
                window.raise_(),
                window.activateWindow(),
                window.setWindowFlag(
                    Qt.WindowStaysOnTopHint,
                    Qt.X11BypassWindowManagerHint
                ),
                window.show()
            )
        )
