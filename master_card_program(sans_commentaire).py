from microbit import uart,sleep
import radio

class Master_card:
    def __init__(self):
        self._palyer_liste={}
        self.player_answer_list={}

    def get_player(self): 
        radio.on()
        while True:
            serial_number_received=radio.receive()
            if serial_number_received!=None :
                for index in range(len(self._palyer_liste)):
                    if serial_number_received==self._palyer_liste["j"+str(index)]:
                        return None 
                    else:
                        self.set_player_id(serial_number_received,str(len(self._palyer_liste)+1))
                        radio.off()
                        break

    def set_player_id(self,serial_number,id):
        self._palyer_liste ["j"+id]=serial_number
        radio.on()
        while True:
            radio.send(str(serial_number)+":"+"j"+str(id))
            radio.off()
            break

    def set_answer_mode(self):
        radio.on()
        for joueur in self._palyer_liste:
            radio.send("go reply"+":"+"j"+str(joueur))
        radio.off()
        self.get_answer()

    def get_answer(self,time_out=100):
        radio.on()
        for _ in range(time_out):
            answer=radio.receive()
            if answer[0] in ["A","B","C","D"]:
                self.player_answer_list["j"+str(answer[len(answer)-1])]=answer[0]
        radio.off()
                
    def send_player_answer_list(self):
        uart.init(baudrate=115200, bits=8)
        uart.write(str(self.player_answer_list))
        
    def wating(self):
        uart.init(baudrate=115200, bits=8)
        while True :
            message = uart.readall()
            if message!=None :
                if message=="1":  
                    self.get_player()
                if message=="2":
                    self.send_player_answer_list()
                if message=="3":
                    self.set_answer_mode()

master = Master_card()
master.wating()  