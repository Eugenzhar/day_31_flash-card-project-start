from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
#print(data)
to_learn = data.to_dict(orient="records")
print(to_learn)

def next_card():
    curent_card = random.choice(to_learn)
    print(curent_card["French"])


window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images\card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 260, text="word", font=("Ariel", 60, "bold"))


# Button
def red_button_clicked():
    print("red button clicked")


cross_image = PhotoImage(file="images\wrong.png")
red_button = Button(image=cross_image, command=next_card)
red_button.grid(column=0, row=1)
red_button.config(highlightthickness=0)


def green_button_clicked():
    print("green button clicked")


check_image1 = PhotoImage(file="images/right.png")
green_button = Button(image=check_image1,highlightthickness=0, command=next_card)
green_button.grid(column=1, row=1)
green_button.config(highlightthickness=0)

window.mainloop()
