import keyboard

from settings import DataSettings


class Hotkey:
    """Горячие клавиши для приложения.
    """

    def __init__(self, window) -> None:
        ds = DataSettings()
        keyboard.add_hotkey(
            ds.hotkey_show_hide,
            lambda: window.show_hide_window()
        )
        keyboard.add_hotkey(
            ds.hotkey_show_paste,
            lambda: window.paste_in_thr()
        )
        keyboard.add_hotkey(
            'Enter',
            lambda: window.translate_in_thr()
        )
