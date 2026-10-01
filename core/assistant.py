from core.voice import speak, get_command
from core.commands import process_command


def start_assistant():
    speak("JARVIS system online. How can I help you?")

    running = True

    while running:
        command = get_command()

        if command:
            running = process_command(command, speak)