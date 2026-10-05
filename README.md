# Chitti-Voice-Assistant 🤖

**Chitti — Voice Assistant** is a Python-based voice assistant for Windows. It listens to voice commands and performs actions such as opening websites, searching Google, and launching Windows applications.

## Features

* 🎤 Voice command recognition
* 🔊 Voice responses
* 🌐 Open websites using voice commands
* 🔎 Google search using voice
* 🖥️ Launch Windows applications
* 🌐 Open Chrome
* 👋 Greeting commands
* 🛑 Stop/exit commands
* 🎧 Microphone noise calibration

## Modules / Libraries Used

* **Python**
* **SpeechRecognition** — voice recognition
* **PyAudio** — microphone input
* **pyttsx3** — voice responses
* **webbrowser** — opening websites
* **subprocess** — launching Windows applications
* **urllib.parse** — processing search queries

## Supported Websites

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

## Supported Windows Applications

* Calculator
* Notepad
* Paint
* File Explorer
* Command Prompt
* PowerShell
* Task Manager
* Chrome

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Chitti-Voice-Assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Chitti

```bash
py -m assistant.main
```

## Example Voice Commands

```text
"Hello Chitti"
"Good morning Chitti"
"Open YouTube"
"Open GitHub"
"Search Python functions"
"Open Calculator"
"Open Chrome"
"Stop Chitti"
```

## How It Works

1. 🎤 Chitti listens to your voice.
2. 🧠 Speech recognition converts voice into text.
3. ⚙️ Chitti identifies the command.
4. 💻 The requested action is performed.
5. 🔊 Chitti responds with voice.
