import pygame, simpleGE, random

"""
Thomas McGovern
03/29/2024
Slide and Catch game
Objective of this assignment is to successfully create and animate a simple object catching game
"""

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ball.png")
        self.setSize(40, 40)
        self.minSpeed = 2
        self.maxSpeed = 6
        self.reset()
        
    def reset(self):
        
        self.y = 20
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class DjMoore(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Djmoore.png")
        self.setSize(100, 100)
        self.position = (320, 400)
        self.moveSpeed = 8
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
 
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("field.png")
        
       
        self.numCoins = 10
        self.score = 0
     

        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10

        
        self.DjMoore = DjMoore(self)
        
        self.coins = []
        for i in range(self.numCoins):
            self.coins.append(Coin(self))
            
        self.sprites = [self.DjMoore, 
                        self.coins,             
                    ]
    def process(self):
        for coin in self.coins:        
            if coin.collidesWith(self.DjMoore):
                   coin.reset()
                   
   



def main():
      
            game = Game()
            game.start()
    
            

            
if __name__ == "__main__":
    main()