from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        
    
    def update_score(self):
        self.write(f'Score: {self.score}', False, font=FONT)
        
    def game_is_over(self):
        self.goto(0,0)
        self.write('GAME OVER', False, align =ALIGNMENT, font=FONT)
    
    def current_score(self):
        self.clear()
        self.score += 1
        self.update_score()
        
        
        
    
    
        