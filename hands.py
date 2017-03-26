left_thumb = (121,106)
right_thumb = (162,106)
left_index = (81,30)
left_middle = (57,14)
left_ring = (33,22)
left_pinky = (10,44)
right_index = (203,30)
right_middle = (227,14)
right_ring = (250,22)
right_pinky = (274,44)

# Each combination of fingers is mapped to a list that contains:
#  - a list of tuples that represent the coordinates of those fingers that are going to be highlighted
#  - the symbols corresponding to that combination of fingers

# TODO: Classic stuff - this solution is elegant, clearly more intuitive but performance has dropped and the gui freezes when typing too fast...
FINGER_MAPPING = {"thumbs": [[left_thumb, right_thumb],(" ")],
                  "left index": [[left_index],("4", "r", "f", "v", "5", "t", "g", "b")],
                  "left middle": [[left_middle],("3", "e", "d", "c")],
                  "left ring": [[left_ring],("2", "w", "s", "x")],
                  "left pinky": [[left_pinky],("1", "q", "a", "z", "`")],
                  "right index": [[right_index],("7", "u", "j", "m", "6", "y", "h", "n")],
                  "right middle": [[right_middle],("8", "i", "k", ",")],
                  "right ring": [[right_ring],("9", "o", "l", ".")],
                  "right pinky": [[right_pinky],("0", "p", ";", "/", "-", "[", "'", "=", "]", "\\", "↵")],
                  "left index and right pinky": [[left_index,right_pinky],("$", "R", "F", "V",  "%", "T", "G", "B")],
                  "left middle and right pinky": [[left_middle,right_pinky],("#", "E", "D", "C")],
                  "left ring and right pinky": [[left_ring,right_pinky],("@", "W", "S", "X")],
                  "left pinky and right pinky": [[left_pinky,right_pinky],("!", "Q", "A", "Z", "~")],
                  "right index and left pinky": [[right_index,left_pinky],("&", "U", "J", "M", "^", "Y", "H", "N")],
                  "right middle and left pinky": [[right_middle,left_pinky],("*", "I", "K", "<")],
                  "right ring and left pinky": [[right_ring,left_pinky],("(", "O", "L", ">")],
                  "right pinky and left pinky": [[right_pinky,left_pinky],(")", "P", ":", "?", "_", "{", "\"", "+", "}", "|")]}


class Hands:

    @staticmethod
    def get_active_fingers(symbol):
        for key in FINGER_MAPPING:
            if symbol in FINGER_MAPPING[key][1]:
                return FINGER_MAPPING[key][0]

    @staticmethod
    def get_inactive_fingers(symbol):
        inactive_fingers = []
        if (symbol.isspace()):
            for key in FINGER_MAPPING:
                if key is not "thumbs":
                    inactive_fingers.extend(FINGER_MAPPING[key][0])
        else:
            for key in FINGER_MAPPING:
                if symbol not in FINGER_MAPPING[key][1]:
                    inactive_fingers.extend(FINGER_MAPPING[key][0])
        return inactive_fingers