import json


def write_json(name, fav_color, fav_number):
    data = {
        name: {
            "favorite color": fav_color,
            "favorite number": fav_number
        }
    }
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def read_json():
    with open("data.json") as file:
        data = json.load(file)
        print(type(data))
    return data


def main():
    name = input("Name: ")
    fav_color = input("Favorite Color: ")
    fav_number = int(input("Favorite Number: "))
    write_json(name, fav_color, fav_number)
    print(read_json())


main()
