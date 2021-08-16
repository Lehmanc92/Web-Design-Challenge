import pandas as pd

data = pd.read_csv("../assets/cities.csv")

html = data.to_html(index=False)

table = open("tablehtml.txt", "w")
table.write(html)
table.close()