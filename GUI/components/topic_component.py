import flet as ft

def create_topic_section(page: ft.Page):
    # Dropdown option lists
    languages = [
        ft.dropdown.Option("English 🇺🇸"),
        ft.dropdown.Option("Filipino 🇵🇭"),
        ft.dropdown.Option("Spanish 🇪🇸"),
        ft.dropdown.Option("French 🇫🇷"),
    ]

    topics = [
        ft.dropdown.Option("Business"),
        ft.dropdown.Option("Health"),
        ft.dropdown.Option("Education"),
        ft.dropdown.Option("Motivation"),
    ]

    video_lengths = [
        ft.dropdown.Option("30-60 Seconds"),
        ft.dropdown.Option("60-90 Seconds"),
        ft.dropdown.Option("90-120 Seconds"),
    ]

    # Left container: Topic selection
    left_panel = ft.Container(
        content=ft.Column(
            [
                ft.Text("1️⃣ Select your topic", size=20, weight=ft.FontWeight.BOLD),
                ft.Dropdown(label="Language", options=languages),
                ft.Dropdown(label="Topic", options=topics),
                ft.Dropdown(label="Video Length", options=video_lengths),
                ft.ElevatedButton(
                    "Generate Script",
                    bgcolor=ft.colors.ORANGE,
                    color=ft.colors.WHITE,
                    expand=True,
                ),
            ],
            spacing=15,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.GREY_300),
    )

    # Right container: Script generation panel
    right_panel = ft.Container(
        content=ft.Column(
            [
                ft.Text("2️⃣ Script Generation", size=20, weight=ft.FontWeight.BOLD),
                ft.TextField(
                    label="Describe what your video is about",
                    multiline=True,
                    min_lines=3,
                    max_lines=5,
                    hint_text="Enter details about your video content...",
                ),
                ft.Row(
                    [
                        ft.PopupMenuButton(
                            icon=ft.icons.MODEL_TRAINING,
                            tooltip="Select AI Model",
                            items=[
                                ft.PopupMenuItem(text="OpenAI Models", disabled=True),
                                ft.PopupMenuItem(text="GPT-4"),
                                ft.PopupMenuItem(text="GPT-4 Turbo"),
                                ft.PopupMenuItem(text="GPT-3.5 Turbo"),
                                ft.PopupMenuItem(),  # divider
                                ft.PopupMenuItem(text="Claude Models", disabled=True),
                                ft.PopupMenuItem(text="Claude 3.5 Sonnet"),
                                ft.PopupMenuItem(text="Claude 3 Opus"),
                                ft.PopupMenuItem(text="Claude 3 Haiku"),
                                ft.PopupMenuItem(),  # divider
                                ft.PopupMenuItem(text="DeepSeek Models", disabled=True),
                                ft.PopupMenuItem(text="DeepSeek-Coder"),
                                ft.PopupMenuItem(text="DeepSeek-Chat"),
                                ft.PopupMenuItem(),  # divider
                                ft.PopupMenuItem(text="Anthropic Models", disabled=True),
                                ft.PopupMenuItem(text="Claude 3"),
                                ft.PopupMenuItem(text="Claude 2"),
                            ],
                        ),
                        ft.ElevatedButton(
                            "Generate Script",
                            bgcolor=ft.colors.BLUE,
                            color=ft.colors.WHITE,
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Generated Script", weight=ft.FontWeight.BOLD),
                                    ft.Row(
                                        [
                                            ft.IconButton(
                                                icon=ft.icons.COPY,
                                                tooltip="Copy to clipboard"
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.DOWNLOAD,
                                                tooltip="Download script"
                                            ),
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Container(
                                content=ft.Text(
                                    "Your generated script will appear here...",
                                    color=ft.colors.GREY_600,
                                ),
                                padding=10,
                                bgcolor=ft.colors.GREY_100,
                                border_radius=5,
                                expand=True,
                                height=300,
                            ),
                        ]
                    ),
                    padding=10,
                    bgcolor=ft.colors.WHITE,
                    border_radius=8,
                    border=ft.border.all(1, ft.colors.GREY_300),
                    margin=ft.margin.only(top=10),
                ),
            ],
            spacing=15,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.GREY_300),
    )

    # Combine both panels in a row
    return ft.Row(
        [
            left_panel,
            right_panel,
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
        expand=True,
    )