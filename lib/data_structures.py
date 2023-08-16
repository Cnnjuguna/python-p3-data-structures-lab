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
    return [food["name"] for food in spicy_foods]
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
    for food in spicy_foods:
        cuisine = food.get("cuisine", "Unknown Cuisine")
        heat_level = food.get("heat_level")
        num_of_emojis = "🌶" * heat_level
        food_info = f"{food['name']} ({cuisine}) | Heat Level: {num_of_emojis}"

        print(food_info)
    pass


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
    pass


matching_cuisine = get_spicy_food_by_cuisine(spicy_foods, "American")
print(matching_cuisine)


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get("heat_level", 0) > 5:
            heat_level_emojis = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
    pass


print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    num_foods = len(spicy_foods)
    total_heat_lvl = 0

    for food in spicy_foods:
        total_heat_lvl += food.get("heat_level")

    if num_foods > 0:
        average_heat_lvl = total_heat_lvl / num_foods
        return average_heat_lvl
    else:
        return 0
    pass


averaged_heat_lvl = get_average_heat_level(spicy_foods)
print(f"Avg: {averaged_heat_lvl:2f}")


def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods

    pass


# new_spicy_food = {
#     "name": "Griot",
#     "cuisine": "Haitian",
#     "heat_level": 10,
# }

create_a_spicy_food = create_spicy_food(
    spicy_foods,
    spicy_food={
        "name": "Griot",
        "cuisine": "Haitian",
        "heat_level": 10,
    },
)

print(create_a_spicy_food)
