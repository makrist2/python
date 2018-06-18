import random


class Vehicle:
    def __init__(self, weight, speed, capacity, year_of_construction, price):
        self.weight = weight
        self.speed = speed
        self.capacity = capacity
        self.year_of_construction = year_of_construction
        self.price = price

    def is_full(self, lb, up):
        global free_seats
        curr_vehicle_volume = 0
        free_space = self.capacity

        while free_space > 0:
            cap = random.randint(lb, up)
            if free_space >= cap:
                curr_vehicle_volume += cap
                free_space -= cap
                free_seats = self.capacity - curr_vehicle_volume
                print('Current free seats %d, passengers queue = %d' % (free_seats, cap))
            else:
                print('Only %d free seat(s) left, %d passenger(s) can\'t go aboard' % (free_seats, cap))
        print('Ready to go!')

    def pretty_print(self):
        print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')
        print('Weight =', self.weight)
        print('Speed =', self.speed)
        print('Capacity =', self.capacity)
        print('Year of const. =', self.year_of_construction)
        print('Ticket price =', self.price)


class Train(Vehicle):
    def __init__(self, weight, speed, capacity, year_of_construction, price, dual_rail):
        super().__init__(weight, speed, capacity, year_of_construction, price)
        self.dual_rail = dual_rail

    def pretty_print(self):
        super().pretty_print()
        print('Is dual-rail =', self.dual_rail)
        print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')

    def speed_check(self):
        if self.dual_rail:
            self.speed = random.randint(141, 200)
            print('Dual-rail train speed =', self.speed)
        else:
            self.speed = random.randint(40, 100)
            print('Mono-rail train speed =', self.speed)


class Airplane(Vehicle):
    def __init__(self, weight, speed, capacity, year_of_construction, price, distance_of_flight):
        super().__init__(weight, speed, capacity, year_of_construction, price)
        self.distance_of_flight = distance_of_flight

    def arrival(self):
        dof = self.distance_of_flight
        while dof > 0:
            print('%d km till arrival' % dof)
            dof -= self.speed
            if dof == 0:
                print('Welcome to wherever you like!')

    def pretty_print(self):
        super().pretty_print()
        print('Distance of flight =', self.distance_of_flight)
        print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')


air1 = Airplane(180.8, 1000, 850, 1970, 300, 10000)
air1.pretty_print()
air1.arrival()
print('‡‡‡‡‡‡‡‡‡‡‡‡ Get passengers in transport ‡‡‡‡‡‡‡‡‡‡‡‡')
air1.is_full(lb=1, up=10)
print('\n')
train1 = Train(6000, 'Based on train type', 500, 1756, 40, False)
train1.pretty_print()
train1.speed_check()
print('‡‡‡‡‡‡‡‡‡‡‡‡ Get passengers in transport ‡‡‡‡‡‡‡‡‡‡‡‡')
train1.is_full(lb=1, up=25)
print('\n')
train2 = Train(5000, 'Based on train type', 400, 2000, 100, True)
train2.pretty_print()
train2.speed_check()
print('‡‡‡‡‡‡‡‡‡‡‡‡ Get passengers in transport ‡‡‡‡‡‡‡‡‡‡‡‡')
train2.is_full(lb=1, up=40)