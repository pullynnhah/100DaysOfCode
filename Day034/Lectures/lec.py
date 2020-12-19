age: int
name: str
height: float
is_human: bool

age = 24
name = "Paula"
height = 1.62
is_human = True

print(age, name, height, is_human)


def police_check(person_age: int) -> bool:
    return person_age > 18


age = int(input("Your age: "))
if police_check(age):
    print("You may pass")
else:
    print("Pay a fine.")
