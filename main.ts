input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 10; index++) {
        svar = svar + gangen
        OLED.writeNum(svar)
        OLED.writeString("-")
    }
    basic.pause(5000)
    OLED.clear()
})
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 10; index++) {
        svar = svar + gangen_4
        OLED.writeNum(svar)
        OLED.writeString("-")
    }
    basic.pause(5000)
    OLED.clear()
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 10; index++) {
        svar = svar + gangen_3
        OLED.writeNum(svar)
        OLED.writeString("-")
    }
    basic.pause(5000)
    OLED.clear()
})
let gangen_4 = 0
let gangen_3 = 0
let gangen = 0
let svar = 0
OLED.init(128, 64)
svar = 0
gangen = 2
gangen_3 = 3
gangen_4 = 4
