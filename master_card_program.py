from microbit import uart
import radio


class Master_card:
    def __init__(self) -> None:
        self._palyer_liste = {}
        self.player_answer_list = {}


    def get_player(self): 
        radio.on()
        while True:
            serial_number_received = radio.receive()
            if serial_number_received != None :
                for index in range(len(self._palyer_liste)):
                    if serial_number_received == self._palyer_liste["j"+str(index)]:
                        return None 
                    else:
                        self.set_player_id(serial_number_received,str(len(self._palyer_liste) + 1 ))
                        break


    def set_player_id(self,serial_number : str ,id : str): 
        self._palyer_liste ["j" + id] = serial_number
        radio.on()
        while True:
            radio.send(str(serial_number)+":"+"j"+str(id)) 
            radio.off()
            break


    def ste_answer_mode(self):
        radio.on()
        for joueur in range(len(self._palyer_liste)):
            radio.send("go reply"+":"+"j"+str(joueur))
        radio.off()


    def get_answer(self,time_out : int) -> dict:
        radio.on()  
        for _ in range(time_out):
            answer = radio.receive()
            if answer[0] in ["A", "B", "C", "D"] :
                self.player_answer_list["j"+str(answer[len(answer)-1])] = answer[0]
                radio.off()

    def get_player_answer_liste(self):
        uart.init(baudrate=115200, bits=8, parity=None, stop=1)
        uart.write(self.player_answer_list)
    
    def send_corrections_answer(self,player_answer_list_corrections):
        for key in player_answer_list_corrections:
            radio.send(str(key)+":"+str(player_answer_list_corrections[key]))
                


if __name__ == "__main__":
    pass