import pandas

data = pandas.read_csv("weather_data.csv")

print(data)
print()

print(data["temp"])
print()

print(type(data))
print(type(data["temp"]))
print()

data_dict = data.to_dict()
print(data_dict)
print()

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))
print()

print(sum(temp_list) / len(temp_list))
print(data["temp"].mean())
print()

print(data["temp"].max())
print()

print(data["condition"])
print()

print(data.condition)
print()

print(data[data.day == "Monday"])
print()

print(data[data.temp == data.temp.max()])
print()

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp_F = monday.temp * 9 / 5 + 32
print(monday_temp_F)
