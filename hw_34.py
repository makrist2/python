class Godzilla:

    STOMACH_VOL = 1000

    def __init__(self):
        self.stomach = 0

    def eat(self, person_vol):
        if self.stomach + person_vol >= 0.9 * self.STOMACH_VOL:
            print('GODZILLA FULL!! THANK YOU HUMAN BEINGS!')
        else:
            self.stomach += person_vol
            print('GIMME MORE FOOD ')
        if person_vol > self.STOMACH_VOL:
            print('THIS HUMAN SO BIG THAT GODZILLA CAN\'T PLACE IT IN ITS MOUTH!!11!')


best_godzilla = Godzilla()
best_godzilla.eat(300)
best_godzilla.eat(300)
best_godzilla.eat(300)
best_godzilla.eat(300)
# best_godzilla.eat(10000000)

