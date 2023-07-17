from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"

# print(os.getcwd())
current_card = {}
to_learn = {}

def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(".\\data\\words_to_learn.csv", index = False)
    next_card()

def next_card():
    global current_card
    global flip_timer
    
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill = "black")
    canvas.itemconfig(canvas_image, image = card_front)
    flip_timer = window.after(3000, flip)
    
    
def flip():
    global current_card
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(canvas_image, image = card_back)
    canvas.itemconfig(card_word,text=current_card["English"], fill = "white")


window = Tk()
window.title("Flashy")
# window.minsize(width=900, height=600)
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

card_front = PhotoImage(file=".\\images\\card_front.png")
card_back = PhotoImage(file=".\\images\\card_back.png")
right_image = PhotoImage(file=".\\images\\right.png")
wrong_image = PhotoImage(file=".\\images\\wrong.png")

button_right = Button(image=right_image, highlightthickness=0,command=is_known)
button_right.grid(row=1, column=1)
button_wrong = Button(image=wrong_image, highlightthickness=0,command=next_card)
button_wrong.grid(column=0, row=1)

canvas= Canvas(width=800, height=526,highlightthickness=0)
canvas_image = canvas.create_image(400,263,image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_title = canvas.create_text(400, 150, text="French", font=("Ariel",40, "italic"))
# label_french.place(relx=400, rely=150)

try:
    data = pandas.read_csv(".\\data\\words_to_learn.csv")
except FileNotFoundError:        
    orgiginal_data = pandas.read_csv(".\\data\\french_words.csv")
    to_learn = orgiginal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# french_dict = {row.French: row.English for (index,row) in french_words.iterrows()}
# res = key, val = random.choice(list(french_dict.items()))
# french_dict_list = to_learn.to_dict(orient="records")

card_word = canvas.create_text(400, 253, text="word", font=("Ariel",60, "bold"))

flip_timer = window.after(3000, flip)

next_card()
window.mainloop()