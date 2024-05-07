# Importing the necessary libraries, written by AdamH
from microbit import uart, sleep    # Module for UART communication and sleep.
import radio    # Module for radio communication between micro:bits.

class Master_card:
    """This class represents the master card that manages the players and their responses."""
    def __init__(self):
        """Initializes the master card."""
        self._palyer_liste = {} # Dictionary to store player ID.
        self.player_answer_list = {} #Dictionary to store player responses.

    def get_player(self): 
        """Receives and records player ID."""
        radio.on()  # Activate the radio module
        while True:
            serial_number_received = radio.receive()    # Waiting for a serial number to be received.
            if serial_number_received != None :
                #Checks if the received serial number is already in the player list.
                for index in range(len(self._palyer_liste)):
                    if serial_number_received == self._palyer_liste["j"+str(index)]:
                        return None 
                    else:
                        self.set_player_id(serial_number_received,str(len(self._palyer_liste) + 1 ))
                        radio.off()
                        break

    def set_player_id(self,serial_number,id):
        """Associates an ID with a serial number and sends confirmation to the player.""" 
        self._palyer_liste ["j" + id] = serial_number   # Associates the identifier with the serial number.
        radio.on()  # Activate the radio module.
        while True:
            radio.send(str(serial_number)+":"+"j"+str(id))  # Send confirmation to the player.
            radio.off() # Disables the radio module.
            break

    def set_answer_mode(self):
        """Sends the signal to activate answer mode to all players."""
        radio.on()  # Activate the radio module.
        for joueur in self._palyer_liste:
            radio.send("go reply"+":"+"j"+str(joueur))  # Sends the signal to each player.
        radio.off() # Disables the radio module
        self.get_answer()   # Waiting for player responses

    def get_answer(self,time_out = 100):
        """Receives and records player responses."""
        radio.on()  # Activate the radio module. 
        for _ in range(time_out):
            answer = radio.receive()    # Waits for a response to be received.
            if answer[0] in ["A", "B", "C", "D"] :  # Checks if the answer is a valid letter and saves it with the player ID.
                self.player_answer_list["j"+str(answer[len(answer)-1])] = answer[0]
        radio.off() # Disables the radio module
                
    def send_player_answer_list(self):
        """Sends the list of player responses via UART."""
        uart.init(baudrate=115200, bits=8)  # Initializes UART communication.
        uart.write(str(self.player_answer_list))  # Sends the list of answers.
        
    def wating(self):
        """Waits for user commands via UART.
        1 -> get_player
        2 -> send_player_answer_list
        3 -> set_answer_mode   """
        uart.init(baudrate=115200, bits=8)  # Initializes UART communication.
        while True :
            message = uart.readall()    # Reads commands.
            if message != None :
                if message == "1":  
                    self.get_player()   # Receives player ID.
                if message == "2":
                    self.send_player_answer_list()  # Sends the list of player response.
                if message == "3":
                    self.set_answer_mode()  # Starts response mode for players.

        
master = Master_card()  # Creates an instance of the Master_card class.
master.wating() # Wait for user commands via UART.      