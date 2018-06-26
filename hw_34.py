class Godzilla:
    STOMACH_LIM = 0.9

    def __init__(self, stomach_vol):
        self.stomach = 0
        self.stomach_vol = stomach_vol

    def eat(self, person_vol):
        if self.stomach + person_vol >= self.STOMACH_LIM * self.stomach_vol:
            print('GODZILLA FULL!! THANK YOU HUMAN BEINGS!')
        else:
            self.stomach += person_vol
            print('GIMME MORE FOOD ')
        if person_vol > self.stomach_vol:
            print('THIS HUMAN SO BIG GODZILLA CAN\'T PLACE IT IN ITS MOUTH!!11!')


best_godzilla = Godzilla(1000)
best_godzilla.eat(300)
best_godzilla.eat(300)
best_godzilla.eat(300)
best_godzilla.eat(300)
best_godzilla.eat(100000)