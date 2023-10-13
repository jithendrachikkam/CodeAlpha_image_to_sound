from PIL import Image
from gtts import gTTS
import pytesseract
import os

# Update the path to Tesseract executable if necessary
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert_to_sound(image_path):
    try:
        open_image = Image.open(image_path)
        text = pytesseract.image_to_string(open_image)
        text_file = " ".join(text.split("\n"))
        print(text_file)
        sound = gTTS(text_file, lang="en")
        sound.save("sound.mp3")
        os.system("sound.mp3")
        return True
    except Exception as e:
        print("An error occurred while executing the code:", e)
        return False

if __name__ == "__main":
    image_path = "imagetext.jpg"
    if convert_to_sound(image_path):
        print("Conversion to sound successful.")
    input()
