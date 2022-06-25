import keyboard


class Hotkey:
    """Горячие клавиши для приложения.
    """

    def __init__(self, window, app) -> None:
        keyboard.add_hotkey(
            'Alt + F2',
            lambda: (window.hide(), app.exec_()) if window.isVisible(
            ) else (window.show(), window.raise_(), window.activateWindow())
        )
