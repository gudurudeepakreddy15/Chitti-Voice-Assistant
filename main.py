import speech_recognition as sr
import webbrowser
import subprocess
import urllib.parse
import os
import difflib


# ==========================================================
# CHITTI VOICE
# ==========================================================
# Uses Windows built-in speech system.
# This is more reliable for repeated responses than
# repeatedly using pyttsx3 on some Windows systems.
# ==========================================================

def speak(text):

    print("Chitti:", text)

    try:

        # Put text into an environment variable.
        # This avoids problems with quotes in PowerShell.
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
# SPEECH RECOGNITION
# ==========================================================

recognizer = sr.Recognizer()

recognizer.pause_threshold = 0.8
recognizer.non_speaking_duration = 0.3

# Starting value.
# It will be changed after microphone calibration.
recognizer.energy_threshold = 300

recognizer.dynamic_energy_threshold = True


# ==========================================================
# TEXT CLEANING
# ==========================================================

def clean_text(text):

    text = text.lower().strip()

    # Common speech recognition mistakes
    replacements = {

        "chitty": "chitti",
        "chitty": "chitti",
        "chite": "chitti",
        "chitey": "chitti",
        "chity": "chitti",
        "chiti": "chitti",

        # "chit" can happen when saying "Chitti"
        "stop chit": "stop chitti",
        "bye chit": "bye chitti",
        "goodbye chit": "goodbye chitti",
        "exit chit": "exit chitti",
        "quit chit": "quit chitti"

    }

    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)

    return text


# ==========================================================
# LISTEN
# ==========================================================

def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:

            print("No speech detected.")
            return ""

    try:

        text = recognizer.recognize_google(audio)

        text = clean_text(text)

        print("You said:", text)

        return text

    except sr.UnknownValueError:

        print("Could not understand.")
        return ""

    except sr.RequestError:

        speak(
            "Sorry, speech recognition is not available."
        )

        return ""


# ==========================================================
# WINDOWS APPLICATIONS
# ==========================================================

def open_application(name):

    applications = {

        "calculator": "calc",
        "calc": "calc",

        "notepad": "notepad",

        "paint": "mspaint",

        "file explorer": "explorer",
        "explorer": "explorer",

        "command prompt": "cmd",
        "cmd": "cmd",

        "powershell": "powershell",

        "task manager": "taskmgr"

    }

    name = name.lower().strip()

    if name in applications:

        speak("Opening " + name)

        try:

            subprocess.Popen(
                applications[name]
            )

        except Exception:

            speak(
                "I could not open " + name
            )

        return True

    return False


# ==========================================================
# OPEN CHROME
# ==========================================================

def open_chrome():

    speak("Opening Chrome")

    try:

        subprocess.Popen(
            [
                "cmd",
                "/c",
                "start",
                "",
                "chrome"
            ],
            shell=False
        )

    except Exception:

        speak("I could not open Chrome")


# ==========================================================
# WEBSITE LIST
# ==========================================================

websites = {

    "youtube":
        "https://www.youtube.com",

    "chatgpt":
        "https://chatgpt.com",

    "google":
        "https://www.google.com",

    "github":
        "https://github.com",

    "w3schools":
        "https://www.w3schools.com",

    "leetcode":
        "https://leetcode.com",

    "geeksforgeeks":
        "https://www.geeksforgeeks.org",

    "linkedin":
        "https://www.linkedin.com",

    "instagram":
        "https://www.instagram.com",

    "facebook":
        "https://www.facebook.com",

    "whatsapp":
        "https://web.whatsapp.com",

    "gmail":
        "https://mail.google.com",

    "python":
        "https://www.python.org",

    "stackoverflow":
        "https://stackoverflow.com",

    "reddit":
        "https://www.reddit.com",

    "amazon":
        "https://www.amazon.in",

    "flipkart":
        "https://www.flipkart.com",

    "netflix":
        "https://www.netflix.com",

    "wikipedia":
        "https://www.wikipedia.org",

    "spotify":
        "https://open.spotify.com",

    "discord":
        "https://discord.com",

    "microsoft":
        "https://www.microsoft.com",

    "x":
        "https://x.com"

}


# ==========================================================
# WEBSITE ALIASES
# ==========================================================

