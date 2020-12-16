def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


weather_celsius = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_fahrenheit = {day: celsius_to_fahrenheit(celsius) for (day, celsius) in weather_celsius.items()}
print(weather_fahrenheit)
