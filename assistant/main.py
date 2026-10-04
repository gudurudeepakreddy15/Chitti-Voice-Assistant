from assistant.speech import (
    speak,
    listen,
    calibrate_microphone
)

from assistant.commands import handle_command


# ==========================================================
# START CHITTI
# ==========================================================

def start_chitti():

    print("================================")
    print("       CHITTI AI STARTING")
    print("================================")

    # Calibrate microphone
    if not calibrate_microphone():

        return

    speak("Hi Deepak, I am Chitti.")

    print("\nChitti is ready!")
    print("Say something...\n")

    # Main loop
    while True:

        command = listen()

        if not command:

            continue

        result = handle_command(command)

        if result == "stop":

            break


# ==========================================================
# RUN CHITTI
# ==========================================================

if __name__ == "__main__":

    start_chitti()