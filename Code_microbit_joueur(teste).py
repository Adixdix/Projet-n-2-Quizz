from microbit import display, Image, button_a, button_b
import radio

class Player:
    def __init__(self,rep):
        self.rep = ["A", "B", "C", "D"]

    def play(self,rep,boucle = True,index = 1):
        display.show(rep[0])
        while boucle:
            if button_a.was_pressed():
                display.show(rep[index % len(rep)])  
                index += 1
                index = index % 4
            if button_b.was_pressed():
                print(rep[index-1])#Attention a enlever a la fin 
                radio.on()
                radio.send(rep[index-1]) 
                radio.off()
                display.show(Image.YES, wait=True)


joueur1 = Player
joueur1.play()