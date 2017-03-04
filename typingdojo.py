from tkinter.font import Font

from hands import Hands
from text import Text
from tkinter import *

from state import State


class TypingDojoGui:

    def __init__(self):
        self.state = State()
        self.hands = Hands()
        self.root = Tk()
        self.set_up_gui()
        self.root.title("Typing Dojo")
        self.root.geometry("800x500+350+70")
        self.root.resizable(0,0)

    def set_up_gui(self):

        self.text_label = Text(self.root, width = 110 , relief = SUNKEN)
        self.fingers_label = Text(self.root, width = 110 )
        self.text_label.pack()
        self.fingers_label.pack()

        self.text_label.config(height=10)

        for character_index in range(len(self.state.text.get_plain_text())):
            self.text_label.insert('insert', self.state.get_char_at(character_index).symbol, character_index)

        self.text_label.tag_config('0'+'CURRENT', background='yellow')
        self.fingers_label.tag_configure('tag-center', justify='center')
        # self.fingers_label.insert('end', "HI" * 10, 'tag-center')
        self.fingers_label.insert('end', self.hands.ascii_hands, 'tag-center')

        # Press ESC and the game quits
        self.root.bind("<Escape>", self.quit)
        self.root.bind("<Key>", self.type_key)

        self.text_label.configure(state="disabled")
        self.fingers_label.configure(state="disabled")

        self.regular_font = Font(family="Mono", size=10, weight="normal")
        self.bold_font = Font(family="Mono", size=11, weight="bold")

        self.refresh_markings()
        self.root.update()



    def type_key(self, event):
        # Don't want to handle cases when user presses <Shift> or <Ctrl>
        char_pressed = event.char
        if not char_pressed == '':
            print(repr(char_pressed))

            if char_pressed == self.state.get_char_at_current_index().symbol:
                self.check_game_finished()
                self.state.unmark_current_character()
                self.state.mark_next_character()
                self.refresh_markings()
                self.root.update()
            else:
                self.state.increment_error_counter()

    def refresh_markings(self):
        for index in range(len(self.state.text.letters)):
            if self.state.text.letters[index].marked:
                self.text_label.tag_config(index, background='yellow')
                self.text_label.tag_config(index, font=self.bold_font)
            else:
                self.text_label.tag_config(index, background='white')
                self.text_label.tag_config(index, font=self.regular_font)

    def run(self):
        self.root.mainloop()

    def check_game_finished(self):
        if self.state.current_key_index == len(self.state.text.get_plain_text()) - 1:
            print("end of game, " + str(elf.state.error_counter) + " errors made")
    #         TODO: this one should be changed,

    def quit(self, event):
        self.root.quit()
        quit()

if __name__ == '__main__':
    typing_dojo_gui= TypingDojoGui()
    typing_dojo_gui.run()
