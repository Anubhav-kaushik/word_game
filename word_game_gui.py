from tkinter import *
import word_game as wgame


# Global variables
play_screen = ""
correct_score_entry = ""
incorrect_score_entry = ""
na_score_entry = ""


# Functions
def escalate():
    pass


def show_word():
    global play_screen

    question = wgame.play()

    word_frame = Frame(play_screen, bg="#ff9f88")
    word_frame.pack(side="left", fill="both", expand=True)

    word_label = Label(word_frame, text=question, font=[" ", 18, "bold"], bg="#ff9f88", fg="white")
    word_label.pack(pady=(20, 10))

    meaning_entry = Entry(word_frame, width=30, font=[" ", 18, "italic"])
    meaning_entry.pack()

    def check_answer(entry, root):
        global correct_score_entry, incorrect_score_entry, na_score_entry

        answer = entry.get()
        entry.delete(0, END)

        status, correct_ans = wgame.answer(answer)

        correct_score_entry.delete(0, END)
        incorrect_score_entry.delete(0, END)
        na_score_entry.delete(0, END)

        correct_score_entry.insert(0, wgame.correct)
        incorrect_score_entry.insert(0, wgame.incorrect)
        na_score_entry.insert(0, wgame.NA)

        status_label = Label(root, text=status, font=[" ", 16, "bold"], bg="#ff9f88", fg="white")
        status_label.pack(pady=(20, 10))

        correct_ans_label = Label(root, text=correct_ans, font=[" ", 16, "bold"], bg="#ff9f88", fg="white")
        correct_ans_label.pack()

        word_label.destroy()
        meaning_entry.destroy()
        submit_button.destroy()

        def clear_ans():
            root.destroy()
            show_word()

        next_button = Button(root, text="Next", width=15, bg="#ff9f23", command=clear_ans)
        next_button.pack(pady=(5, 10))

    submit_button = Button(word_frame, text="Submit", width=15, bg="#ff9f23",
                           command=lambda: check_answer(meaning_entry, word_frame))
    submit_button.pack(pady=(20, 20))


def play():
    global play_screen, correct_score_entry, incorrect_score_entry, na_score_entry

    play_screen = Tk()
    play_screen.title("Word Game")
    # play_screen.geometry("1366x1080")

    # Frame for scoreboard
    scoreboard_frame = Frame(play_screen, bg="#88f9ff")
    scoreboard_frame.pack(fill="x")

    correct_score_label = Label(scoreboard_frame, text="Correct", font=[" ", 12, "bold"], bg="#88f9ff")
    incorrect_score_label = Label(scoreboard_frame, text="Incorrect", font=[" ", 12, "bold"], bg="#88f9ff")
    na_score_label = Label(scoreboard_frame, text="Not Answered", font=[" ", 12, "bold"], bg="#88f9ff")

    correct_score_entry = Entry(scoreboard_frame, width=5)
    incorrect_score_entry = Entry(scoreboard_frame, width=5)
    na_score_entry = Entry(scoreboard_frame, width=5)

    correct_score_label.grid(row=0, column=0, padx=(200, 0))
    incorrect_score_label.grid(row=0, column=2, padx=(300, 0))
    na_score_label.grid(row=0, column=4, padx=(300, 0))

    correct_score_entry.grid(row=0, column=1)
    incorrect_score_entry.grid(row=0, column=3)
    na_score_entry.grid(row=0, column=5, padx=(0, 200))

    # Frame for display words
    show_word()

    play_screen.mainloop()


def main_screen():
    mainscreen = Tk()
    mainscreen.title("Word Game")
    mainscreen.geometry("300x200")

    add_vocab_button = Button(mainscreen, text="Add Vocab", width=15, font=[" ", 12, "bold"], bg="#ff9f23",
                              command=escalate)
    add_vocab_button.pack(pady=(20, 20))

    play_button = Button(mainscreen, text="Play", width=15, font=[" ", 12, "bold"], bg="#ff9f23", command=play)
    play_button.pack(pady=(20, 20))

    mainscreen.mainloop()


if __name__ == "__main__":
    main_screen()
