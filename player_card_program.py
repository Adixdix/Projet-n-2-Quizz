from microbit import display, Image, button_a, button_b, sleep
import radio
import random


class Player_card:       
    def __init__(self) -> None:
        self.different_answer = ["A", "B", "C", "D"]
        self.id_player = None
        
        
    def get_serial_number(self,size = 20):
        for _ in range(size):
            serial_number = serial_number + str(random.randint(0,9))
        return serial_number

    def send_serial_number(self,serial_number):
        radio.on()
        while True:
            radio.send(str(serial_number))
            id = radio.receive()
            if id != None and len(id) == 23:
                for index in range(20):
                    serial_number_send = serial_number_send + id[index]
                if serial_number == serial_number_send:                      
                    self.id_player = "j"+str(id[23])
                    radio.send("ok:"+str(self.id_player))
                    radio.off()


    def waiting(self):
        radio.on()
        while True:
            mode = radio.receive()
            for index in range(8):
                mode_ =  mode_ + mode[index]
            if mode[len(mode)] == self.id_player[1] and str(mode_) == "go reply":
                self.response_mode(self.different_answer)


    def response_mode(self,different_answer):
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
                        radio.send(str(different_answer[index-1])+":"+str(self.id_player)) 
                        reception = radio.receive()
                        for i in range(1):
                            reception_ =  reception_ + reception[4 + i]
                        if reception[len(reception)] == self.id_player[1] and  reception_ == "ok":
                            radio.off()
                            break
Player1 = Player_card                        
print(Player1.get_serial_number(Player1))      #Teste a enlever a la fin.
