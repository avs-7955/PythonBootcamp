travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above


def add_new_country(country_visited, no_of_visits, cities_visited):
    """Takes the country visited, the number of inputs and citites visited as parameters.
    It will then add them into the travel_log list."""
    country_adding = {}
    country_adding["country"] = country_visited
    country_adding["visits"] = no_of_visits
    country_adding["cities"] = cities_visited
    travel_log.append(country_adding)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
