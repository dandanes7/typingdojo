L1 = "Left 1"
L2 = "Left 2"
L3 = "Left 3"
L4 = "Left 4"
L5 = "Left 5"

R1 = "Right 1"
R2 = "Right 2"
R3 = "Right 3"
R4 = "Right 4"
R5 = "Right 5"

l1r1="Left1 or Right1"

l2 = "left 2"
l3 = "left 3"
l4 = "left 4"
l5 = "left 5"

r2 = "right 2"
r3 = "right 3"
r4 = "right 4"
r5 = "right 5"

FINGER_MAPPING = {l1r1: (" "),
                  l2: ("4", "r", "f", "v", "5", "t", "g", "b"),
                  l3: ("3", "e", "d", "c"),
                  l4: ("2", "w", "s", "x"),
                  l5: ("1", "q", "a", "z", "`"),
                  r2: ("7", "u", "j", "m", "6", "y", "h", "n"),
                  r3: ("8", "i", "k", ","),
                  r4: ("9", "o", "l", "."),
                  r5: ("0", "p", ";", "/", "-", "[", "'", "=", "]", "\\", "↵"),
                  L2: ("$", "R", "F", "V",  "%", "T", "G", "B"),
                  L3: ("#", "E", "D", "C"),
                  L4: ("@", "W", "S", "X"),
                  L5: ("!", "Q", "A", "Z", "~"),
                  R2: ("&", "U", "J", "M", "^", "Y", "H", "N"),
                  R3: ("*", "I", "K", "<"),
                  R4: ("(", "O", "L", ">"),
                  R5: (")", "P", ":", "?", "_", "{", "\"", "+", "}", "|")}

# TODO: indicating the finger by text is counterintuitive
# those two gif hands should be replaced, and the fingers should be highlighted

class Hands:

    def get_finger(self, symbol):

        for key in FINGER_MAPPING:
            if symbol in FINGER_MAPPING[key]:
                if symbol.isspace():
                    finger = l1r1
                elif key[0].isupper():
                    finger = self.add_shift_finger(key)
                else:
                    finger = key
                return finger.upper()

    def add_shift_finger(self, key):
        if key[0] == "L":
            return (key + " & " + R5)
        else:
            return (L5 + " & " + key)



