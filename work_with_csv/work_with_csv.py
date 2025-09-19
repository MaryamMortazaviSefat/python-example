import csv

with open("products.csv","r", encoding="utf-8") as file:
    reader=csv.DictReader(file)
    products=list(reader)