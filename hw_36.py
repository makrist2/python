import random


class Vehicle:
    def __init__(self, weight, speed, capacity, year_of_construction, price):
        self.weight = weight
        self.speed = speed
        self.capacity = capacity
        self.year_of_construction = year_of_construction
        self.price = price

    def check_vehicle_for_free_seats(self, lb, up):
        curr_vehicle_volume = 0
        free_space = self.capacity
        free_seats = 0
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


air1 = Airplane(
    weight=180.8,
    speed=1000,
    capacity=850,
    year_of_construction=1970,
    price=300,
    distance_of_flight=10000
)
air1.pretty_print()
air1.arrival()
print('‡‡‡‡‡‡‡‡‡‡‡‡ Get passengers in transport ‡‡‡‡‡‡‡‡‡‡‡‡')
air1.check_vehicle_for_free_seats(lb=1, up=10)
print('\n')
train1 = Train(
    weight=6000,
    speed='Based on train type',
    capacity=500,
    year_of_construction=1756,
    price=40,
    dual_rail=False
)
train1.pretty_print()
train1.speed_check()
print('‡‡‡‡‡‡‡‡‡‡‡‡ Get passengers in transport ‡‡‡‡‡‡‡‡‡‡‡‡')
train1.check_vehicle_for_free_seats(lb=1, up=25)
print('\n')
train2 = Train(
    weight=5000,
    speed='Based on train type',
    capacity=400,
    year_of_construction=2000,
    price=100,
    dual_rail=True
)
train2.pretty_print()
train2.speed_check()
print('‡‡‡‡‡‡‡‡‡‡‡‡ Get passengers in transport ‡‡‡‡‡‡‡‡‡‡‡‡')
train2.check_vehicle_for_free_seats(lb=1, up=40)