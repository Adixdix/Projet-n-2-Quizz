from microbit import display, Image, button_a, button_b, sleep
import radio
import random

class Player_card:
    def __init__(self) -> None:
        self.different_answer = ["A", "B", "C", "D"]


    def get_serial_number(self,size = 20):
        set_serial_number = ""
        for _ in range(size):
            serial_number = set_serial_number + str(random.randint(0,9))
            return(serial_number)


    def send_serial_number(self,serial_number):
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


    def waiting(self,id_player):
        radio.on()
        while True:
            mode = radio.receive()
            for index in range(8):
                mode_ =  mode_ + mode[index]
            if mode[len(mode)] == id_player[1] and str(mode_) == "go reply":
                self.response_mode(self.different_answer)



    def response_mode(self,different_answer,id_player):
            index = 0
            while True:
                if button_a.was_pressed():
                    display.show(different_answer[index % len(different_answer)])  
                    index += 1
                    index = index % 4
                if button_b.was_pressed():
                    display.show(Image.YES, wait=True)
                    print(different_answer[index-1])#Attention a enlever a la fin 
                    radio.on()
                    while True:
                        radio.send(str(different_answer[index-1])+":"+str(id_player)) 
                        reception = radio.receive()
                        for i in range(1):
                            reception_ =  reception_ + reception[4 + i]
                        if reception[len(reception)] == id_player[1] and  reception_ == "ok":
                            radio.off()
                            break