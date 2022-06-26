import keyboard


class Hotkey:
    """Горячие клавиши для приложения.
    """

    def __init__(self, window) -> None:
        keyboard.add_hotkey(
            'Alt + F2',
            lambda: window.show_hide_window()
        )
        keyboard.add_hotkey(
            'Alt + F3',
            lambda: window.paste_in_thr()
        )
