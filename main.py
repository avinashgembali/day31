from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# reading the data from csv file
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def flashing():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_back, image=frontImage)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_front, image=back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    flashing()


window = Tk()
window.title("flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
back_image = PhotoImage(file="images/card_back.png")
card_back = canvas.create_image(400, 263, image=back_image)
frontImage = PhotoImage(file="images/card_front.png")
card_front = canvas.create_image(400, 263, image=frontImage)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 24, "normal"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 24, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

r_image = PhotoImage(file="images/right.png")
right = Button(image=r_image, command=is_known)
right.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right.grid(row=1, column=0)

w_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=w_image, command=flashing)
wrong.config(bg=BACKGROUND_COLOR, highlightthickness=0)
wrong.grid(row=1, column=1)

flashing()

window.mainloop()
