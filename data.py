import pandas

data = pandas.read_csv("great_leaders.csv")

persons_data = {row["Person"]: row["Work"] for (index, row) in data.iterrows()}
# print(persons_data)