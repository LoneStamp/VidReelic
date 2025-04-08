# config/icon.py

import os

def get_icon_path():
    icon_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "public", "assets", "icons", "vidVoyant.ico")
    )
    print(f"Icon path resolved to: {icon_path}")  # For debugging
    return icon_path
