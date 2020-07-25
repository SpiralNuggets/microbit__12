def ledoff():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)

random = 0

def on_gesture_shake():
    basic.clear_screen()
    if random == 2:
        basic.show_string("Yes")
    elif random == 1:
        basic.show_string("No")
    else
        basic.show_string("I don't know")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def ledon():
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)

def on_forever():
    pass
basic.forever(on_forever)

basic.show_string("Hello!")
basic.show_number(0)