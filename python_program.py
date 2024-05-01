import serial
import serial.tools.list_ports
import json

class CommunicationMicrobit:
    VID_MICROBIT = 0x0D28  #the VID value of the micro:bit
    PID_MICROBIT = 0x0204  #the PID value of the micro:bit

    def __init__(self):
        self.answer_list = None
        self.baudrate = 115200
        self.port = self.find_microbit_port()
        if self.port:
            self.open_connection()

    def find_microbit_port(self):
        ports = serial.tools.list_ports.comports()
        for p in ports:
            if p.vid == self.VID_MICROBIT and p.pid == self.PID_MICROBIT:
                return p.device
        return None
    
    
    def open_connectionn(self):
        port_opened = False
        error_occurred = False
        self.port = serial.Serial(self.port, self.baudrate)  # Tentative d'ouverture du port série
        if self.port.isOpen():  # Vérification si le port est ouvert
            print("Connection established successfully")
            port_opened = True
        else:
            print("Problem connecting")
            error_occurred = True
        if not port_opened or error_occurred:  # Si une erreur est survenue, réinitialiser le port à None
            self.port = None


    def receive_player_answer_list(self):
        answer_list_invalid = ""
        index = 0
        while True:
            message = self.port.readline().decode('utf-8')
            if message != None:
                while message[index] != "M":
                    answer_list_invalid = answer_list_invalid + message[index]
                    index += 1
                answer_list_valid = answer_list_invalid.replace("'", "\"")
                self.answer_list = json.loads(answer_list_valid)
                return self.answer_list
            else:
                return "No connection"


    def send_data(self, message):
        if self.port:
            self.port.write((message).encode('utf-8'))
        else:
            print("No connection")


    def close_connection(self):
        if self.port:
            self.port.close()


if __name__ == "__main__":
    communication = CommunicationMicrobit()
    communication.recevoir_donnees()

    