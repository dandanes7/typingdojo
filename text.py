import random

from character import Character


class Text:
    def __init__(self, paths):
        self.letters = []
        self.code_snippets = self.load_code_snippets(paths)
        selected_fragment = random.randint(0, len(self.code_snippets) - 1)
        for char in self.code_snippets[selected_fragment]:
            if "\n" in char:
                self.letters.append(Character("↵", "\r"))
                self.letters.append(Character(char, "\n"))
            else:
                self.letters.append(Character(char, char))
        self.letters[0].mark()

    def get_plain_text(self):
        str = ''
        for char in self.letters:
            str += char.displayed_symbol
        return str

    def load_code_snippets(self, paths):
        code_snippets = []
        for path in paths:
            with open(path, 'r') as file:
                snippet = file.read()
            code_snippets.append(snippet)
        return code_snippets
