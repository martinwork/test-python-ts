def Update():
    global row1str, row2str
    if time > -1:
        # read notes list and deal with row1
        row16 = row15
        row15 = row14
        row14 = row13
        row13 = row12
        row12 = row11
        row11 = row10
        row10 = row9
        row9 = row8
        row8 = row7
        row7 = row6
        row6 = row5
        row5 = row4
        row4 = row3
        row3 = row2
        row2 = row1
        if notes[time] == 1:
            pass
        if notes[time] == 2:
            pass
        if notes[time] == 0:
            pass
        # Button sound test
        if not (CheckB == 1):
            music.ring_tone(262)
        else:
            music.rest(1)
        row1str = "UNDER"
        row2str = "CONSTRUCTION"
        music.set_volume(40)
        makerbit.show_string_on_lcd1602(row1str, makerbit.position1602(LcdPosition1602.POS1), 16)
        makerbit.show_string_on_lcd1602(row2str, makerbit.position1602(LcdPosition1602.POS17), 16)
B = 0
Y = 0
X = 0
row2str = ""
row1str = ""
CheckB = 0
notes: List[number] = []
time = 0
row1: List[number] = []
pressed_last_tick = 0
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
makerbit.connect_lcd(39)
time = -2
once = True
notes = [0,
    1,
    2,
    2,
    1,
    0,
    1,
    0,
    2,
    1,
    2,
    0,
    2,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0]
bpm = 60
tbb = 25 / bpm

def on_forever():
    global B, CheckB
    # Joystick test
    if X > 700:
        led.plot(2, 2)
    else:
        led.unplot(2, 2)
    X_joy = pins.analog_read_pin(AnalogPin.P1)
    Y_joy = pins.analog_read_pin(AnalogPin.P0)
    B = pins.analog_read_pin(AnalogPin.P2)
    CheckB = pins.digital_read_pin(DigitalPin.P5)
    if CheckB == 1:
        led.unplot(1, 1)
        pressed_last_tick == 0
    else:
        led.plot(1, 1)
        pressed_last_tick == 1
basic.forever(on_forever)

def on_every_interval():
    global time
    time += 1
    Update()
loops.every_interval(tbb * 1000, on_every_interval)
