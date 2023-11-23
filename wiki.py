import flet as ft
from header import *
from database import *

## index             [0]
## domain TEXT       [1]
## kingdom TEXT      [2] 
## family TEXT       [3]
## species TEXT      [4] 
## description TEXT  [5]
## image TEXT        [6]

def wikipage(animal):
  
  animal_img = ft.Image(
        src = animal[6],
        width = 400,
        height = 400,
        fit = ft.ImageFit.FIT_HEIGHT,
        border_radius = 20,
    )

  description_text = ft.Text(
        animal[5],
        size = 16,
        text_align = ft.TextAlign.CENTER,
        width = 500,
        height = 400,
    )

  speciesname_text = ft.Text(
        animal[4], 
        size = 36,
        text_align = ft.TextAlign.CENTER,
        width = 400,
        height = 40,
        color = "#9DBF32",
    )

  tag_container = ft.Container(
    content = ft.Text(animal[3]),
    alignment = ft.alignment.center,
    bgcolor = "#9DBF32",
    border_radius = 20,
    width = 400,
    height = 30,
    )

  return ft.Row(controls = [
      ft.Column([speciesname_text, ft.Stack([animal_img, tag_container])]), 
      description_text], 
      alignment = ft.MainAxisAlignment.CENTER,
      spacing = 50,
    )

def return_emoji(animal):
  if animal[2] == 'Animalia':
    if animal[3] == 'Canidae':   ##🐶
      return '\U0001F436'
    elif animal[3] == 'Felidae': ##🐱
      return '\U0001F408'
    elif animal[3] == 'Ursidae': ##🐻
      return '\U0001F43B'
  elif animal[2] == 'Plantae':   ##🌱
    return '\U0001F331'
  elif animal[2] == 'Fungi':     ##🍄
    return '\U0001F344'
  else:                          ##🔎
    return '\U0001F50E'
