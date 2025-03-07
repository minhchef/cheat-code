import mss
import numpy as np
import cv2
import base64
import pytesseract
from ollama import Client
from io import BytesIO
from PIL import Image

# Configure pytesseract (ensure Tesseract OCR is installed on your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Test\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"  # Update this path if needed

def capture_screen(screen_number=1):
    with mss.mss() as sct:
        monitors = sct.monitors  # Get all screens
        if screen_number < len(monitors):
            monitor = monitors[screen_number]  # Select specific screen
            screenshot = sct.grab(monitor)
            img = np.array(screenshot)
            return img
        else:
            print("Screen number out of range")
            return None

def extract_text(image_array):
    # Convert image array to grayscale
    gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGRA2GRAY)
    # Perform OCR to extract text
    extracted_text = pytesseract.image_to_string(gray_image)
    return extracted_text.strip()

def send_to_ollama(text):
    print("Sending text to Ollama...")
    client = Client(host='http://localhost:11434')
    
    response = client.chat(model='llama3.2', messages=[
        {'role': 'user', 'content': f"Please provide a well-formatted PHP solution inside a Markdown code block for the following problem:\n\n{text}\n\nEnsure the response is clean and well-structured."},
    ])
    
    # Extract the actual response text
    if 'message' in response and 'content' in response['message']:
        formatted_response = response['message']['content']
        print("Response received from Ollama:\n", formatted_response)
        return formatted_response
    else:
        print("Unexpected response format from Ollama:", response)
        return None

if __name__ == "__main__":
    count = 1
    while True:
        user_input = input("Press Enter to capture (or type 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        
        print("Capturing screen...")
        image = capture_screen(1)
        if image is not None:
            filename = f"screenshot_{count}.png"
            cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_BGRA2BGR))  # Save screenshot
            print(f"Screenshot saved as {filename}")
            
            print("Extracting text from image...")
            extracted_text = extract_text(image)
            ##print("Extracted Text:", extracted_text)
            
            if extracted_text:
                print("Sending extracted text to Ollama for analysis...")
                send_to_ollama(extracted_text)
            
            count += 1
