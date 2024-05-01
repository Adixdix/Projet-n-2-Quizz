from microbit import uart, sleep
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
        dico = {"A":1,"B":2,"C":3,"D":4}
        for index in range(len(self.player_answer_list)):
            self.get_player_answer_liste[index] = dico[self.get_player_answer_liste[index]]
        uart.init(baudrate=115200, bits=8)
        uart.write(self.get_player_answer_liste)
    
    def send_corrections_answer(self,player_answer_list_corrections):
        for key in player_answer_list_corrections:
            radio.send(str(key)+":"+str(player_answer_list_corrections[key]))
                


if __name__ == "__main__":
    teste = Master_card()
    while True:
        sleep(500)
        teste.get_player_answer_liste()