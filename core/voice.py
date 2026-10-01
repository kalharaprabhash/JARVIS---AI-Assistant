import asyncio
import os
import speech_recognition as sr
import edge_tts
import pygame

from faster_whisper import WhisperModel

from config import (
    WAKE_WORDS,
    LANGUAGE,
    LISTEN_TIMEOUT,
    PHRASE_TIME_LIMIT
)


# =========================
# WHISPER
# =========================

print("Loading JARVIS speech model...")

model = WhisperModel(
    "small.en",
    device="cpu",
    compute_type="int8"
)

print("Speech model ready.")


# =========================
# MICROPHONE
# =========================

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


# =========================
# JARVIS VOICE
# =========================

VOICE = "en-US-GuyNeural"


def speak(text):
    print(f"JARVIS: {text}")

    file = "jarvis_voice.mp3"

    async def generate_voice():
        await edge_tts.Communicate(
            text,
            VOICE
        ).save(file)

    asyncio.run(generate_voice())

    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.quit()


# =========================
# RECORD AUDIO
# =========================

def record_audio():

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=LISTEN_TIMEOUT,
                phrase_time_limit=PHRASE_TIME_LIMIT
            )

            return audio

        except sr.WaitTimeoutError:

            return None


# =========================
# WHISPER TRANSCRIPTION
# =========================

def transcribe(audio):

    if audio is None:
        return ""

    try:

        wav_data = audio.get_wav_data()

        filename = "jarvis_input.wav"

        with open(filename, "wb") as f:
            f.write(wav_data)

        segments, info = model.transcribe(
            filename,
            language="en",
            beam_size=5,
            temperature=0,
            vad_filter=False,
            condition_on_previous_text=False
        )

        text = " ".join(
            segment.text
            for segment in segments
        ).strip()

        print(f"You: {text}")

        return text.lower()

    except Exception as e:

        print("Whisper error:", e)

        return ""


# =========================
# GET COMMAND
# =========================

def get_command():

    audio = record_audio()

    text = transcribe(audio)

    if not text:
        return ""

    for wake_word in sorted(
        WAKE_WORDS,
        key=len,
        reverse=True
    ):

        if text.startswith(wake_word):

            command = text[len(wake_word):].strip()

            print(f"COMMAND: {command}")

            return command

    return text