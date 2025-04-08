import flet as ft

def create_voice_section(page: ft.Page):
    # Section: Voice Selection
    voices = [
        ("aloy", "Warm and conversational"),
        ("echo", "Clear and friendly"),
        ("fable", "Soothing and soft"),
        ("nova", "Engaging and bright"),
        ("onyx", "Deep and authoritative")
    ]
    voice_cards = [
        ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.PLAY_CIRCLE_OUTLINE, color=ft.colors.GREY),
                ft.Text(name, expand=1),
                ft.Text("OpenAI", color=ft.colors.GREY),
                ft.Text(desc, color=ft.colors.GREY),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=10,
            border=ft.border.all(1, ft.colors.GREY_300),
            border_radius=8
        )
        for name, desc in voices
    ]
    return ft.Container(
        content=ft.Column([
            ft.Text("2️⃣ Select your voice", size=20, weight=ft.FontWeight.BOLD),
            ft.TextField(hint_text="Search Voice..."),
            *voice_cards
        ], spacing=15),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.GREY_300)
    )