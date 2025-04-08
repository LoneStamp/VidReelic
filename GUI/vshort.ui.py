# UI
import flet as ft
from config.icon import get_icon_path

# Import components
from GUI.components.sidebar_component import create_sidebar
from GUI.components.topic_component import create_topic_section
from GUI.components.voice_component import create_voice_section
from GUI.components.social_media_component import create_social_media_section
from GUI.components.genration_mode import create_generation_mode_section

def main(page: ft.Page):
    page.title = "VidVoyant"
    page.bgcolor = ft.colors.GREY_100
    page.scroll = ft.ScrollMode.AUTO
    page.window_icon = get_icon_path() 
    page.window_width = 1080
    page.window_height = 720
    page.scroll = ft.ScrollMode.HIDDEN  
   
    # Create all components
    sidebar = create_sidebar(page)
    section_main_1 = create_topic_section(page)
    section_main_2 = create_voice_section(page)
    section_main_3 = create_social_media_section(page)
    section_main_4 = create_generation_mode_section(page)
   
    page.add(
        ft.Row([
            sidebar,
            ft.Container(
                content=ft.Column([
                    ft.Text("Create New Series", size=24, weight=ft.FontWeight.BOLD),
                    section_main_1,
                    section_main_2,
                    section_main_3,
                    section_main_4
                ], expand=1, scroll=ft.ScrollMode.AUTO, spacing=30),
                padding=20,
                expand=True
            )
        ], expand=True)
    )

ft.app(target=main)# UI 
