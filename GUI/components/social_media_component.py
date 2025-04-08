import flet as ft

def create_social_media_section(page: ft.Page):
    # Section: Social Media
    return ft.Container(
        content=ft.Column([
            ft.Text("3️⃣ Connect your social media account (Optional)", size=20, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("Upgrade to Premium to automatically post to your social media channels. Upgrade now", bgcolor=ft.colors.ORANGE, color=ft.colors.WHITE),
            ft.Dropdown(label="Choose or connect a social Media account", options=[ft.dropdown.Option("Choose or connect a social Media account")]),
            ft.Row([
                ft.Image(src="https://storage.googleapis.com/a1aa/image/lD9KQAZ3nNhFEeWDTn86ucZPk0_zg36z89kU882zyMA.jpg", width=30, height=30),
                ft.Text("YouTube", color=ft.colors.GREY_800)
            ])
        ], spacing=15),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.GREY_300)
    )