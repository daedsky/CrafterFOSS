from components import custom_controls as cc
import flet as ft

# type hinting <start>
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from views.install_layout import InstallLayout


# type hinting <end>

def install(install_layout: 'InstallLayout') -> None:
    dlg = cc.InfoAlertDialog(page=install_layout.page,
                             content_text='',
                             title_text='FOSS')
    dlg.content = ft.Text(spans=[
        ft.TextSpan('This is the FOSS version of the app. Please install Non FOSS version of the the app '),
        ft.TextSpan('from here', url='https://github.com/daedsky/Crafter/releases',
                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, color=ft.Colors.BLUE,
                                       decoration_color=ft.Colors.BLUE)),
        ft.TextSpan(' to use this feature.')
    ])
    dlg.show()
