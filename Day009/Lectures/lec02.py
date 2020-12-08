capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
print(capitals)
print()

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
print(travel_log)
print()

travel_log = {
    "France": {
        "cities visited": ["Paris", "Lille", "Dijon"],
        "total visits": 12
    },
    "Germany": {
        "cities visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total visits": 5
    }
}
print(travel_log)
print()

travel_log = [
    {
        "country": "France",
        "cities visited": ["Paris", "Lille", "Dijon"],
        "total visits": 12
    },
    {
        "country": "Germany",
        "cities visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total visits": 5
    }
]

print(travel_log)
