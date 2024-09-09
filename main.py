import pyautogui
import time
from datetime import datetime, timedelta

"""
DESCRIPTION:
    A python script to interact with the keyboard using the pyautogui library. The purpose is to automate sending current location device to the whatsapp chat room.

STEPS:
1. connect mobile device into the computer
2. adb devices (then find your device)
3. use `scrcpy -s <SERIALNUMBER>` to mirror the device screen
4. run the script
5. click on the whatsapp chat room
"""


def calculate_time_until_target(hour, minute):
    now = datetime.now()
    print(f"Current time: {now}")
    target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if now > target_time:
        # If the target time is in the past today, schedule for the next day
        target_time += timedelta(days=1)

    return round((target_time - now).total_seconds())  # Round the total seconds


def log_remaining_time(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_str = f"{int(mins)} minutes and {int(secs)} seconds remaining"
        print(f"[LOG] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {time_str}")
        time.sleep(1)  # Sleep for 1 second
        seconds -= 1


key_to_press = [
    # Selecting the attachment menu
    "tab",
    "enter",
    # Selecting location button
    "tab",
    "tab",
    "tab",
    "tab",
    "tab",
    "tab",
    "tab",
    "tab",
    "tab",
    "enter",
    # Selecting "share your current location"
    "tab",
    "tab",
    "tab",
    "tab",
    "tab",
    "tab",
    "enter",
]

TIMER = 10

TARGET_HOUR = 18  # Hour when you want to run the script (8 AM)
TARGET_MINUTE = 37  # Minute when you want to run the script (00)


print(
    r"""
 ____  _____ ____    _    ____      ___ ____      _        _     _______   __
/ ___|| ____/ ___|  / \  |  _ \    |_ _/ ___|    | |      / \   |__  /\ \ / /
\___ \|  _| \___ \ / _ \ | |_) |    | |\___ \    | |     / _ \    / /  \ V / 
 ___) | |___ ___) / ___ \|  _ <     | | ___) |   | |___ / ___ \  / /_   | |  
|____/|_____|____/_/   \_\_| \_\   |___|____/    |_____/_/   \_\/____|  |_|
"""
)


# Calculate how many seconds until the target time
time_until_run = calculate_time_until_target(TARGET_HOUR, TARGET_MINUTE)

# Log time every second
print(f"Waiting until next {TARGET_HOUR}:{TARGET_MINUTE}... ({time_until_run} seconds)")
log_remaining_time(time_until_run)

# COUNTDOWN TIMER BEFORE START
for i in range(TIMER):
    print(f"Starting in {TIMER-i} ...")
    time.sleep(1)

print("Started... running...")

for key in key_to_press:
    pyautogui.press(key)
    time.sleep(0.5)

print("Script finished...")
