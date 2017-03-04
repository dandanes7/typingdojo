import random

from character import Character


class Text:
    java_hello_world = 'public static void main (String argc[]) {\n    System.out.println("Hello World!");\n};'

    go_hello_world = 'func main() {\n    fmt.Println("Hello World!")\n}'

    dummy_message = (java_hello_world, go_hello_world)

    def __init__(self):
        self.letters = []
        selected_fragment = random.randint(0, len(self.dummy_message) - 1)
        for char in self.dummy_message[selected_fragment]:
            self.letters.append(Character(char))
        self.letters[0].mark()

    def get_plain_text(self):
        str = ''
        for char in self.letters:
            str += char.symbol
        return str
