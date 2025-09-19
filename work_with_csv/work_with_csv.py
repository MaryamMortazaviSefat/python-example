import csv
import os

script_dir=os.path.dirname(__file__)
file_path=os.path.join(script_dir,"products.csv")

with open(file_path,"r") as file:
    reader=csv.DictReader(file)
    products=list(reader)

print(products)

new_data=[]
for product in products:
    name=product["Product Name"]
    price=int(product["Price"])
    quantity=int(product["Quantity"])
    total_price= price*quantity
    new_data.append([name,price,quantity,total_price])


new_file_path=os.path.join(script_dir,"new_products.csv")
with open(new_file_path,"w",newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Product Name","Price","Quantity","Total Price"])
    writer.writerows(new_data)