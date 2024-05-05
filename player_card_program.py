# Importing the necessary libraries.
from microbit import display, Image, button_a, button_b # Module to interact with the micro:bit.
import radio    # Module for radio communication between micro:bit.
import machine  # Module for access to micro:bit hardware.

class Player_card:
    """This class represents the player card that communicates with other micro:bits via radio."""
    def __init__(self) -> None:
        """Initializes the player card."""
        self.different_answer = ["A", "B", "C", "D"]    # List of possible answers.
        self.id_player = None   # Player ID.
        self.my_serial_number = self.get_serial_number()    # Obtains the unique serial number of the micro:bit.
        
    def get_serial_number(self):
        """Gets the unique serial number of the micro:bit."""
        self.my_serial_number = ''.join([hex(n)[2:] if len(hex(n)) == 4 else '0'+hex(n)[2:] for n in list( machine.unique_id())])        
        # Gets the unique serial number and converts it to a hexadecimal string.
        return self.my_serial_number
        
    def send_serial_number(self) -> str:
        """Sends the unique serial number via radio and waits for confirmation of receipt."""
        radio.on()  # Activate the radio module.
        while True:
            radio.send(str(self.my_serial_number))  # Send serial number.
            id = radio.receive()    # Wait for a message to be received
            if id != None:
                id_receive = "" # Initialize the string to store the received ID.
                for index in range(len(self.my_serial_number)):
                    id_receive = id_receive + id[index] # Get the received ID.
                if self.my_serial_number == id_receive: # Checks if the received ID matches the serial number of this micro:bit.
                    self.id_player = "j"+str(id[len(id)])   # Assigns a unique ID to the player.
                    radio.off() # Disables the radio module.
                    break

    def waiting(self):
        """Waits for response mode start signal."""
        radio.on()  # Activate the radio module.
        while True:
            mode = radio.receive()  # Wait for start signal.
            mode_ = ""  # Initialize the string to store the received mode.
            for index in range(8):
                mode_ =  mode_ + mode[index]    # Get received mode.
            if mode[len(mode)] == self.id_player[1] and str(mode_) == "go reply":   # Checks if the received mode matches.
                self.response_mode(self.different_answer)   # Starts reply mode.

    def response_mode(self,different_answer):
            """Handles response mode where the player can choose a response and send it via radio."""
            index = 0   # Initializes the index to browse possible answers.
            while True:
                if button_a.was_pressed():
                    display.show(different_answer[index % len(different_answer)])   # Displays the selected answer.
                    index += 1  # Move to the next response
                    index = index % 4   # Ensures the index remains within the range of possible answers.
                if button_b.was_pressed():
                    display.show(Image.YES, wait=True)  # Shows a visual confirmation that the response has been sent 
                    radio.on()  # Activate the radio module.
                    radio.send(str(different_answer[index-1])+":"+str(self.id_player))  # Sends selected response and player ID via radio.
                    radio.off() # Disables the radio module.
                    break   # Exits the loop.

player = Player_card()  # Creates an instance of the Player_card class.
player.send_serial_number() # Sends the unique serial number and waits for confirmation of receipt.
player.waiting()# Wait for response mode start signal.

