from super_market.super_shop import SuperShop
from super_market.store import Store
from super_market.customer import Customer
from super_market.product import Clothing
from super_market.product import Food
from super_market.product import Misc


if __name__ == "__main__":
    def exe():
        print("Please select customer:")
        for i, customer in enumerate(my_shop.customers):
            print("%i| %s" % (i, customer.name))

        customer_id = int(input("Customer > "))

        print("What do you want to sell?")
        for i, product in enumerate(my_shop.storage_facilities.get_item()):
            print("%i| %s: %s" % (i, product.category, product.title))

        product_id = int(input("Product > "))

        my_shop.sell(customer_id, product_id)


    my_shop = SuperShop()

    t_shirt1 = Clothing(10, "M", 'T-Shirt One')
    t_shirt2 = Clothing(70, "S", 'T-Shirt Two')
    apple = Food(20, 'Apple', '04.05.97 - 05.05.05')
    misc = Misc(10, 'Table')
    store1 = Store("NIGHT SHOP SUPER SHOP")

    store1.add_item(t_shirt1)
    store1.add_item(t_shirt2)
    store1.add_item(apple)
    store1.add_item(misc)
    my_shop.add_store(store1)

    customer1 = Customer("Ivan")
    customer2 = Customer("Sanya")
    my_shop.add_customer(customer1)
    my_shop.add_customer(customer2)

    running = True

    while running:
        print(my_shop)
        exe()
        print(my_shop)
        choice = input("Enter Q to quit, or press ENTER to continue")
        if choice.lower() == "q":
            break
