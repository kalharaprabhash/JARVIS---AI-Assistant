import ctypes
import subprocess
import pyperclip
import screen_brightness_control as sbc


def volume_up():
    for _ in range(5):
        ctypes.windll.user32.keybd_event(
            0xAF, 0, 0, 0
        )


def volume_down():
    for _ in range(5):
        ctypes.windll.user32.keybd_event(
            0xAE, 0, 0, 0
        )


def volume_mute():
    ctypes.windll.user32.keybd_event(
        0xAD, 0, 0, 0
    )


def brightness_up():
    try:
        current = sbc.get_brightness()[0]
        sbc.set_brightness(
            min(current + 10, 100)
        )
    except Exception:
        pass


def brightness_down():
    try:
        current = sbc.get_brightness()[0]
        sbc.set_brightness(
            max(current - 10, 0)
        )
    except Exception:
        pass


def read_clipboard():
    try:
        text = pyperclip.paste()

        if text:
            return text

        return "Clipboard is empty."

    except Exception:
        return "Unable to read clipboard."


def take_screenshot():
    subprocess.Popen(
        "explorer.exe ms-screenclip:"
    )


def minimize_window():
    ctypes.windll.user32.keybd_event(
        0x5B, 0, 0, 0
    )
    ctypes.windll.user32.keybd_event(
        0x44, 0, 0, 0
    )
    ctypes.windll.user32.keybd_event(
        0x44, 0, 2, 0
    )
    ctypes.windll.user32.keybd_event(
        0x5B, 0, 2, 0
    )


def maximize_window():
    ctypes.windll.user32.keybd_event(
        0x5B, 0, 0, 0
    )
    ctypes.windll.user32.keybd_event(
        0x55, 0, 0, 0
    )
    ctypes.windll.user32.keybd_event(
        0x55, 0, 2, 0
    )
    ctypes.windll.user32.keybd_event(
        0x5B, 0, 2, 0
    )


def close_window():
    ctypes.windll.user32.keybd_event(
        0x12, 0, 0, 0
    )
    ctypes.windll.user32.keybd_event(
        0x73, 0, 0, 0
    )
    ctypes.windll.user32.keybd_event(
        0x73, 0, 2, 0
    )
    ctypes.windll.user32.keybd_event(
        0x12, 0, 2, 0
    )