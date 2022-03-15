from tkinter import IntVar, StringVar

import Utils


class Controller(object):
    def __init__(self, app):
        self.tally_0 = IntVar()
        self.tally_1 = IntVar()
        self.tally_2 = IntVar()
        self.tally_3 = IntVar()
        self.tally_4 = IntVar()
        self.tally_5 = IntVar()
        self.tally_6 = IntVar()
        self.tally_7 = IntVar()
        self.tally_8 = IntVar()
        self.tally_9 = IntVar()
        self.pi = StringVar()
        self.paused = False
        self.app = app

    def pause_play(self):
        self.paused = not self.paused

        if self.app.pauseplay['text'] == "Pause":
            self.app.pauseplay['text'] = "Play"
        else:
            self.app.pauseplay['text'] = "Pause"

    def go_to_entry(self): #TODO: complete this
        digit_count = Utils.read_and_tally_digits_up_to_i(self.app.entry.get())

        self.tally_0.set(digit_count[0])
        self.tally_1.set(digit_count[1])
        self.tally_2.set(digit_count[2])
        self.tally_3.set(digit_count[3])
        self.tally_4.set(digit_count[4])
        self.tally_5.set(digit_count[5])
        self.tally_6.set(digit_count[6])
        self.tally_7.set(digit_count[7])
        self.tally_8.set(digit_count[8])
        self.tally_9.set(digit_count[9])
