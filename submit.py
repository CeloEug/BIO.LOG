import flet as ft
from header import *
from wiki import *
from database import *

def submitPage(page: ft.Page) -> None:
    
    page_style(page)

    page_emoji = '\U0001F50E'

    page.appbar = ft.AppBar(
        bgcolor = '#08141B',
        title = ft.Row(
                    spacing = 0,
                    controls = [biolog_logohalf(), biolog_logocomplete(page_emoji)]
                ),  
        actions = 
            [
                menu_tabs()
            ]
        )    

    text_title: ft.TextField = ft.TextField(
        label = 'Animal name:', 
        text_align = ft.TextAlign.LEFT, 
        width = 150,
        disabled = False)
        
    text_description: ft.TextField = ft.TextField(
        label = 'Description:', 
        text_align = ft.TextAlign.CENTER, 
        width = 630, 
        min_lines = 8,
        max_lines = 10,
        disabled = False)
    
    text_imgurl: ft.TextField = ft.TextField(
        label = 'Image URL:',
        text_align = ft.TextAlign.CENTER, 
        width = 630) 
    
    button_submit: ft.ElevatedButton = ft.ElevatedButton(
        text = 'Submit Form ⮞',
        disabled = True)
    
    domain_dropdown: ft.Dropdown = ft.Dropdown(
            label="Domain:",
            width = 150,
            options=[
                ft.dropdown.Option("Archaea"),
                ft.dropdown.Option("Bacteria"),
                ft.dropdown.Option("Eucarya"),
            ],
            autofocus=True)
    
    kingdom_dropdown: ft.Dropdown = ft.Dropdown(
            label="Kingdom:",
            width = 150,
            options=[
                ft.dropdown.Option("Animalia"),
                ft.dropdown.Option("Plantae"),
                ft.dropdown.Option("Fungi"),
                ft.dropdown.Option("Other"),
                ft.dropdown.Option("None"),
            ],
            autofocus=True)
    
    family_dropdown: ft.Dropdown = ft.Dropdown(
            label="Family:",
            width = 150,
            options=[
                ft.dropdown.Option("Felidae"),
                ft.dropdown.Option("Canidae"),
                ft.dropdown.Option("Ursidae"),
                ft.dropdown.Option("Other"),
                ft.dropdown.Option("None"),
            ],
            autofocus=True)
        
    def validate(p: ft.ControlEvent) -> None:
        if all([text_title.value, text_description.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        page.update()
        
    def fetchAnimal():
        c.execute("SELECT rowid, * FROM lifeForm ORDER BY rowid DESC LIMIT 1")
        animal = c.fetchone()
        return animal
    
    def changeRoute():
        dataAnimal = fetchAnimal()
        page.controls.pop()
        page.update()
        page_emoji = return_emoji(dataAnimal) 
        page.appbar.title.controls[1] = biolog_logocomplete(page_emoji)  
        page.controls.append(wikipage(dataAnimal))
        page.update()

    def submit(e: ft.ControlEvent) -> None:
        c.execute('''
        INSERT INTO lifeForm (domain, kingdom, family, species, description, image)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (domain_dropdown.value, kingdom_dropdown.value, family_dropdown.value, text_title.value, text_description.value ,text_imgurl.value))
    
        conn.commit()
        changeRoute()

    def submitPage():
        return ft.Column(  
                    controls = 
                    [         
                        ft.Row([text_title, domain_dropdown, kingdom_dropdown, family_dropdown], alignment = ft.MainAxisAlignment.CENTER), 
                        ft.Row([text_description], alignment = ft.MainAxisAlignment.CENTER),
                        ft.Row([text_imgurl], alignment = ft.MainAxisAlignment.CENTER),
                        ft.Row([button_submit], alignment = ft.MainAxisAlignment.CENTER)
                    ], 
                )

    text_title.on_change = validate
    text_description.on_change = validate 
    button_submit.on_click = submit
        
    page.add(
            submitPage())

ft.app(target = submitPage, use_color_emoji=True ,view = ft.AppView.WEB_BROWSER)
conn.close()
