from assistant.speech import speak
from assistant.websites import (
    find_website,
    open_website,
    google_search
)
from assistant.applications import (
    open_application,
    open_chrome
)


# ==========================================================
# STOP COMMANDS
# ==========================================================

STOP_COMMANDS = [
    "stop chitti",
    "bye chitti",
    "goodbye chitti",
    "exit chitti",
    "quit chitti",
    "stop"
]


# ==========================================================
# GREETINGS
# ==========================================================

GREETINGS = [
    "hello",
    "hi",
    "hey",
    "hello chitti",
    "hi chitti",
    "hey chitti"
]


# ==========================================================
# CHECK STOP COMMAND
# ==========================================================

def is_stop_command(command):

    command = command.lower().strip()

    for stop_command in STOP_COMMANDS:

        if command == stop_command:

            return True

    return False


# ==========================================================
# REMOVE GREETING
# ==========================================================

def remove_greeting(command):

    command = command.lower().strip()

    for greeting in GREETINGS:

        if command == greeting:

            return ""

        if command.startswith(greeting + " "):

            command = command[len(greeting):].strip()

            return command

    return command


# ==========================================================
# HANDLE COMMAND
# ==========================================================

def handle_command(command):

    command = command.lower().strip()

    # ------------------------------------------------------
    # STOP
    # ------------------------------------------------------

    if is_stop_command(command):

        speak("Goodbye!")

        return "stop"


    # ------------------------------------------------------
    # GREETING
    # ------------------------------------------------------

    if command in GREETINGS:

        speak("Hello! How can I help you?")

        return "continue"


    # ------------------------------------------------------
    # REMOVE GREETING
    # ------------------------------------------------------

    command = remove_greeting(command)

    if command == "":

        speak("Hello! How can I help you?")

        return "continue"


    # ------------------------------------------------------
    # OPEN CHROME
    # ------------------------------------------------------

    if "open chrome" in command:

        speak("Opening Chrome.")

        open_chrome()

        return "continue"


    # ------------------------------------------------------
    # GOOGLE SEARCH
    # ------------------------------------------------------

    if command.startswith("search "):

        query = command[7:].strip()

        if query:

            speak("Searching Google.")

            google_search(query)

            return "continue"


    if command.startswith("google "):

        query = command[7:].strip()

        if query:

            speak("Searching Google.")

            google_search(query)

            return "continue"


    # ------------------------------------------------------
    # OPEN WEBSITE
    # ------------------------------------------------------

    if command.startswith("open "):

        target = command[5:].strip()

        website = find_website(target)

        if website:

            speak("Opening " + website)

            open_website(website)

            return "continue"


    # ------------------------------------------------------
    # WINDOWS APPLICATIONS
    # ------------------------------------------------------

    if command.startswith("open "):

        target = command[5:].strip()

        if open_application(target):

            speak("Opening " + target)

            return "continue"


    # ------------------------------------------------------
    # WEBSITE NAME WITHOUT "OPEN"
    # ------------------------------------------------------

    website = find_website(command)

    if website:

        speak("Opening " + website)

        open_website(website)

        return "continue"


    # ------------------------------------------------------
    # UNKNOWN COMMAND
    # ------------------------------------------------------

    speak(
        "Sorry, I don't understand that command."
    )

    return "continue"