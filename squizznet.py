#from squizz import squizznet
#import markiplier
import transformers
import flet as ft
from flet import IconButton, Page, Row, TextField, icons, Image, ElevatedButton
from transformers import pipeline, set_seed


from transformers import GPT2Tokenizer, GPT2Model


print("squizz on them")

page = ft.Page
qTopic = ''
view = ''

def quizzMake(page: ft.Page):
    page.title = "SquizzNET™"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    qTopic = ft.TextField()
    def button_clicked(e):
        print('peepee')
    page.add(
        ft.Row([
                ft.Text(value="Provide a specific topic for your Squizz", text_align=ft.TextAlign.RIGHT)
            ],
            alignment=ft.MainAxisAlignment.CENTER), 
        ft.Row([qTopic], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton("Generate Squizz", on_click=button_clicked)], alignment=ft.MainAxisAlignment.CENTER)
    )

def displayQuiz(page: ft.Page):
    print('funny')
    # generator = pipeline('text-generation', model='gpt2')
    # set_seed(42)
    # generator("Make a quiz about " + qTopic, num_return_sequences=1)

def welcomeToSquizz():
    jamison = ft.Image(src=f"ezgif.com-crop.gif")
    b = ft.ElevatedButton("Press to Squizz", on_click=button_clicked)
    page.add(ft.Column(
        horizontal_alignment = ft.MainAxisAlignment.CENTER,
        controls = [
            ft.Row(
            [
                ft.Text(value="Welcome to SquizzNET™", text_align=ft.TextAlign.RIGHT)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ), ft.Row([jamison], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([b], alignment=ft.MainAxisAlignment.CENTER)
        ]    
    ))
    return view

def button_clicked(e):
        page.remove(view)
        page.views.append(quizzMake)
        #page.update()

def main(page: ft.Page):
    page.title = "SquizzNET™"
    #view = welcomeToSquizz()
    page.add(welcomeToSquizz())
    # page.remove(view)
    

ft.app(target=main)

