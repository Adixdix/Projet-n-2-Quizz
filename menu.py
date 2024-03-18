import pygame as pg
#Joshua LERAS IRIARTE
class Button():
    def __init__(self, image:str, pos:tuple, text_input:str, font, base_color:str):
        """Define the elements of the button : 
        the image, position, text, font  and the color of the button"""
        self.image = image
        
        self.x_pos = pos[0] # position x of the button
        self.y_pos = pos[1] #position y of the button
        
        self.font = font #the font got from the default font of pygame
        self.base_color = base_color # the color of the button
        self.text_input = text_input #the text in the button
        
        self.text = self.font.render(self.text_input, True, self.base_color) #display of the button
        if self.image is None : #if we give no image, there will be only the text
            self.image = self.text
            
        #get_ret() create a rect object(storing a rectangular coordinates) with the size, the image and the x, y coordinate. 
        #We can change the coordinate by passing an argument like center or topleft
        self.image_rect = self.image.get_rect(center=(self.x_pos, self.y_pos))#Assign the center of the image object at x, y coordinate
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos)) #Assign the center of the text object at x, y coordinate
        
    def update(self, screen) -> None:
        """Update the display of the button"""
        if self.image is not None: #if 
            screen.blit(self.image, self.image_rect)
        else:  #if no image is given, only the text
            screen.blit(self.text, self.text_rect)#display the text
    
    def press_button(self, position) -> bool:
        """Check if the mouse press the button
        -Collision is detected if the x coordinate of the mouse is in the button
        -And if the y coordinate is in the button"""
        if position[0] in range(self.image_rect.left, self.image_rect.right) and \
           position[1] in range(self.image_rect.top, self.image_rect.bottom):
            return True
        return False
    
class Menu():
    def __init__(self, title_menu, title_color='white'):
        pg.init()

        self.mouse_pos = pg.mouse.get_pos() #get the coordinate of the mouse on the screen
        
        self.menu_text = pg.font.SysFont("Comic Sans MS", 100).render(title_menu, True, title_color)#get the font with pygame and display the text
        self.menu_rect = self.menu_text.get_rect(center=(425, 100)) #Assign the center of the text object x, y coordinate
        
        self.play_button = Button(image=pg.image.load('assets/play_button.png'), \
                                  pos=(425,300), text_input="PLAY",\
                                  font=pg.font.SysFont("Comic Sans MS", 20), base_color='white')#Give the parameters of the button
        
    def check_button_input(self) -> None:
        """check if the mouse clicked"""
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouse_pos = pg.mouse.get_pos() #reset the mouse position to his actual position when clicked
                return self.play_button.press_button(self.mouse_pos) #check for the button
            if event.type == pg.QUIT:
                pg.quit()
                
    def get_font(self, size:int) :
        """Get the default font of pygame for the button"""
        pg.font.Font(pg.font.get_default_font(), size) #the default font file is: freesansbold.ttf
        
    def update_menu(self, screen) -> None:
        """Update the display of the menu"""
        screen.blit(self.menu_text, self.menu_rect) #Display the text
