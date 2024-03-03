import datetime
import os
import pystray
from PIL import Image, ImageDraw, ImageFont
import ctypes

def get_current_week():
    now = datetime.datetime.now()
    return now.strftime("%U")

def on_left_click(icon, item):
    week = get_current_week()
    ctypes.windll.user32.MessageBoxW(0, f"Current Week: {week}", "Week Widget", 0)

def create_menu():
    menu = pystray.Menu(
        pystray.MenuItem("Show Week", on_left_click),
        pystray.MenuItem("Exit", lambda: icon.stop()),
    )
    return menu

def create_icon():
    icon_path = os.path.abspath("week_icon.ico")
    week = get_current_week()
    image = Image.new("RGB", (32,32), "white")
    draw = ImageDraw.Draw(image)

    # Increase font size
    font_size = 24

    # Load a TrueType font with the specified size
    font = ImageFont.truetype("arial.ttf", font_size)

    draw.text((3,3), week, fill="black", font=font)
    icon = pystray.Icon("Week Widget", image, "Current Week", create_menu())
    return icon

if __name__ == "__main__":
    icon = create_icon()
    icon.run()
