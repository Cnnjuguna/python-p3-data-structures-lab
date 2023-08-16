spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    for food in spicy_foods:
        print(food["name"])
    pass


def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food.get("heat_level", 0) > 5:
            spiciest_foods.append(food)
    return spiciest_foods
    pass


get_spiciest_foods(spicy_foods)


def print_spicy_foods(spicy_foods):
    pass


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass


def print_spiciest_foods(spicy_foods):
    pass


def get_average_heat_level(spicy_foods):
    pass


def create_spicy_food(spicy_foods, spicy_food):
    pass
