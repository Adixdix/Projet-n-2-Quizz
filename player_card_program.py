from microbit import display, Image, button_a, button_b
import radio
import machine
import random


class Player_card:
    def __init__(self) -> None:
        self.different_answer = ["A", "B", "C", "D"]
        self.id_player = None
        self.my_serial_number = self.get_serial_number()
        
    def get_serial_number(self):
        self.my_serial_number = ''.join([hex(n)[2:] if len(hex(n)) == 4 else '0'+hex(n)[2:] for n in list( machine.unique_id())])
        return self.my_serial_number

    def send_serial_number(self):
        radio.on()
        while True:
            radio.send(str(self.my_serial_number))
            id = radio.receive()
            if id != None:
                for index in range(len(self.my_serial_number)):
                    id_receive = id_receive + id[index]
                if self.my_serial_number == id_receive:                      
                    self.id_player = "j"+str(id[len(id)])
                    radio.off()
                    break


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
                    radio.send(str(different_answer[index-1])+":"+str(self.id_player)) 
                    radio.off()
                    break



if __name__ == "__main__":
    Player1 = Player_card                        
    print(Player1.get_serial_number(Player1))