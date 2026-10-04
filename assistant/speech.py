import os
import subprocess
import speech_recognition as sr

from config.settings import (
    LISTEN_TIMEOUT,
    PHRASE_TIME_LIMIT,
    NOISE_CALIBRATION_DURATION,
    PAUSE_THRESHOLD,
    NON_SPEAKING_DURATION,
    ENERGY_THRESHOLD
)


# ==========================================================
# SPEAK
# ==========================================================

def speak(text):

    print("Chitti:", text)

    try:

        env = os.environ.copy()
        env["CHITTI_TEXT"] = text

        powershell_command = (
            "Add-Type -AssemblyName System.Speech; "
            "$voice = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
            "$voice.Rate = 0; "
            "$voice.Volume = 100; "
            "$voice.Speak($env:CHITTI_TEXT); "
            "$voice.Dispose();"
        )

        subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-Command",
                powershell_command
            ],
            env=env,
            check=False,
            creationflags=getattr(
                subprocess,
                "CREATE_NO_WINDOW",
                0
            )
        )

    except Exception as e:

        print("Voice error:", e)


# ==========================================================
# SPEECH RECOGNIZER
# ==========================================================

recognizer = sr.Recognizer()

recognizer.pause_threshold = PAUSE_THRESHOLD
recognizer.non_speaking_duration = NON_SPEAKING_DURATION
recognizer.energy_threshold = ENERGY_THRESHOLD
recognizer.dynamic_energy_threshold = True


# ==========================================================
# TEXT CLEANING
# ==========================================================

def clean_text(text):

    text = text.lower().strip()

    replacements = {

        "chitty": "chitti",
        "chite": "chitti",
        "chitey": "chitti",
        "chity": "chitti",
        "chiti": "chitti",

        "stop chit": "stop chitti",
        "bye chit": "bye chitti",
        "goodbye chit": "goodbye chitti",
        "exit chit": "exit chitti",
        "quit chit": "quit chitti"

    }

    for wrong, correct in replacements.items():

        text = text.replace(
            wrong,
            correct
        )

    return text


# ==========================================================
# MICROPHONE CALIBRATION
# ==========================================================

def calibrate_microphone():

    try:

        with sr.Microphone() as source:

            print(
                "Adjusting microphone "
                "for background noise..."
            )

            print(
                "Please stay quiet "
                "for 2 seconds..."
            )

            recognizer.adjust_for_ambient_noise(
                source,
                duration=NOISE_CALIBRATION_DURATION
            )

            print(
                "Noise calibration complete."
            )

            print(
                "Energy threshold:",
                recognizer.energy_threshold
            )

            print("Microphone ready!")

            return True

    except Exception as e:

        print(
            "Microphone error:",
            e
        )

        speak(
            "I could not access "
            "the microphone."
        )

        return False


# ==========================================================
# LISTEN
# ==========================================================

def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        try:

            audio = recognizer.listen(
                source,
                timeout=LISTEN_TIMEOUT,
                phrase_time_limit=PHRASE_TIME_LIMIT
            )

        except sr.WaitTimeoutError:

            print("No speech detected.")

            return ""

    try:

        text = recognizer.recognize_google(
            audio
        )

        text = clean_text(text)

        print(
            "You said:",
            text
        )

        return text

    except sr.UnknownValueError:

        print(
            "Could not understand."
        )

        return ""

    except sr.RequestError:

        speak(
            "Sorry, speech recognition "
            "is not available."
        )

        return ""