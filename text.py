import random

from character import Character


class Text:
    java_hello_world = 'public static void main (String argc[]) {\n    System.out.println("Hello World!");\n};'

    go_hello_world = 'func main() {\n    fmt.Println("Hello World!")\n}'

    # dummy_message = (java_hello_world, go_hello_world)
    dummy_message = ("hy{\n}...", "hooo{\n}...")

    def __init__(self):
        self.letters = []
        selected_fragment = random.randint(0, len(self.dummy_message) - 1)
        for char in self.dummy_message[selected_fragment]:
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
