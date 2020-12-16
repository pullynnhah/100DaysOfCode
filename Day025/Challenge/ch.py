import pandas

data = pandas.read_csv('squirrel_census.csv')

black_count = len(data[data['Primary Fur Color'] == "Black"])
cinnamon_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
gray_count = len(data[data['Primary Fur Color'] == "Gray"])

colors_dict = {
    'Fur Color': ['Black', 'Cinnamon', 'Gray'],
    'Count': [black_count, cinnamon_count, gray_count]
}

new_data = pandas.DataFrame(colors_dict)
new_data.to_csv('color_data.csv')
