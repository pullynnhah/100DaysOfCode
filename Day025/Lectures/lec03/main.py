import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("score_data.csv")
