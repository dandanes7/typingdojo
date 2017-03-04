class Character:
    def __init__(self, symbol):
        self.symbol = symbol
        self.marked = False

    def mark(self):
        self.marked = True

    def unmark(self):
        self.marked = False