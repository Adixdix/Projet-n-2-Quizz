from microbit import display, Image, button_a, button_b, sleep
import radio
import random


def get_serial_number(size = 20):
    set_serial_number = ""
    for _ in range(size):
        serial_number = set_serial_number + str(random.randint(0,9))
        return(serial_number)

def send_serial_number(serial_number):
    radio.on()
    while True:
        radio.send(str(serial_number))
        id = radio.receive()
        if id != None and len(id) == 23:
            for index in range(20):
                serial_number_send = serial_number_send + id[index]
            if serial_number == serial_number_send:
                id_player = "j"+str(id[23])
                return id_player


def main(serial_number):
    radio.on()
    while True:
        mode = radio.receive()
        if mode  == "go reply"+str(serial_number)