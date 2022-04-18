from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
#print(data)
to_learn = data.to_dict(orient="records")
#print(to_learn)
curent_card = {}

def next_card():
    global curent_card, flip_timer
    window.after_cancel(flip_timer)
    curent_card = random.choice(to_learn)
    print(curent_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=curent_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curent_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(curent_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images\card_front.png")
card_back_img = PhotoImage(file="images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 260, text="word", font=("Ariel", 60, "bold"))


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
green_button = Button(image=check_image1,highlightthickness=0, command=is_known)
green_button.grid(column=1, row=1)
green_button.config(highlightthickness=0)

next_card()

window.mainloop()