website_aliases = {

    # YouTube
    "youtube": "youtube",
    "you tube": "youtube",

    # ChatGPT
    "chatgpt": "chatgpt",
    "chat gpt": "chatgpt",

    # Google
    "google": "google",

    # GitHub
    "github": "github",
    "git hub": "github",

    # W3Schools
    "w3schools": "w3schools",
    "w3 school": "w3schools",
    "w3 schools": "w3schools",
    "w three schools": "w3schools",
    "w three school": "w3schools",

    # LeetCode
    "leetcode": "leetcode",
    "leet code": "leetcode",

    # GeeksForGeeks
    "geeksforgeeks": "geeksforgeeks",
    "geeks for geeks": "geeksforgeeks",
    "geeks for geek": "geeksforgeeks",

    # LinkedIn
    "linkedin": "linkedin",
    "linked in": "linkedin",

    # Instagram
    "instagram": "instagram",
    "insta": "instagram",

    # Facebook
    "facebook": "facebook",
    "face book": "facebook",

    # WhatsApp
    "whatsapp": "whatsapp",
    "whats app": "whatsapp",

    # Gmail
    "gmail": "gmail",
    "g mail": "gmail",

    # Python
    "python": "python",
    "python website": "python",

    # StackOverflow
    "stackoverflow": "stackoverflow",
    "stack overflow": "stackoverflow",

    # Reddit
    "reddit": "reddit",

    # Amazon
    "amazon": "amazon",
    "amazon india": "amazon",

    # Flipkart
    "flipkart": "flipkart",
    "flip kart": "flipkart",

    # Netflix
    "netflix": "netflix",

    # Wikipedia
    "wikipedia": "wikipedia",
    "wiki pedia": "wikipedia",

    # Spotify
    "spotify": "spotify",

    # Discord
    "discord": "discord",

    # Microsoft
    "microsoft": "microsoft",

    # X
    "twitter": "x",
    "x": "x"

}


# ==========================================================
# NORMALIZE WEBSITE NAME
# ==========================================================

def normalize_website_name(name):

    name = name.lower().strip()

    # Remove unnecessary words
    removable_words = [
        "website",
        "site",
        "web site"
    ]

    for word in removable_words:

        name = name.replace(word, "").strip()

    return name


# ==========================================================
# FIND WEBSITE
# ==========================================================

def find_website(name):

    name = normalize_website_name(name)

    # Exact alias
    if name in website_aliases:

        return website_aliases[name]

    # Exact website key
    if name in websites:

        return name

    # Fuzzy matching
    all_names = list(website_aliases.keys())

    matches = difflib.get_close_matches(
        name,
        all_names,
        n=1,
        cutoff=0.65
    )

    if matches:

        return website_aliases[matches[0]]

    return None


# ==========================================================
# OPEN WEBSITE
# ==========================================================

def open_website(name):

    website_key = find_website(name)

    if website_key is None:

        return False

    speak(
        "Opening " + website_key
    )

    try:

        webbrowser.open(
            websites[website_key]
        )

    except Exception:

        speak(
            "I could not open "
            + website_key
        )

    return True


# ==========================================================
# OPEN DIRECT URL
# ==========================================================

def open_url(target):

    target = target.strip()

    # Already a complete URL
    if target.startswith("http://") or target.startswith("https://"):

        speak("Opening website")

        try:

            webbrowser.open(target)

        except Exception:

            speak("I could not open that website.")

        return True


    # Domain such as example.com
    if "." in target and " " not in target:

        url = "https://" + target

        speak("Opening website")

        try:

            webbrowser.open(url)

        except Exception:

            speak("I could not open that website.")

        return True

    return False


# ==========================================================
# GOOGLE SEARCH
# ==========================================================

def search_google(query):

    query = query.strip()

    if query == "":

        speak(
            "What should I search for?"
        )

        return

    speak(
        "Searching for " + query
    )

    encoded_query = urllib.parse.quote(
        query
    )

    url = (
        "https://www.google.com/search?q="
        + encoded_query
    )

    try:

        webbrowser.open(url)

    except Exception:

        speak(
            "I could not perform the search."
        )


# ==========================================================
# STOP COMMAND
# ==========================================================

def is_stop_command(command):

    command = clean_text(command)

    command = command.strip()

    # Exact commands
    stop_commands = {

        "bye",
        "goodbye",
        "stop",
        "exit",
        "quit",

        "bye chitti",
        "goodbye chitti",
        "stop chitti",
        "exit chitti",
        "quit chitti",

        "chitti bye",
        "chitti goodbye",
        "chitti stop",
        "chitti exit",
        "chitti quit",

        "stop listening",
        "stop listening chitti"

    }

    if command in stop_commands:

        return True

    # Also handle natural sentences
    words = command.split()

    if len(words) >= 1:

        first_word = words[0]

        if first_word in {
            "stop",
            "exit",
            "quit",
            "bye",
            "goodbye"
        }:

            # Accept:
            # stop
            # stop chitti
            # stop listening
            # bye chitti
            return True

    return False


# ==========================================================
# GREETING
# ==========================================================

