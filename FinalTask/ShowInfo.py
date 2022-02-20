def show_info():
    import pandas
    print("You have decided to show all information.")
    df = pandas.read_csv('shop_list.csv', delimiter=',',
        names=["category", "product", "cost", "date"])
    print(df)