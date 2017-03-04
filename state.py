from text import Text


class State:
    def __init__(self):
        self.text = Text()
        self.current_key_index = 0
        self.error_counter = 0

    def get_char_at_current_index(self):
        return self.text.letters[self.current_key_index]

    def get_char_at(self, character_index):
        return self.text.letters[character_index]

    def increment_current_index(self):
        self.current_key_index += 1

    def unmark_current_character(self):
        char = self.text.letters[self.current_key_index]
        char.unmark()

    def mark_next_character(self):
        char = self._get_next_char()
        if char.symbol == '\n':
            char = self._get_next_char()
        char.mark()

    def increment_error_counter(self):
        self.error_counter += 1

    def _get_next_char(self):
        self.increment_current_index()
        char = self.text.letters[self.current_key_index]
        return char
        # def check_game_finished(self):
        #     # if self.current_key_index
