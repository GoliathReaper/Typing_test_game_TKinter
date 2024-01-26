import customtkinter
from data import text
from random import randint

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("640x320")
app.title('Typing Test')
app.columnconfigure((0, ), weight=1, uniform='a')
app.rowconfigure((3, ), weight=1, uniform='a')

text = text[randint(0, 3)]
running = True
time_ = 60


def start():
    global running
    running = True
    timer()
    print("button pressed")


def restart():
    global time_, running
    running = False
    time_ = 60
    label.configure(text=f"{time_}s", font=('Ariel', 20))
    user_input.delete(1.0, "end")
    print("button pressed")


def get_text(textbox, text):
    t = textbox.get("0.0", "end")
    user_input = len(t.split(' '))
    for i in text:
        print(i)
    customtkinter.CTk.after(app, 1000, get_text, user_input, text)
    return


def score(user_text, text):
    user = user_text.get("0.0", "end")
    actual_text = text.split(' ')[0:len(user.split(' '))]

    count = 0
    if running:
        for item in actual_text:
            if item in user.split(' '):
                count += 1
        accuracy = count / len(actual_text) * 100
        wpm = len(user)/5
        print(wpm, accuracy)
        return wpm, accuracy


def timer():
    global time_, running
    if running:
        label.configure(text=f"{time_}s", font=('Ariel', 20))
        customtkinter.CTk.after(app, 1000, timer)
        time_ -= 1
        print(time_)
        wpm, accuracy = score(user_input, text)
        if time_ < 1:
            label.configure(text=f"WPM: {wpm} | Accuracy: {accuracy}")
            running = False


label = customtkinter.CTkLabel(master=app, text="60s", font=('Ariel', 20))
label.grid(row=0, column=0, padx=20, pady=20)


textbox = customtkinter.CTkTextbox(app, corner_radius=16, border_width=1)
textbox.insert("0.0", text)  # insert at line 0 character 0
textbox.configure(state="disabled")  # configure textbox to be read-only
textbox.grid(row=1, column=0, padx=20, pady=20, sticky='nswe')

user_input = customtkinter.CTkTextbox(app, corner_radius=16, border_width=1)
user_input.grid(row=2, column=0, padx=20, pady=20, sticky='nswe')

# button to start the test
button = customtkinter.CTkButton(master=app, text="Start", command=start)
button.grid(row=3, column=0, padx=0, pady=0)

button1 = customtkinter.CTkButton(master=app, text="Restart", command=restart)
button1.grid(row=4, column=0, padx=0, pady=20)


app.mainloop()
