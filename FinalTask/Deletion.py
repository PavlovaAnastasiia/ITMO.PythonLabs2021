def deletion():
    print("You have decided to delete some info...")
    filename = "shop_list.csv"
    shoplist = open(filename, "w")
    shoplist.truncate()
    shoplist.close()