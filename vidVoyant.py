# vidVoyant.py

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'GUI'))

from vshort_ui import main  # from GUI/vshort_ui.py

import flet as ft
ft.app(target=main)  # 👈 launch app here
