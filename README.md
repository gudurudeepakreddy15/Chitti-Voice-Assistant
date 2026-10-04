# Chitti AI 🤖

Chitti AI is a Python-based voice assistant for Windows.

It listens to voice commands, understands them using speech recognition, and performs useful actions such as opening websites, searching Google, and launching Windows applications.

## Features

* 🎤 Voice command recognition
* 🔊 Voice responses
* 🌐 Open popular websites
* 🔎 Google search using voice
* 🖥️ Open Windows applications
* 🌐 Open Chrome
* 👋 Greeting commands
* 🛑 Stop commands
* 🎧 Microphone noise calibration
* 🗂️ Modular Python project structure

## Supported Websites

Chitti can open websites such as:

* YouTube
* ChatGPT
* Google
* GitHub
* W3Schools
* LeetCode
* GeeksforGeeks
* LinkedIn
* Instagram
* WhatsApp
* Gmail
* Python
* Stack Overflow
* Reddit
* Amazon
* Flipkart
* Netflix
* Wikipedia
* Spotify
* Discord
* Microsoft
* X

## Windows Applications

Chitti can open:

* Calculator
* Notepad
* Paint
* File Explorer
* Command Prompt
* PowerShell
* Task Manager
* Chrome

## Technologies Used

* Python
* SpeechRecognition
* PyAudio
* Windows PowerShell
* Web browser automation

## Project Structure

```text
chitti AI/
│
├── assistant/
│   ├── __init__.py
│   ├── main.py
│   ├── speech.py
│   ├── websites.py
│   ├── applications.py
│   └── commands.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Start Chitti

Open the terminal inside the project folder and run:

```bash
py -m assistant.main
```

### 3. Give a voice command

For example:

```text
Open YouTube
Open W3Schools
Open LeetCode
Search Python functions
Open Calculator
Stop Chitti
```

## Future Improvements

* Control the computer using voice
* Add more applications
* Add more natural conversations
* Add weather information
* Add reminders
* Add AI-powered question answering
* Add more voice commands


