import os
import time
import subprocess
import threading
import urllib.request
import ctypes

import speech_recognition as sr
import psutil
import pyperclip
import screen_brightness_control as sbc
import pyttsx3


# =========================
# JARVIS SETTINGS
# =========================

engine = pyttsx3.init()
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


# =========================
# VOICE OUTPUT
# =========================

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()


# =========================
# LISTEN
# =========================

def listen():
    try:
        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.3
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        try:
            text = recognizer.recognize_google(
                audio,
                language="en-US"
            )

        except:
            text = recognizer.recognize_google(
                audio,
                language="si-LK"
            )

        print("YOU:", text)

        return text.lower().strip()

    except sr.WaitTimeoutError:
        return ""

    except Exception as e:
        print("Voice error:", e)
        return ""


# =========================
# WAKE WORD
# =========================

def get_command():

    text = listen()

    if not text:
        return ""

    # Wake word check
    wake_words = [
        "hey jarvis",
        "hey jarvis",
        "jarvis"
    ]

    found = False

    for wake in wake_words:

        if wake in text:

            found = True

            # Remove wake word
            command = text.replace(wake, "").strip()

            # Example:
            # "hey jarvis open chrome"
            if command:
                return command

            # Example:
            # "hey jarvis"
            speak("Yes, I'm listening.")

            return listen()

    # No wake word = ignore
    if not found:
        print("Wake word not detected.")
        return ""

    return ""


# =========================
# OPEN WEBSITES
# =========================

def open_google():

    subprocess.Popen(
        ["cmd", "/c", "start", "https://google.com"]
    )

    speak("Opening Google.")


def open_youtube():

    subprocess.Popen(
        ["cmd", "/c", "start", "https://youtube.com"]
    )

    speak("Opening YouTube.")


def open_chrome():

    try:
        subprocess.Popen("chrome.exe")

    except:
        subprocess.Popen(
            ["cmd", "/c", "start", "chrome"]
        )

    speak("Opening Chrome.")


# =========================
# OPEN APPS
# =========================

def open_app(app):

    try:

        subprocess.Popen(app)

    except:

        speak("I could not open that application.")


# =========================
# VOLUME
# =========================

def volume_up():

    for _ in range(5):

        ctypes.windll.user32.keybd_event(
            0xAF,
            0,
            0,
            0
        )

    speak("Volume increased.")


def volume_down():

    for _ in range(5):

        ctypes.windll.user32.keybd_event(
            0xAE,
            0,
            0,
            0
        )

    speak("Volume decreased.")


def mute():

    ctypes.windll.user32.keybd_event(
        0xAD,
        0,
        0,
        0
    )

    speak("Volume muted.")


# =========================
# BRIGHTNESS
# =========================

def brightness_up():

    try:

        current = sbc.get_brightness()[0]

        value = min(
            current + 10,
            100
        )

        sbc.set_brightness(value)

        speak(
            f"Brightness {value} percent."
        )

    except:

        speak(
            "Brightness control is unavailable."
        )


def brightness_down():

    try:

        current = sbc.get_brightness()[0]

        value = max(
            current - 10,
            0
        )

        sbc.set_brightness(value)

        speak(
            f"Brightness {value} percent."
        )

    except:

        speak(
            "Brightness control is unavailable."
        )


# =========================
# SYSTEM STATUS
# =========================

def system_status():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    battery = psutil.sensors_battery()

    speak(
        f"CPU usage is {cpu} percent."
    )

    speak(
        f"RAM usage is {ram} percent."
    )

    if battery:

        speak(
            f"Battery is {battery.percent} percent."
        )


def battery_status():

    battery = psutil.sensors_battery()

    if battery:

        speak(
            f"Battery is {battery.percent} percent."
        )

    else:

        speak(
            "Battery information is unavailable."
        )


def internet_status():

    try:

        urllib.request.urlopen(
            "https://www.google.com",
            timeout=3
        )

        speak(
            "Internet connection is working."
        )

    except:

        speak(
            "Internet connection is unavailable."
        )


# =========================
# CLIPBOARD
# =========================

def read_clipboard():

    text = pyperclip.paste()

    if text:

        print("\nCLIPBOARD:")
        print(text)

        speak(
            "I displayed the clipboard content in the command window."
        )

    else:

        speak(
            "The clipboard is empty."
        )


# =========================
# FOLDERS
# =========================

def open_folder(folder):

    path = os.path.expanduser(folder)

    if os.path.exists(path):

        os.startfile(path)

    else:

        speak(
            "That folder was not found."
        )


# =========================
# TIMER
# =========================

def start_timer(minutes):

    def timer_thread():

        time.sleep(
            minutes * 60
        )

        speak(
            "Timer finished."
        )

    threading.Thread(
        target=timer_thread,
        daemon=True
    ).start()

    speak(
        f"Timer started for {minutes} minutes."
    )


# =========================
# SCREENSHOT
# =========================

def screenshot():

    subprocess.Popen(
        [
            "explorer.exe",
            "ms-screenclip:"
        ]
    )

    speak(
        "Screenshot tool opened."
    )


# =========================
# WINDOW CONTROL
# =========================

def minimize_window():

    ctypes.windll.user32.keybd_event(
        0x5B,
        0,
        0,
        0
    )

    ctypes.windll.user32.keybd_event(
        0x28,
        0,
        0,
        0
    )

    ctypes.windll.user32.keybd_event(
        0x28,
        0,
        2,
        0
    )

    ctypes.windll.user32.keybd_event(
        0x5B,
        0,
        2,
        0
    )

    speak(
        "Window minimized."
    )