def greeting(command):

    command = clean_text(command)

    command = command.strip()

    greetings = {

        "hi",
        "hello",
        "hey",
        "hi chitti",
        "hello chitti",
        "hey chitti"

    }

    if command in greetings:

        speak(
            "Hello Deepak, "
            "what can I help you with?"
        )

        return True


    if command == "good morning":

        speak(
            "Good morning Deepak"
        )

        return True


    if command == "good afternoon":

        speak(
            "Good afternoon Deepak"
        )

        return True


    if command == "good evening":

        speak(
            "Good evening Deepak"
        )

        return True


    if command == "good night":

        speak(
            "Good night Deepak"
        )

        return True

    return False


# ==========================================================
# REMOVE GREETING / CHITTI
# ==========================================================

def remove_greeting(command):

    greetings = [

        "hello chitti",
        "hi chitti",
        "hey chitti",
        "chitti",

        "hello",
        "hi",
        "hey"

    ]

    for word in greetings:

        if command.startswith(word):

            command = command[
                len(word):
            ].strip()

            break

    return command


# ==========================================================
# HANDLE COMMAND
# ==========================================================

def handle_command(command):

    command = clean_text(command)


    # ------------------------------------------------------
    # STOP
    # ------------------------------------------------------

    if is_stop_command(command):

        speak(
            "Goodbye Deepak"
        )

        return False


    # ------------------------------------------------------
    # GREETINGS
    # ------------------------------------------------------

    if greeting(command):

        return True


    # ------------------------------------------------------
    # REMOVE "CHITTI"
    # ------------------------------------------------------

    command = remove_greeting(
        command
    )


    # ------------------------------------------------------
    # ONLY CHITTI
    # ------------------------------------------------------

    if command == "":

        speak(
            "Yes Deepak, "
            "what can I help you with?"
        )

        return True


    # ------------------------------------------------------
    # SEARCH FOR
    # ------------------------------------------------------

    if command.startswith(
        "search for "
    ):

        query = command[
            len("search for "):
        ].strip()

        search_google(query)

        return True


    # ------------------------------------------------------
    # SEARCH
    # ------------------------------------------------------

    if command.startswith(
        "search "
    ):

        query = command[
            len("search "):
        ].strip()

        search_google(query)

        return True


    # ------------------------------------------------------
    # OPEN COMMAND
    # ------------------------------------------------------

    if command.startswith(
        "open "
    ):

        target = command[
            len("open "):
        ].strip()


        # ----------------------------------------------
        # Chrome
        # ----------------------------------------------

        if target in {

            "chrome",
            "google chrome"

        }:

            open_chrome()

            return True


        # ----------------------------------------------
        # Windows applications
        # ----------------------------------------------

        if open_application(
            target
        ):

            return True


        # ----------------------------------------------
        # Direct URL
        # ----------------------------------------------

        if open_url(
            target
        ):

            return True


        # ----------------------------------------------
        # Known website
        # ----------------------------------------------

        if open_website(
            target
        ):

            return True


        # ----------------------------------------------
        # Unknown website
        # ----------------------------------------------

        speak(
            "I don't know that website. "
            "I will search for it."
        )

        search_google(
            target
        )

        return True


    # ------------------------------------------------------
    # DIRECT WEBSITE NAME
    # Example: You say "leetcode"
    # ------------------------------------------------------

    if open_website(
        command
    ):

        return True


    # ------------------------------------------------------
    # DIRECT CHROME
    # ------------------------------------------------------

    if command in {

        "chrome",
        "google chrome"

    }:

        open_chrome()

        return True


    # ------------------------------------------------------
    # UNKNOWN COMMAND
    # ------------------------------------------------------

    speak(
        "Sorry, I don't understand "
        "that command yet."
    )

    return True


# ==========================================================
# MAIN
# ==========================================================

def main():

    print()
    print("========================================")
    print("              CHITTI AI")
    print("========================================")
    print()


    # ------------------------------------------------------
    # MICROPHONE CALIBRATION
    # ------------------------------------------------------

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
                duration=2
            )

            print(
                "Noise calibration complete."
            )

            print(
                "Energy threshold:",
                recognizer.energy_threshold
            )

    except Exception as e:

        print(
            "Microphone error:",
            e
        )

        speak(
            "I could not access "
            "the microphone."
        )

        return


    print()
    print(
        "Microphone ready!"
    )
    print()


    # ------------------------------------------------------
    # START MESSAGE
    # ------------------------------------------------------

    speak(
        "Hi Deepak, "
        "I am Chitti. "
        "What can I help you with?"
    )


    # ------------------------------------------------------
    # MAIN LOOP
    # ------------------------------------------------------

    while True:

        command = listen()

        if command == "":
            continue

        keep_running = handle_command(
            command
        )

        if not keep_running:

            break


# ==========================================================
# START CHITTI
# ==========================================================

if __name__ == "__main__":

    main()