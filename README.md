# Screen Capture and AI Analysis with Ollama

## Overview
This project captures a specific screen (useful if you have multiple screens) and sends the captured image to **Ollama**, an open-source LLM for vision-based predictions.

## Features
- Capture a specific screen
- Save the screenshot locally
- Send the image to **Ollama** for AI-based analysis
- Display AI-generated insights from the screenshot

## Prerequisites
Ensure you have the following dependencies installed:

Downaload Install Tesseract : https://github.com/UB-Mannheim/tesseract/wiki
Copy install path and paste to : pytesseract.pytesseract.tesseract_cmd
For example:  r"C:\Users\Test\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

```sh
pip install mss opencv-python numpy pillow requests pytesseract ollama
```

You also need to **install Ollama** if you haven't already:
```sh
curl -fsSL https://ollama.ai/install.sh | sh
```

## Setup
1. **Run Ollama with a vision model** (e.g., `llama3.2`):
   ```sh
   ollama pull llama3.2
   ```
2. **Run the script**
   ```sh
   python screen_capture_ai.py
   ```

## Usage
1. **Run Ollama in the background** with the LLaVA model:
   ```sh
   ollama run llava
   ```
2. **Run the script and capture screenshots**
   ```sh
   python screen_capture_ai.py
   ```
3. Press `Enter` to capture a screenshot.
4. The AI will analyze the image and provide a response.
5. Type `q` to exit.

## License
This project is open-source and can be modified as needed.
