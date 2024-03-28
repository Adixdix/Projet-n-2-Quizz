import random
from microbit import display, Image, button_a, button_b, sleep
import radio

def get_serial_number(size = 20):
    set_serial_number = ""
    for _ in range(size):
        set_serial_number = set_serial_number + str(random.randint(0,9))
    return int(set_serial_number)


def teste ():
    radio.on()
    serial_number = get_serial_number()
    while True:
        radio.send()
        sleep(50)
        id = radio.receive()
        if id != None and len(id) == 23:
            for index in range(20):
                serial_number_send = serial_number_send + id[index]
            if serial_number == serial_number_send:
                id_player = "j"+str(id[23])
