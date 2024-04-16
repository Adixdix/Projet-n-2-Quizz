from microbit import display, Image, button_a, button_b, sleep
import radio


class Master_card:
    def __init__(self) -> None:
        self._palyer_liste = {}
        self.player_answer_list = {}


    def get_player(self): 
        radio.on()
        while True:
            serial_number_received = radio.receive()
            if serial_number_received != None and len(serial_number_received) == 20 :
                for index in range(len(self._palyer_liste)):
                    if serial_number_received == self._palyer_liste["j"+str(index)]:
                        return None 
                    else:
                        self.set_player_id(serial_number_received,str(len(self._palyer_liste) + 1 ))
                        break


    def set_player_id(self,serial_number_received : int ,id : str): 
        self._palyer_liste ["j" + id] = serial_number_received
        radio.on()
        while True:
            radio.send(str(serial_number_received)+":"+"j"+str(id))
            sleep(50)
            answer_send = radio.receive()
            if answer_send == "ok":
                radio.off()
                break
            sleep(50)


    def get_answer_mode(self):
        radio.on()
        for joueur in range(len(self._palyer_liste)):
            radio.send("go reply"+":"+"j"+str(joueur))
        radio.off()


    def get_answer(self,time_out : int) -> dict:
        radio.on()  
        for _ in range(time_out):
            answer = radio.receive()
            if answer != None :
                self.player_answer_list["j"+str(answer[1])] = answer[3]
                radio.send("j"+str(answer[1])+":ok")
                radio.off()

    def get_player_answer_liste(self):
        return self.player_answer_list
    
    def send_corrections_answer(self,player_answer_list_corrections):
        for key in player_answer_list_corrections:
            radio.send(str(player_answer_list_corrections[key])+":"+str(key))
                
