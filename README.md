
Lisa - Python Desktop Voice Assistant

Lisa is a lightweight, Python-based desktop voice assistant designed to automate daily tasks on Windows. It utilizes speech recognition to execute system commands, browse the web, play music, and fetch information from Wikipedia.

🌟 Features

Wake Word Detection: The assistant stays in standby mode until it hears the wake word "Lisa".

Web Automation: Opens popular websites (Google, YouTube, Instagram, LinkedIn) and university portals (VTOP).

System Control: Opens system applications (Calculator, Notepad, Command Prompt) and handles power options (Shutdown, Restart, Lock).

Knowledge Retrieval: Automatically searches Wikipedia when asked questions starting with "Who", "What", "Explain", etc.

Music Playback: Plays songs from a user-defined library.

Continuous Listening: Stays active until told to sleep or stop.

🛠️ Prerequisites & Installation

1. Python

Ensure you have Python 3.6+ installed on your system.

2. Install Dependencies

Open your terminal or command prompt and run the following command to install the required libraries:

pip install speechrecognition pyttsx3 wikipedia


Note on PyAudio: The speech_recognition library requires PyAudio to access the microphone.

Windows: If pip install pyaudio fails, you may need to download the .whl file for your specific Python version from Christoph Gohlke's library or use:

pip install pipwin
pipwin install pyaudio


Linux/Mac: You may need to install portaudio headers (e.g., sudo apt-get install python3-pyaudio).

3. Create the Music Library

The code relies on a local file named musiclib.py. You must create this file in the same directory as your main script.

Create musiclib.py:

# musiclib.py

# Dictionary mapping song names (lowercase) to URLs
music = {
    "stealth": "[https://www.youtube.com/watch?v=U47Tr9BB_wE](https://www.youtube.com/watch?v=U47Tr9BB_wE)",
    "march": "[https://www.youtube.com/watch?v=Xqeq4b5u_Xw](https://www.youtube.com/watch?v=Xqeq4b5u_Xw)",
    "skyfall": "[https://www.youtube.com/watch?v=DeumyOzKqgI](https://www.youtube.com/watch?v=DeumyOzKqgI)",
    # Add your own songs here following the format: "song_name": "url"
}


🚀 Usage

Run the main Python script:

python main.py


Wait for the initialization message: "Initializing Lisa...".

The console will print "Listening for wake word 'Lisa'...".

Say "Lisa" to activate the assistant.

Once active, Lisa will say "Yes, I am listening". You can now give commands.

🗣️ Command Reference

Here is the list of commands Lisa currently understands:

General & System

Voice Command

Action

"Lisa"

Wakes up the assistant from standby.

"Lisa off" / "Stop listening"

Deactivates active mode and returns to standby.

"Open Calculator"

Launches Windows Calculator.

"Open Notepad"

Launches Windows Notepad.

"Open Command Prompt" / "CMD"

Opens the terminal.

"Shutdown"

Shuts down the PC (1-second delay).

"Restart"

Restarts the PC.

"Lock"

Locks the workstation immediately.

Web Browsing

Voice Command

Action

"Open Google"

Opens https://www.google.com/search?q=Google.com in default browser.

"Open YouTube"

Opens YouTube.com.

"Open Instagram"

Opens Instagram.com.

"Open LinkedIn"

Opens LinkedIn.com.

"Open VTOP Bhopal"

Opens VIT Bhopal VTOP portal.

"Open VTOP Chennai"

Opens VIT Chennai VTOP portal.

Media & Knowledge

Voice Command

Action

"Play [song name]"

Plays a song defined in musiclib.py. 



 Example: "Play Skyfall"

"Who is [name]"

Fetches a summary from Wikipedia.

"What is [thing]"

Fetches a summary from Wikipedia.

"Tell/Describe/Explain [topic]"

Fetches a summary from Wikipedia.

⚠️ Troubleshooting

1. "PyAudio" error during installation:
Refer to the installation section above. This is the most common issue on Windows machines.

2. Microphone not recognized:
Ensure your default microphone is set correctly in Windows Sound Settings.

3. "Sorry, I couldn't find information about that":
This occurs if the Wikipedia search is ambiguous or if there is no internet connection. Try being more specific with your query.

4. "Sorry, I can't find that song":
Ensure the song name you are saying matches a key in your musiclib.py dictionary exactly.

📜 License

This project is open-source and free to use.
