import flet as ft

def create_generation_mode_section(page: ft.Page):
    # Section: Generation Mode
    return ft.Container(
        content=ft.Column([
            ft.Text("4️⃣ Select your generation mode", size=20, weight=ft.FontWeight.BOLD),
            ft.RadioGroup(
                options=[
                    ft.Radio(value="video", label="Video", selected=True),
                    ft.Radio(value="audio", label="Audio"),
                    ft.Radio(value="image", label="Image"),
                ],
                value="video",
                on_change=lambda e: print(f"Selected: {e.value}")
            )
        ], spacing=15),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.GREY_300)
    )