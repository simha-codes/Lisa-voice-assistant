# Lisa - AI Voice Assistant

**Lisa** is a Python-based voice assistant that can perform various tasks such as searching Wikipedia, opening websites, playing music, launching applications, and system operations like shutdown or lock. Lisa is activated using the wake word "Lisa" and responds to voice commands.

---

## Features

* **Wake Word Detection**: Listens for the wake word "Lisa" to activate.
* **Wikipedia Search**: Answers general questions and provides summaries.
* **Website Launcher**: Opens Google, YouTube, Instagram, LinkedIn, and VTOP portals.
* **Music Playback**: Plays songs from a predefined music library.
* **Application Launcher**: Opens Calculator, Notepad, and Command Prompt.
* **System Commands**: Shutdown, restart, or lock the computer.
* **Voice Feedback**: Provides audio responses using text-to-speech.

---

## Installation

1. **Clone the repository**:

```bash
git clone <repository_link>
cd <repository_folder>
```

2. **Install dependencies**:

```bash
pip install pyttsx3 speechrecognition wikipedia
```

> **Note:** `musiclib.py` should be present in the same folder as `lisa.py`.

3. **Windows Only**: Uses `sapi5` TTS engine for voice output.

---

## Usage

1. Run the main script:

```bash
python lisa.py
```

2. Lisa will initialize and listen for the wake word "Lisa".

3. Example commands:

* "Lisa, open Google"
* "Lisa, play Despacito"
* "Lisa, open calculator"
* "Who is Albert Einstein?"
* "Lisa off" (to stop Lisa)

---

## Code Structure

```
lisa.py          # Main Python script
musiclib.py      # Contains music library dictionary
README.md        # Project documentation
```

---

## Key Learnings

* Implemented speech recognition and text-to-speech.
* Controlled system applications and web browsers via Python.
* Integrated Wikipedia API for information retrieval.
* Developed wake word detection for interactive voice control.

---

## Future Improvements

* Add natural conversation capabilities.
* Expand music library.
* Cross-platform support (Linux/macOS).
* Contextual command understanding using AI.

---

## License

This project is for educational purposes. You can freely use and modify it for learning and personal projects.
