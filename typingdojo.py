from tkinter.font import Font

import time

from text import Text
from tkinter import *
from state import State

# TODO: should fetch snippets from github repository
# pass github repo address as command line arg
PATHS = ("sample_code_java.txt", "sample_code_go.txt")
BACKGROUND_COLOR = "#CFD8DC"

class TypingDojoGui:
    def __init__(self):
        self.root = Tk()
        self.state = State(PATHS)
        self.current_finger = StringVar()
        self.score_label_text = StringVar()
        self.set_up_gui()
        self.root.title("Typing Dojo")
        self.root.geometry("800x500+350+70")
        self.root.resizable(0, 0)
        self.root.config(bg=BACKGROUND_COLOR)

    def set_up_gui(self):
        self.code_fragment_text = Text(self.root, width=110, height=10, relief=SUNKEN)
        self.current_finger_label = Label(self.root, width=110, justify='center', bg=BACKGROUND_COLOR,
                                          highlightbackground=BACKGROUND_COLOR, textvariable=self.current_finger)
        self.hands_image_label = Label(self.root, width=300, height=200, bg=BACKGROUND_COLOR,
                                       highlightbackground=BACKGROUND_COLOR)
        self.score_label = Label(self.root, width=110, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR,
                                 justify='center', textvariable=self.score_label_text)
        self.code_fragment_text.pack()
        self.current_finger_label.pack()
        self.hands_image_label.pack()
        self.score_label.pack()

        self.code_fragment_text.tag_config('0' + 'CURRENT', background='yellow')

        for character_index in range(len(self.state.text.get_plain_text())):
            self.code_fragment_text.insert('insert', self.state.get_char_at(character_index).displayed_symbol,
                                           character_index)

        self.photo = PhotoImage(file="hands.gif")
        self.hands_image_label.configure(image=self.photo)

        # Press ESC to exit
        self.root.bind("<Escape>", self.quit)
        self.root.bind("<Key>", self.type_key)

        self.code_fragment_text.configure(state="disabled")
        self.hands_image_label.configure(state="disabled")

        self.regular_font = Font(family="Mono", size=10, weight="normal")
        self.bold_font = Font(family="Mono", size=11, weight="bold")

        self.refresh_markings()
        self.root.update()

    def type_key(self, event):
        char_pressed = event.char
        # treat backspace key press separately
        if char_pressed == '\b' and self.state.current_key_index != 0:
            self.state.unmark_current_character()
            self.state.mark_previous_character()
            self.root.update()
            self.refresh_markings()
        # Don't want to handle cases when user presses <Shift> or <Ctrl>
        elif not char_pressed == '':
            self.state.increment_keys_pressed_counter()
            print(repr(char_pressed))  # For debugging

            if char_pressed == self.state.get_char_at_current_index().value:
                if self.check_game_finished():
                    return
                self.state.unmark_current_character()
                self.state.mark_next_character()
            else:
                self.state.increment_error_counter()
        self.refresh_markings()

    def refresh_markings(self):
        self.update_score()
        self.update_current_finger()
        for index in range(len(self.state.text.letters)):
            if self.state.text.letters[index].marked:
                self.code_fragment_text.tag_config(index, background='yellow')
                self.code_fragment_text.tag_config(index, font=self.bold_font)
            else:
                self.code_fragment_text.tag_config(index, background='white')
                self.code_fragment_text.tag_config(index, font=self.regular_font)

    def update_current_finger(self):
        finger = self.state.get_current_finger()
        self.current_finger.set(finger)

    def update_score(self):
        if (self.state.keys_pressed_counter == 0):
            accuracy = 0
        else:
            accuracy = (
                       self.state.keys_pressed_counter - self.state.error_counter) * 100 // self.state.keys_pressed_counter
        self.score_label_text.set("You have " + str(self.state.error_counter) + " errors out of " +
                                  str(self.state.keys_pressed_counter) + " touches.\n" +
                                  "Accuracy:" + str(accuracy) + "%")

    def run(self):
        self.root.mainloop()

    def check_game_finished(self):
        if self.state.current_key_index == len(self.state.text.get_plain_text()) - 1:
            # Wait a few seconds before refreshing game, so that the player can see score & accuracy
            time.sleep(3)  # TODO: find something better than sleep to show that current game ended
            self.state = State(PATHS)
            # In order to be able to call delete or insert on the text widget, it has to be in 'normal' state
            self.code_fragment_text.configure(state="normal")
            self.code_fragment_text.delete(1.0, END)
            for character_index in range(len(self.state.text.get_plain_text())):
                self.code_fragment_text.insert('insert', self.state.get_char_at(character_index).displayed_symbol,
                                               character_index)
            self.code_fragment_text.configure(state="disabled")
            self.state.mark_first()
            self.refresh_markings()
            self.root.update()
            return True
        else:
            return False

    def quit(self, event):
        self.root.quit()
        quit()


if __name__ == '__main__':
    typing_dojo_gui = TypingDojoGui()
    typing_dojo_gui.run()
