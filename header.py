import flet as ft
from database import *

page_emoji = u'\U00002753' 
animal = c.fetchone()

def theme(thisPage, primaryColor, primaryContainer):
    thisPage.theme = ft.Theme(
        color_scheme = ft.ColorScheme(
        primary = primaryColor, ##ft.colors.GREEN,
        primary_container = primaryContainer, ##ft.colors.GREEN_200,
        )
    )

def page_style(pageName):
    pageName.title = 'bio.log'
    pageName.fonts = {
        "DMSans": 'https://github.com/CeloEug/BIO.LOG/raw/main/DMSans-VariableFont_opsz,wght.ttf'
    }
    theme(pageName, '#9DBF32', ft.colors.GREEN_200)
    pageName.bgcolor = '#0A141B'

def biolog_logohalf():
    return ft.Text(
    f"BIO.",
    size = 40,
    weight=ft.FontWeight.BOLD,
    font_family= "DMSans",
    color = '#D2D2D2')

def biolog_logocomplete(emoji):
    return ft.Text(
    f"LOG({emoji})",
    size = 40,
    weight=ft.FontWeight.BOLD,
    font_family= "DMSans",
    color =  "#9DBF32")
                        
def menu_tabs():
    return ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text="Add something"), 
            ft.PopupMenuItem(text="Show something") 
            ]
    )

