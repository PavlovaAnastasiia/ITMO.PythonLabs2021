def addition():
    import csv

    filename = "shop_list.csv"
    print("You have decided to add some info.")

    shoplists = ["category", "product", "cost", "date"]
    shop = []
    category = input("Category: ")
    shop.insert(category)
    product = input("Product: ")
    shop.append(product)
    cost = input("Cost: ")
    shop.append(cost)
    date = input("Date in the format (dd/mm/yyyy): \n")
    shop.append(date)

    shoplist = dict(zip(shoplists, shop))
    print(shoplist)

    with open(filename, "w", newline="") as fh:
        writer = csv.DictWriter(fh, quoting=csv.QUOTE_ALL)
        for category, values in sorted(shoplist.items()):
             writer.writerow(dict(category=category, product=product, cost=cost, date=date))

