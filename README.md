# ai-desktop-translator
A modern, lightweight Desktop AI Translator built with Python 3.13. Features a Tkinter-based GUI and utilizes the Google Translate engine via the deep-translator library for fast and accurate multi-language translation.
# AI Desktop Translator 🌍

A simple yet powerful desktop application to translate text between languages instantly using AI.

## ✨ Features
* **Auto-Language Detection:** No need to select the source language; the AI figures it out.
* **Modern GUI:** Clean interface built with Python's Tkinter.
* **Python 3.13 Compatible:** Uses the latest `deep-translator` library to avoid legacy module errors.
* **Instant Results:** Fast translation for popular languages like Hindi, Spanish, French, and German.

## 🚀 Installation

Follow these steps to get the project running on your local machine:

### 1. Prerequisites
Make sure you have **Python 3.10 or higher** installed (tested on Python 3.13).

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/ai-desktop-translator.git](https://github.com/YOUR_USERNAME/ai-desktop-translator.git)
cd ai-desktop-translator
3. Set Up a Virtual Environment (Recommended)
Creating a virtual environment keeps your project dependencies isolated and clean.

Create the environment:

Bash
python -m venv venv
Activate the environment:

Windows: ```bash .\venv\Scripts\activate

Mac/Linux: ```bash source venv/bin/activate


4. Install Dependencies
Install the necessary AI translation libraries:

Bash
pip install deep-translator
🛠️ How to Execute
To launch the application, ensure your virtual environment is active and run the following command:

Bash
python gui_translator.py
📖 How to Use
Input: Type or paste the text you want to translate in the top input box.

Select Language: Choose your target language (e.g., Hindi, Spanish, French) from the dropdown menu.

Translate: Click the "Translate Now" button.

Result: The AI will automatically detect your input language and display the translation in the bottom box.