def maximize_window():

    ctypes.windll.user32.keybd_event(
        0x5B,
        0,
        0,
        0
    )

    ctypes.windll.user32.keybd_event(
        0x26,
        0,
        0,
        0
    )

    ctypes.windll.user32.keybd_event(
        0x26,
        0,
        2,
        0
    )

    ctypes.windll.user32.keybd_event(
        0x5B,
        0,
        2,
        0
    )

    speak(
        "Window maximized."
    )


def close_window():

    ctypes.windll.user32.keybd_event(
        0x12,
        0,
        0,
        0
    )

    ctypes.windll.user32.keybd_event(
        0x73,
        0,
        0,
        0
    )

    ctypes.windll.user32.keybd_event(
        0x73,
        0,
        2,
        0
    )

    ctypes.windll.user32.keybd_event(
        0x12,
        0,
        2,
        0
    )

    speak(
        "Window closed."
    )


# =========================
# POWER
# =========================

def lock_pc():

    speak(
        "Locking the computer."
    )

    ctypes.windll.user32.LockWorkStation()


def shutdown_pc():

    speak(
        "Computer will shut down in five seconds."
    )

    os.system(
        "shutdown /s /t 5"
    )


def cancel_shutdown():

    os.system(
        "shutdown /a"
    )

    speak(
        "Shutdown cancelled."
    )


def restart_pc():

    speak(
        "Computer will restart in five seconds."
    )

    os.system(
        "shutdown /r /t 5"
    )


def sleep_pc():

    speak(
        "Putting the computer to sleep."
    )

    os.system(
        "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    )


# =========================
# COMMAND PROCESSOR
# =========================

def process_command(text):

    if not text:
        return True


    # =====================
    # WEBSITES
    # =====================

    if (
        "open google" in text
        or text == "google"
    ):

        open_google()


    elif (
        "open youtube" in text
        or text == "youtube"
    ):

        open_youtube()


    # =====================
    # APPS
    # =====================

    elif "open chrome" in text:

        open_chrome()


    elif "open notepad" in text:

        open_app(
            "notepad.exe"
        )

        speak(
            "Opening Notepad."
        )


    elif "open calculator" in text:

        open_app(
            "calc.exe"
        )

        speak(
            "Opening Calculator."
        )


    elif "open paint" in text:

        open_app(
            "mspaint.exe"
        )

        speak(
            "Opening Paint."
        )


    # =====================
    # FOLDERS
    # =====================

    elif "open downloads" in text:

        open_folder(
            "~/Downloads"
        )

        speak(
            "Opening Downloads."
        )


    elif "open desktop" in text:

        open_folder(
            "~/Desktop"
        )

        speak(
            "Opening Desktop."
        )


    elif "open documents" in text:

        open_folder(
            "~/Documents"
        )

        speak(
            "Opening Documents."
        )


    elif "open pictures" in text:

        open_folder(
            "~/Pictures"
        )

        speak(
            "Opening Pictures."
        )


    elif "open videos" in text:

        open_folder(
            "~/Videos"
        )

        speak(
            "Opening Videos."
        )


    # =====================
    # VOLUME
    # =====================

    elif "volume up" in text:

        volume_up()


    elif "volume down" in text:

        volume_down()


    elif "mute" in text:

        mute()


    # =====================
    # BRIGHTNESS
    # =====================

    elif "brightness up" in text:

        brightness_up()


    elif "brightness down" in text:

        brightness_down()


    # =====================
    # SYSTEM
    # =====================

    elif "system status" in text:

        system_status()


    elif (
        "cpu" in text
        or "ram" in text
    ):

        system_status()


    elif "battery" in text:

        battery_status()


    elif "internet" in text:

        internet_status()


    # =====================
    # CLIPBOARD
    # =====================

    elif "clipboard" in text:

        read_clipboard()


    # =====================
    # SCREENSHOT
    # =====================

    elif "screenshot" in text:

        screenshot()


    # =====================
    # WINDOW
    # =====================

    elif "minimize" in text:

        minimize_window()


    elif "maximize" in text:

        maximize_window()


    elif "close window" in text:

        close_window()


    # =====================
    # TIMER
    # =====================

    elif "timer" in text:

        numbers = [

            int(word)

            for word in text.split()

            if word.isdigit()

        ]

        if numbers:

            start_timer(
                numbers[0]
            )

        else:

            speak(
                "Please say the timer duration."
            )


    # =====================
    # POWER
    # =====================

    elif (
        "lock computer" in text
        or "lock pc" in text
    ):

        lock_pc()


    elif "cancel shutdown" in text:

        cancel_shutdown()


    elif "shutdown" in text:

        shutdown_pc()


    elif "restart" in text:

        restart_pc()


    elif (
        "sleep computer" in text
        or "sleep pc" in text
    ):

        sleep_pc()


    # =====================
    # STOP
    # =====================

    elif (
        "stop jarvis" in text
        or "exit jarvis" in text
        or "goodbye jarvis" in text
    ):

        speak(
            "Goodbye."
        )

        return False


    else:

        speak(
            "I don't understand that command yet."
        )


    return True


# =========================
# START JARVIS
# =========================

speak(
    "JARVIS system online."
)

speak(
    "Say, Hey JARVIS, when you need me."
)


# =========================
# MAIN LOOP
# =========================

while True:

    command = get_command()

    if command:

        if not process_command(command):

            break