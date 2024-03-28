from microbit import display, Image, button_a, button_b, sleep
import radio

class Master_card:
    def __init__(self) -> None:
        self._palyer_liste = {}


    def get_player(self): 
        radio.on()
        while True:
            serial_number = radio.receive()
            if serial_number != None :
                for index in range(len(self._palyer_liste)):
                    if serial_number == self._palyer_liste[index]:
                        return None 
                    else:
                        self.set_player_id(serial_number,str(len(self._palyer_liste) + 1 ))
                        radio.off()
                        break

    def set_player_id(self,serial_number:int,id:str): 
        self._palyer_liste ["j" + id] = serial_number
        radio.on()
        while True:
            radio.send(serial_number "j"+str(id))
            sleep(50)
            answer = radio.receive()
            if answer == "ok":
                break
            sleep(50)

