def on_button_pressed_a():
    RingbitCar.freestyle(0, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)

def on_forever():
    pass
basic.forever(on_forever)
