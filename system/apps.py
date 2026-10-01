import os
import subprocess
import webbrowser
import psutil


def open_google():
    webbrowser.open("https://www.google.com")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def open_chrome():
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            return

    webbrowser.open("https://www.google.com")


def open_notepad():
    subprocess.Popen("notepad.exe")


def open_calculator():
    subprocess.Popen("calc.exe")


def open_paint():
    subprocess.Popen("mspaint.exe")


def open_downloads():
    os.startfile(
        os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )
    )


def open_desktop():
    os.startfile(
        os.path.join(
            os.path.expanduser("~"),
            "Desktop"
        )
    )


def open_documents():
    os.startfile(
        os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )
    )


def open_pictures():
    os.startfile(
        os.path.join(
            os.path.expanduser("~"),
            "Pictures"
        )
    )


def open_videos():
    os.startfile(
        os.path.join(
            os.path.expanduser("~"),
            "Videos"
        )
    )


def get_running_apps():
    apps = []

    for process in psutil.process_iter(["name"]):
        try:
            name = process.info["name"]

            if name and name.lower().endswith(".exe"):
                apps.append(name)

        except Exception:
            pass

    return sorted(set(apps))