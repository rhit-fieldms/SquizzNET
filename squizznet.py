#from squizz import squizznet
#import markiplier
import transformers
import flet as ft
from flet import IconButton, Page, Row, TextField, icons, Image, ElevatedButton
from transformers import pipeline, set_seed


from transformers import GPT2Tokenizer, GPT2Model


print("squizz on them")

def main(page: ft.Page):
    page.title = "SquizzNET™"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    jamison = ft.Image(src=f"ezgif.com-crop.gif")
    def button_clicked(e):
        b.data += 1
        t.value = f"Squizzed {b.data} time(s)"
        page.update()

    b = ft.ElevatedButton("Press to Squizz", on_click=button_clicked, data=0)
    t = ft.Text()
    page.add(
        ft.Row(
            [
                ft.Text(value="Welcome to SquizzNET™", text_align=ft.TextAlign.RIGHT)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ), ft.Row([jamison], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([b, t], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)

generator = pipeline('text-generation', model='gpt2')
set_seed(42)
generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)