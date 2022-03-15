from tkinter import Tk, Label, Button, Entry
import Controller


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pi Day 2022")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.configure(background="#F0D8AC")
        self.controller = Controller.Controller(self)
        self.create_widgets()

    def create_widgets(self):
        # Creating Canvas
        self.scrolling = Label(self, text="3.14159", font=("Helvetica", 244), bg="#F0D8AC", textvariable=self.controller.pi)
        self.scrolling.pack(expand=True)
        self.scrolling.place(x=0, y=-50)

        # Play/Pause Button
        self.pauseplay = Button(self, text="Pause", bg="#F0D8AC", width=10, height=2)
        self.pauseplay.configure(command=self.controller.pause_play)
        self.pauseplay.pack(expand=True)
        self.pauseplay.place(x=400, y=650)

        # Entry Button
        self.entry = Entry(self, bg="#F0D8AC", width=10)
        self.entry.pack(expand=True, anchor="center")
        self.entry.bind("<Return>", self.controller.go_to_entry)
        self.entry.place(x=600, y=662)

        # Go to Button
        self.go_to = Button(self, text="Go To", bg="#F0D8AC", width=10, height=2)
        self.go_to.pack(expand=True)
        self.go_to.configure(command=self.controller.go_to_entry)
        self.go_to.bind("<Return>", self.controller.go_to_entry)
        self.go_to.place(x=800, y=650)

        # Tally Board
        self.tally_label = Label(self, text="Tally of Digits", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label.pack(expand=True)
        self.tally_label.place(relx=0.5, y=350, anchor="center")

        self.tally_label_0 = Label(self, text="0:", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label_0.pack(expand=True)
        self.tally_label_0.place(x=400, y=400, anchor="center")

        self.tally_label_1 = Label(self, text="1:", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label_1.pack(expand=True)
        self.tally_label_1.place(x=400, y=450, anchor="center")

        self.tally_label_2 = Label(self, text="2:", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label_2.pack(expand=True)
        self.tally_label_2.place(x=400, y=500, anchor="center")

        self.tally_label_3 = Label(self, text="3:", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label_3.pack(expand=True)
        self.tally_label_3.place(x=400, y=550, anchor="center")

        self.tally_label_4 = Label(self, text="4:", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label_4.pack(expand=True)
        self.tally_label_4.place(x=400, y=600, anchor="center")

        self.tally_label_5 = Label(self, text="5:", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label_5.pack(expand=True)
        self.tally_label_5.place(x=800, y=400, anchor="center")

        self.tally_label_6 = Label(self, text="6:", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label_6.pack(expand=True)
        self.tally_label_6.place(x=800, y=450, anchor="center")

        self.tally_label_7 = Label(self, text="7:", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label_7.pack(expand=True)
        self.tally_label_7.place(x=800, y=500, anchor="center")

        self.tally_label_8 = Label(self, text="8:", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label_8.pack(expand=True)
        self.tally_label_8.place(x=800, y=550, anchor="center")

        self.tally_label_9 = Label(self, text="9:", font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_label_9.pack(expand=True)
        self.tally_label_9.place(x=800, y=600, anchor="center")

        self.tally_0 = Label(self, textvariable=self.controller.tally_0, font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_0.pack(expand=True)
        self.tally_0.place(x=425, y=400, anchor="w")

        self.tally_1 = Label(self, textvariable=self.controller.tally_1, font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_1.pack(expand=True)
        self.tally_1.place(x=425, y=450, anchor="w")

        self.tally_2 = Label(self, textvariable=self.controller.tally_2, font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_2.pack(expand=True)
        self.tally_2.place(x=425, y=500, anchor="w")

        self.tally_3 = Label(self, textvariable=self.controller.tally_3, font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_3.pack(expand=True)
        self.tally_3.place(x=425, y=550, anchor="w")

        self.tally_4 = Label(self, textvariable=self.controller.tally_4, font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_4.pack(expand=True)
        self.tally_4.place(x=425, y=600, anchor="w")

        self.tally_5 = Label(self, textvariable=self.controller.tally_5, font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_5.pack(expand=True)
        self.tally_5.place(x=825, y=400, anchor="w")

        self.tally_6 = Label(self, textvariable=self.controller.tally_6, font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_6.pack(expand=True)
        self.tally_6.place(x=825, y=450, anchor="w")

        self.tally_7 = Label(self, textvariable=self.controller.tally_7, font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_7.pack(expand=True)
        self.tally_7.place(x=825, y=500, anchor="w")

        self.tally_8 = Label(self, textvariable=self.controller.tally_8, font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_8.pack(expand=True)
        self.tally_8.place(x=825, y=550, anchor="w")

        self.tally_9 = Label(self, textvariable=self.controller.tally_9, font=("Helvetica", 24), bg="#F0D8AC")
        self.tally_9.pack(expand=True)
        self.tally_9.place(x=825, y=600, anchor="w")

    def destroy(self):
        super().destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
