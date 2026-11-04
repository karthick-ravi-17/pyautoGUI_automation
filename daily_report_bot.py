
import pyautogui
import pyperclip
import time
import os
from datetime import datetime

# ------------------------------------
# CONFIGURATION
# ------------------------------------

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

# Create output folder
OUTPUT_DIR = os.path.join(os.getcwd(), "daily_reports")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generate current date and time
now = datetime.now()

current_date = now.strftime("%Y-%m-%d")
current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

# File paths
txt_filename = f"daily_report_{current_date}.txt"
screenshot_filename = f"daily_report_{current_date}.png"

txt_path = os.path.join(OUTPUT_DIR, txt_filename)
screenshot_path = os.path.join(
    OUTPUT_DIR, screenshot_filename
)

# ------------------------------------
# STEP 1: OPEN CHROME
# ------------------------------------

print("Opening Chrome...")

pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write("chrome", interval=0.1)
pyautogui.press("enter")

time.sleep(5)

# Navigate to weather website
weather_url = "https://wttr.in/Chennai?format=3"

pyautogui.hotkey("ctrl", "l")
pyautogui.write(weather_url, interval=0.03)
pyautogui.press("enter")

time.sleep(8)

print("Weather website opened.")

# ------------------------------------
# STEP 2: COPY WEBSITE INFORMATION
# ------------------------------------

print("Copying weather information...")

pyautogui.hotkey("ctrl", "a")
time.sleep(1)

pyautogui.hotkey("ctrl", "c")
time.sleep(2)

# Retrieve copied information
weather_data = pyperclip.paste().strip()

if not weather_data:
    weather_data = "Weather information unavailable"

# Remove unwanted line breaks
weather_data = weather_data.replace("\n", " ").strip()

print("Fetched Data:", weather_data)

# ------------------------------------
# STEP 3: PREPARE REPORT
# ------------------------------------

comment = "Check weather conditions before outdoor activities."

# Create three-column report
header = "Date & Time | Fetched Information | My Comment"

report_row = (
    f"{current_datetime} | "
    f"{weather_data} | "
    f"{comment}"
)

report_content = header + "\n" + report_row

# ------------------------------------
# STEP 4: OPEN NOTEPAD
# ------------------------------------

print("Opening Notepad...")

pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write("notepad", interval=0.1)
pyautogui.press("enter")

time.sleep(4)

# ------------------------------------
# STEP 5: ENTER REPORT DATA
# ------------------------------------

print("Entering report into Notepad...")

pyperclip.copy(report_content)

pyautogui.hotkey("ctrl", "v")

time.sleep(3)

# ------------------------------------
# STEP 6: SAVE TEXT FILE
# ------------------------------------

print("Saving report...")

pyautogui.hotkey("ctrl", "shift", "s")
time.sleep(3)

# Enter complete file path
pyperclip.copy(txt_path)
pyautogui.hotkey("ctrl", "v")

time.sleep(1)

# Save file
pyautogui.press("enter")
time.sleep(3)

# Handle possible overwrite/format dialogs
pyautogui.press("left")
pyautogui.press("enter")
time.sleep(2)

print("Text file saved:", txt_path)

# ------------------------------------
# STEP 7: TAKE SCREENSHOT
# ------------------------------------

print("Capturing Notepad screenshot...")

screenshot = pyautogui.screenshot()
screenshot.save(screenshot_path)

print("Screenshot saved:", screenshot_path)

# ------------------------------------
# STEP 8: DISPLAY FINAL STATUS
# ------------------------------------

print("\n================================")
print("DAILY REPORT BOT COMPLETED")
print("================================")

print("Date & Time:", current_datetime)
print("Fetched Data:", weather_data)
print("Text File:", txt_path)
print("Screenshot:", screenshot_path)

print("\nAutomation completed successfully!")
