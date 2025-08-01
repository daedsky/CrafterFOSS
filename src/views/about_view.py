import flet as ft
from components import custom_controls as cc
from models.app_info import AppInfo

# type hinting <start>
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.app import CrafterApp


# type hinting <end>


class AboutLayout(ft.Column):
    def __init__(self, app: 'CrafterApp', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app: 'CrafterApp' = app
        self.page: ft.Page = app.page
        self.controls: list[ft.Control] = self.get_layout()

    @staticmethod
    def url_openable_text(non_clickable_text: str, clickable_text: str, urlink: str) -> ft.Text:
        return ft.Text(spans=[ft.TextSpan(non_clickable_text),
                              ft.TextSpan(clickable_text, style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                                          url=urlink)],
                       size=16)

    def get_layout(self):
        IMAGE_APPICON = ft.Container(ft.Image(src='/icon.png', width=100, height=100), padding=5,
                                     bgcolor=ft.Colors.SECONDARY_CONTAINER, border_radius=21)
        LABEL_APPNAME = ft.Text(value='Crafter for BootAnimation', text_align=ft.TextAlign.CENTER, size=18,
                                weight=ft.FontWeight.BOLD, color=ft.Colors.PRIMARY)

        LABEL_APP_VERSION = ft.Text(value=AppInfo.VERSION, color=ft.Colors.TERTIARY)

        container_first = ft.Container(
            content=ft.Column([ft.Row(controls=[IMAGE_APPICON], alignment=ft.MainAxisAlignment.CENTER),
                               ft.Row(controls=[LABEL_APPNAME], alignment=ft.MainAxisAlignment.CENTER),
                               ft.Row(controls=[LABEL_APP_VERSION], alignment=ft.MainAxisAlignment.CENTER)]
                              ),
            border_radius=8
        )
        LABEL_MADE_WITH = self.url_openable_text(non_clickable_text='Made With: ', clickable_text='Python',
                                                 urlink='https://python.org')

        LABEL_GIT_REPO = self.url_openable_text(non_clickable_text='Source Code available at: ',
                                                clickable_text='Github',
                                                urlink=AppInfo.GIT_REPO_URL)

        icon_python = ft.Image(src='/python_icon.png', width=20, height=20)

        container_made_with = cc.CardViewContainer(icon=ft.Icons.CODE_ROUNDED, title_text='Open Source',
                                                   content_controls=[
                                                       ft.Row([LABEL_MADE_WITH, icon_python]),
                                                       ft.Row([LABEL_GIT_REPO])
                                                   ])

        LABEL_LIB_FLET = self.url_openable_text(non_clickable_text='', clickable_text='Flet',
                                                urlink='https://flet.dev')
        LABEL_LIB_PILLOW = self.url_openable_text(non_clickable_text='', clickable_text='Pillow',
                                                  urlink=
                                                  'https://python-pillow.github.io/')
        LABEL_LIB_PYJNIUS = self.url_openable_text(non_clickable_text='', clickable_text='Pyjnius',
                                                   urlink=
                                                   'https://pyjnius.readthedocs.io')
        container_libraries = cc.CardViewContainer(icon=ft.Icons.EXTENSION_ROUNDED, title_text='Libraries Used',
                                                   content_controls=[
                                                       LABEL_LIB_FLET, LABEL_LIB_PILLOW, LABEL_LIB_PYJNIUS
                                                   ])
        LABEL_MIT_LICENSE = self.url_openable_text(non_clickable_text='MIT License (No warranty or guarantee) ',
                                                   clickable_text='[Full Text]',
                                                   urlink=AppInfo.APP_LICENSE_URL)
        LABEL_PRIVACY_POLICY = self.url_openable_text(non_clickable_text='Privacy Policy ', clickable_text='[see here]',
                                                      urlink=AppInfo.PRIVACY_POLICY_URL)
        container_privacy_policy = cc.CardViewContainer(icon=ft.Icons.PRIVACY_TIP_OUTLINED,
                                                        title_text='License & Privacy Policy',
                                                        content_controls=[
                                                            LABEL_MIT_LICENSE,
                                                            LABEL_PRIVACY_POLICY
                                                        ])
        structure = [
            container_first,
            container_made_with,
            container_libraries,
            container_privacy_policy
        ]

        return structure


class AboutView(ft.View):
    def __init__(self, app: 'CrafterApp', *args, **kwargs):
        super().__init__(*args, **kwargs, scroll=ft.ScrollMode.AUTO)
        self.app: 'CrafterApp' = app
        self.page: ft.Page = app.page
        self.appbar = cc.ReturnHomeAppBar('About')
        self.controls: list[ft.Control] = [AboutLayout(app=self.app)]
