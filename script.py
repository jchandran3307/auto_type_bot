import sys
import time
import pyautogui
import random

def human_type(text, delay_range=(0.01, 0.07)):
    """Types the text character by character with random human-like delays."""
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(*delay_range))

def main():
    if len(sys.argv) > 1:
        text = sys.argv[1]
        print("Typing will begin in 10 seconds... Move your cursor where you want to type.")
        time.sleep(10)  # Wait for 10 seconds before typing
        human_type(text)
        print("Typing completed!")
    else:
        print("No input provided.")

if __name__ == "__main__":
    main()
