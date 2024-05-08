from microbit import display, Image, button_a, button_b, sleep
import radio
import machine

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
            sleep(700)
            if id != None:
                id_receive = ""
                for index in range(len(self.my_serial_number)):
                    if index < len(id):
                        id_receive += id[index]
                    else:
                        break
                if self.my_serial_number == id_receive:
                    print("ok")
                    self.id_player = "j"+str(id[len(id)-1])
                    radio.off()
                    break

    def waiting(self):
        radio.on()
        mode_=""
        while True:
            mode=radio.receive()
            sleep(700)
            if mode!=None:
                for index in range(8):
                    mode_= mode_+mode[index]
                if mode[len(mode)-1] == self.id_player[1] and str(mode_) == "go reply":
                    print("ok")
                    self.response_mode()

    def response_mode(self):
        display.clear()
        index = 0
        while True:
            if button_a.was_pressed():
                display.show(self.different_answer[index % len(self.different_answer)])  
                index += 1
                index = index % 4
            if button_b.was_pressed():
                display.show(Image.YES, wait=True)
                radio.send(str(self.different_answer[index-1])+":"+str(self.id_player))
                print("repose envoier")
                break

player = Player_card()                        
player.send_serial_number()
player.waiting()