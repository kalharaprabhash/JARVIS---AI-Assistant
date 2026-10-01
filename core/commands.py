from ai.brain import think

from system.apps import (
    open_google,
    open_youtube,
    open_chrome,
    open_notepad,
    open_calculator,
    open_paint,
    open_downloads,
    open_desktop,
    open_documents,
    open_pictures,
    open_videos
)

from system.windows import (
    volume_up,
    volume_down,
    volume_mute,
    brightness_up,
    brightness_down,
    read_clipboard,
    take_screenshot,
    minimize_window,
    maximize_window,
    close_window
)

from system.power import (
    lock_pc,
    shutdown_pc,
    cancel_shutdown,
    restart_pc,
    sleep_pc
)

from system.system_info import (
    get_system_status,
    get_battery_status,
    check_internet
)


def process_command(command, speak):

    command = command.lower().strip()

    if not command:
        return True

    # =========================
    # APPS / WEBSITES
    # =========================

    if "google" in command:
        speak("Opening Google.")
        open_google()

    elif "youtube" in command:
        speak("Opening YouTube.")
        open_youtube()

    elif "chrome" in command:
        speak("Opening Chrome.")
        open_chrome()

    elif "notepad" in command:
        speak("Opening Notepad.")
        open_notepad()

    elif "calculator" in command or "calculate" in command:
        speak("Opening Calculator.")
        open_calculator()

    elif "paint" in command:
        speak("Opening Paint.")
        open_paint()

    elif "downloads" in command or "download folder" in command:
        speak("Opening Downloads.")
        open_downloads()

    elif "desktop" in command:
        speak("Opening Desktop.")
        open_desktop()

    elif "documents" in command or "document folder" in command:
        speak("Opening Documents.")
        open_documents()

    elif "pictures" in command or "picture folder" in command:
        speak("Opening Pictures.")
        open_pictures()

    elif "videos" in command or "video folder" in command:
        speak("Opening Videos.")
        open_videos()

    # =========================
    # VOLUME
    # =========================

    elif (
        "volume up" in command
        or "increase volume" in command
        or "volume increase" in command
    ):
        volume_up()

    elif (
        "volume down" in command
        or "decrease volume" in command
        or "volume decrease" in command
    ):
        volume_down()

    elif (
        "mute" in command
        or "mute volume" in command
        or "volume mute" in command
    ):
        volume_mute()

    # =========================
    # BRIGHTNESS
    # =========================

    elif (
        "brightness up" in command
        or "increase brightness" in command
        or "brightness increase" in command
    ):
        brightness_up()

    elif (
        "brightness down" in command
        or "decrease brightness" in command
        or "brightness decrease" in command
    ):
        brightness_down()

    # =========================
    # WINDOWS
    # =========================

    elif "read clipboard" in command or "clipboard" in command:
        result = read_clipboard()
        speak(result)

    elif (
        "screenshot" in command
        or "take screenshot" in command
        or "screen shot" in command
    ):
        speak("Taking screenshot.")
        take_screenshot()

    elif "minimize" in command:
        minimize_window()

    elif "maximize" in command:
        maximize_window()

    elif "close window" in command or "close this" in command:
        close_window()

    # =========================
    # SYSTEM STATUS
    # =========================

    elif (
        "system status" in command
        or "system information" in command
        or "computer status" in command
    ):
        speak(get_system_status())

    elif (
        "battery status" in command
        or "battery" in command
    ):
        speak(get_battery_status())

    elif (
        "internet status" in command
        or "internet connection" in command
        or "internet" in command
    ):
        if check_internet():
            speak("Internet connection is available.")
        else:
            speak("Internet connection is not available.")

    # =========================
    # POWER
    # =========================

    elif (
        "lock computer" in command
        or "lock pc" in command
        or "lock computer" in command
    ):
        speak("Locking the computer.")
        lock_pc()

    elif "cancel shutdown" in command:
        cancel_shutdown()
        speak("Shutdown cancelled.")

    elif (
        "restart computer" in command
        or "restart pc" in command
        or "restart" in command
    ):
        speak("Restarting the computer in 10 seconds.")
        restart_pc()

    elif (
        "shutdown computer" in command
        or "shutdown pc" in command
        or "shut down" in command
    ):
        speak("Shutting down the computer in 10 seconds.")
        shutdown_pc()

    elif (
        "sleep computer" in command
        or "sleep pc" in command
    ):
        speak("Putting the computer to sleep.")
        sleep_pc()

    # =========================
    # EXIT
    # =========================

    elif (
        "stop" in command
        or "exit" in command
        or "goodbye" in command
    ):
        speak("Goodbye.")
        return False

    # =========================
    # AI
    # =========================

    else:

        response = think(command)

        print("AI RESPONSE:", response)

        if response:
            speak(response)
        else:
            speak("I don't understand that command yet.")

    return True