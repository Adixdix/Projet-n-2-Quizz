# Importing the necessary libraries, written by AdamH
import serial   # Module for serial communication.
import serial.tools.list_ports  # Module for the list of available serial ports.
import json # Module for processing JSON data

class Communication_Microbit:
    """This class handles communication with a micro:bit via a serial port."""
    VID_MICROBIT = 0x0D28  #the VID value of the micro:bit
    PID_MICROBIT = 0x0204  #the PID value of the micro:bit

    def __init__(self):
        """Initializes the CommunicationMicrobit class."""
        self.answer_list = None # Initializes the list of player responses to None.
        self.baudrate = 115200  # Transmission speed in bauds.
        self.port = self.find_microbit_port()   # Search for the micro:bit serial port.
        if self.port:
            self.open_connection()  # Opens the connection with the micro:bit.

    def find_microbit_port(self) -> str:
        """Finds the serial port the micro:bit is connected to."""
        ports = serial.tools.list_ports.comports()  # List all available serial ports.
        for p in ports:
            if p.vid == self.VID_MICROBIT and p.pid == self.PID_MICROBIT:   # Checks if the port VID and PID match those of the micro:bit.
                return p.device # Returns the serial port name if the micro:bit is found.
        return None # Returns None if the micro:bit is not found.
    
    
    def open_connection(self):
        """Opens the serial connection with the micro:bit."""
        port_opened = False # Indicates whether the port was opened successfully.
        error_occurred = False  # Indicates if there was an error opening the port.
        self.port = serial.Serial(self.port, self.baudrate) # Attempting to open the serial port.
        if self.port.isOpen():  # Checking if the port is open.
            print("Connection established successfully")
            port_opened = True
        else:
            print("Problem connecting")
            error_occurred = True
        if not port_opened or error_occurred:  # If an error occurred, reset the port to None.
            self.port = None

    def close_connection(self):
        """Close the serial connection with the micro:bit."""
        if self.port:
            self.port.close()   # Close the connection with the micro:bit.

    def receive_player_answer_list(self) -> dict:
        """Receives and processes the list of player responses sent by the micro:bit."""
        answer_list_invalid = ""    # Initialize a string to store the list of responses.
        index = 0
        message = self.port.readline().decode('utf-8')  # Reading the micro:bit message.
        if message != None:
            print(message)
            while message[index] != "M":
                answer_list_invalid = answer_list_invalid + message[index]
                index += 1
            answer_list_valid = answer_list_invalid.replace("'", "\"")  # Replace apostrophes with quotes for JSON format.
            self.answer_list = json.loads(answer_list_valid)    # Converting JSON string to Python dictionary.
            return self.letter_to_index_transformation()    # Transformation of letters into numerical indexes.
        else:
            return "No connection"
                
    def letter_to_index_transformation(self) -> dict:
        """Transforms the letters of player responses into numerical indexes."""
        answer_index = {"A": 1, "B": 2, "C": 3, "D": 4} # Letter->index correspondence dictionary.
        for key in self.answer_list:
            self.answer_list[key] = answer_index[self.answer_list[key]] # Replace letters with corresponding indexes.
        return self.answer_list

    def get_player(self):
        """Allows you to add a player."""
        self.port.write(get_player.encode('utf-8'))
        
    def send_player_answer_list(self):
        """Allows you to ask the master microbit card to send the list of responses."""
        self.port.write(send_player_answer_list.encode('utf-8'))

    def set_answer_mode_player(self):
        """Allows you to switch the microbit player to response mode."""
        self.port.write(set_answer_mode_player.encode('utf-8'))