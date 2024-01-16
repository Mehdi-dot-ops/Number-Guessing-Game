from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x600")
root.configure(bg="#5F8670")
root.title("Number Guessing")

global bt3, images, shuffle_counter, circles, target_number

image2 = Image.open("Numbers.png")
Img2 = image2.resize((500, 200))
photo2 = ImageTk.PhotoImage(Img2)
img_label2 = Label(root, image=photo2, bg="#5F8670")
img_label2.image = photo2
img_label2.place(x=-3, y=400)

secret_number = "none"


def On_Click(event):
    btn = event.widget
    buttonText = btn.cget("text")

    if secret_number == buttonText:
        answer_label.config(text="You Guessed Correct.")
        answer_label.place(x=120, y=470)

        secret_label.configure(text=f"Secret Number Was '{secret_number}'",
                               font=("Copperplate Gothic Light", 15, "bold"), fg="#FF9800", bg="#5F8670")
        secret_label.place(x=110, y=440)

        Start_Game()

    else:
        answer_label.config(text="Wrong! Please Try Again.")
        answer_label.place(x=105, y=470)


def Start_Game():
    global secret_number

    for button in button_list:
        button.config(text=str(random.randint(10, 100)))

    randomButton = random.choice(button_list)
    secret_number = randomButton.cget("text")
    print("Secret Number is: ", secret_number)

    global images, shuffle_counter, circles

    bt1.destroy()

    l2 = Label(root, text=f"Guess The Secret Number", fg="#FF9800", bg="#5F8670",
               font=("Copperplate Gothic Light", 15, "bold"))
    l2.place(x=100, y=410)

    def shuffle():
        btn3 = Button(root, text="Shuffle", command=Start_Game, bg="#FF9800",
                      font=("Copperplate Gothic Light", 10, "bold"), bd=10, width=8)
        btn3.place(x=100, y=350)

        bt1.destroy()

        lbl2 = Label(root, text=f"Guess The Secret Number", fg="#FF9800", bg="#5F8670",
                     font=("Copperplate Gothic Light", 15, "bold"))
        lbl2.place(x=100, y=410)

    shuffle()


def Quit():
    bt4.configure(text="Quit", command=Quit, bg="#FF9800", font=("Copperplate Gothic Light", 10, "bold"),
                  bd=10, width=8)
    bt4.place(x=300, y=350)
    root.destroy()


bt1 = Button(root, text="Let's Play", command=Start_Game, bg="#FF9800", font=("Copperplate Gothic Light", 10, "bold"),
             bd=10, width=8)
bt1.place(x=100, y=350)

bt4 = Button(root, text="Quit", command=Quit, bg="#FF9800", font=("Copperplate Gothic Light", 10, "bold"),
             bd=10, width=8)
bt4.place(x=300, y=350)

button_one = Button(root, text="0", font=("Copperplate Gothic Light", 20, "bold"), bg="#FF9800", bd=20, pady=8)
button_one.place(x=50, y=100)

button_two = Button(root, text="0", font=("Copperplate Gothic Light", 20, "bold"), bg="#FF9800", bd=20, pady=8)
button_two.place(x=198, y=100)

button_three = Button(root, text="0", font=("Copperplate Gothic Light", 20, "bold"), bg="#FF9800", bd=20, pady=8)
button_three.place(x=345, y=100)

button_list = [button_one, button_two, button_three]

answer_label = Label(root, text="", font=("Copperplate Gothic Light", 15, "bold"), fg="#FF9800", bg="#5F8670")
answer_label.place(x=100, y=440)

secret_label = Label(root, text=f"",
                     font=("Copperplate Gothic Light", 15, "bold"), fg="#FF9800", bg="#5F8670")
secret_label.place(x=110, y=440)

button_one.bind("<Button-1>", On_Click)
button_two.bind("<Button-1>", On_Click)
button_three.bind("<Button-1>", On_Click)

Start_Game()

root.mainloop()
