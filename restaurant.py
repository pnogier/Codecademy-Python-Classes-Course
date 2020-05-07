# You’ve started position as the lead programmer for the family-style Italian
# restaurant Basta Fazoolin’ with My Heart.
# The restaurant has been doing fantastically and seen a lot of growth lately.
# You’ve been hired to keep things organized.


class Menu():  # Create a Menu class
    # Give Menu a constructor with the five parameters
    # self, name, items,start_time, and end_time.
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # Give our Menu class a string representation method that will tell you
    # the name of the menu.
    # Also, indicate in this representation when the menu is available.
    def __repr__(self):
        return self.name + "'s menu is available from " + \
            str(self.start_time) + " to " + str(self.end_time) + "."

    # A method that returns the total price of a purchase consisiting of
    # all the items in purchased_items.
    def calculate_bill(self, purchased_items):
        count = 0
        for item in purchased_items:
            count += self.items[item]
        return count


# Let’s create our first menu: brunch. Brunch is served from 11am to 4pm.
brunch = Menu("Brunch", {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}, 1100, 1600)

# Let’s create our second menu item early_bird.
# Early-bird Dinners are served from 3pm to 6pm.
early_bird = Menu("Early Bird", {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00,
}, 1500, 1800)

# Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm.
dinner = Menu("Dinner", {
    'crostini with eggplant caponata': 13.00,
    'ceaser salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00,
}, 1700, 2300)

# And let’s create our last menu, kids.
# The kids menu is available from 11am until 9pm.
kids = Menu("Kids", {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}, 1100, 2100)

# Print brunch's string representation.
print(brunch)
# Test out Menu.calculate_bill() over brunch's menu
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# Test out Menu.calculate_bill() over early bird's menu
print(early_bird.calculate_bill(
    ['salumeria plate', 'mushroom ravioli (vegan)']))


class Franchise():  # Let’s create a Franchise class.
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # Give our Franchises a string represenation so that we’ll be able to
    # tell them apart. If we print out a Franchise it should tell us the
    # address of the restaurant.
    def __repr__(self):
        return "The restaurant is located at " + self.address

    # Give Franchise an .available_menus() method that takes in a time
    # parameter and returns a list of the Menu objects that are
    # available at that time.
    def available_menus(self, time):
        available = []  # Create an empty list to stock our availables menus
        for item in self.menus:  # Loop trough menus
            # Check if available at this time
            if time >= item.start_time and time <= item.end_time:
                available.append(item)  # Append it to available menu's list
        return available  # Return the list of Menus object


# Our flagship store is located at "1232 West End Road" and our new
# installment is located at "12 East Mulberry Street".
# Pass in all four menus along with these addresses.
flagship_store = Franchise("1232 West End Road", [
                           brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [
    brunch, early_bird, dinner, kids])
# Testing our method with 12 noon time
print(new_installment.available_menus(1200))
# Another test with 5 pm
print(new_installment.available_menus(1700))


class Business():  # Let’s define a Business class.
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Let’s create our first Business.
# The name is "Basta Fazoolin' with my Heart" and the two franchises
# are flagship_store and new_installment.
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [
                          flagship_store, new_installment])

# Before we create our new business, we’ll need a Franchise
# and before our Franchise we’ll need a menu.
arepas_menu = Menu("Take a' Arepa", {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
}, 1000, 2000)

# Let’s create our first Take a’ Arepa franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
# Then, create our arepa Business
take_a_arepa = Business("Take a' Arepa", [arepas_place])
# Print the take_a_arepa Business firt Franchise's first Menu's string
# representation
print(take_a_arepa.franchises[0].menus[0])
