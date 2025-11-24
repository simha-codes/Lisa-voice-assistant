Lisa - Python Desktop Voice Assistant
Lisa is a lightweight, Python-based desktop voice assistant designed to automate daily tasks on
Windows. It utilizes speech recognition to execute system commands, browse the web, play music, and
fetch information from Wikipedia.
🌟 Features
Wake Word Detection: The assistant stays in standby mode until it hears the wake word "Lisa".
Web Automation: Opens popular websites (Google, YouTube, Instagram, LinkedIn) and university
portals (VTOP).
System Control: Opens system applications (Calculator, Notepad, Command Prompt) and
handles power options (Shutdown, Restart, Lock).
Knowledge Retrieval: Automatically searches Wikipedia when asked questions starting with
"Who", "What", "Explain", etc.
Music Playback: Plays songs from a user-defined library.
Continuous Listening: Stays active until told to sleep or stop.
🛠️ Prerequisites & Installation
1. Python
Ensure you have Python 3.6+ installed on your system.
2. Install Dependencies
Open your terminal or command prompt and run the following command to install the required
libraries:
pip install speechrecognition pyttsx3 wikipedia
Note on PyAudio: The speech_recognition library requires PyAudio to access the
microphone.
Windows: If pip install pyaudio fails, you may need to download the .whl file for
your specific Python version from Christoph Gohlke's library or use:
pip install pipwin
pipwin install pyaudio
