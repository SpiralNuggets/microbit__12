function ledoff() {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}

let random = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.clearScreen()
    if (random == 2) {
        basic.showString("Yes")
    } else if (random == 1) {
        basic.showString("No")
    }
    
})
function ledon() {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
}

basic.forever(function on_forever() {
    
})
basic.showString("Hello!")
basic.showNumber(0)
