import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D6, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder = EncoderHandler()
encoder.pins = ((board.D8, board.D9, board.D10, False),)
keyboard.modules.append(encoder)

keyboard.keymap = [
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.X),
        KC.LCTL(KC.Z), KC.LCTL(KC.LSFT(KC.Z)), KC.F5,
        KC.LCTL(KC.GRAVE), KC.PSCR, KC.MUTE,
    ],
]

encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.MPLY),),
]

if __name__ == "__main__":
    keyboard.go()
