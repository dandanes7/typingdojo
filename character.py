class Character:
    def __init__(self, displayed_symbol, value):
        self.displayed_symbol = displayed_symbol
        self.value = value
        self.marked = False

    def mark(self):
        self.marked = True

    def unmark(self):
        self.marked = False