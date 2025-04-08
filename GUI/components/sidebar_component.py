import flet as ft

def create_sidebar(page: ft.Page):
    # Sidebar
    sidebar = ft.Container(
        content=ft.Column([
            ft.Image(
                src="https://storage.googleapis.com/a1aa/image/fMzfbP_sMUfGgmy719zRpwglc626eXM_j9QUPoXnxe8.jpg",
                width=40,
                height=40,
                border_radius=ft.border_radius.all(50)
            ),
            ft.TextButton("Dashboard", on_click=lambda _: None),
            ft.TextButton("Video Series", on_click=lambda _: None),
            ft.TextButton("Social Accounts", on_click=lambda _: None),
            ft.TextButton("Settings", on_click=lambda _: None),
        ], spacing=10),
        padding=20,
        width=250,
        bgcolor=ft.colors.WHITE,
        height=page.height,
        border_radius=ft.border_radius.all(0),
        shadow=ft.BoxShadow(blur_radius=4, 
        color=ft.colors.GREY_300)
    )
    return sidebar