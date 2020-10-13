def on_button_pressed_a():
    global svar
    for index in range(10):
        svar = svar + gangen
        OLED.write_num(svar)
        OLED.write_string("-")
    basic.pause(5000)
    OLED.clear()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global svar
    for index2 in range(10):
        svar = svar + gangen_4
        OLED.write_num(svar)
        OLED.write_string("-")
    basic.pause(5000)
    OLED.clear()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global svar
    for index3 in range(10):
        svar = svar + gangen_3
        OLED.write_num(svar)
        OLED.write_string("-")
    basic.pause(5000)
    OLED.clear()
input.on_button_pressed(Button.B, on_button_pressed_b)

gangen_4 = 0
gangen_3 = 0
gangen = 0
svar = 0
OLED.init(128, 64)
svar = 0
gangen = 2
gangen_3 = 3
gangen_4 = 4